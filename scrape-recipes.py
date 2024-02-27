import argparse
import json
import logging
import asyncio
from itertools import chain

import aiohttp
from bs4 import BeautifulSoup

BASE_URL = "https://panlasangpinoy.com/categories/recipes"
INGREDIENT_CLASS = "wprm-recipe-ingredient-name"
NAME_CLASS = "wprm-recipe-name"
INSTRUCTION_CLASS = "wprm-recipe-instruction-text"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


async def get_recipe_links(session, page_url):
    logging.info(f"Scraping: {page_url}")
    async with session.get(page_url) as response:
        soup = BeautifulSoup(await response.text(), "html.parser")
    a_tags = soup.find_all("a", class_="entry-title-link", href=True)
    return [a_tag["href"] for a_tag in a_tags]


async def scrape_recipe_details(session, link):
    data = {
        "link": link,
        "name": None,
        "ingredients": None,
        "instructions": None,
    }

    logging.info(f"Scraping: {link}")
    async with session.get(link) as response:
        soup = BeautifulSoup(await response.text(), "html.parser")

    container = soup.find("div", class_="oc-recipe-container")

    if not container:
        logging.warning(f"Could not find recipe container: {link}")
        return data

    data["name"] = container.find("h2", class_=NAME_CLASS).text.strip()
    data["ingredients"] = [
        ingr.text.strip()
        for ingr in container.find_all("span", class_=INGREDIENT_CLASS)
    ]
    data["instructions"] = [
        instr.text.strip()
        for instr in container.find_all("div", class_=INSTRUCTION_CLASS)
    ]
    return data


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Scrape Panlasang Pinoy recipes",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-p",
        "--pages",
        help="Number of list pages to scrape",
        type=int,
        metavar="N",
        required=True,
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Output file name",
        metavar="FILE",
        default="panlasang_pinoy_recipes.json",
    )
    return parser.parse_args()


async def main():
    args = parse_arguments()

    async with aiohttp.ClientSession() as session:
        list_pages = [f"{BASE_URL}/page/{i}" for i in range(1, args.pages + 1)]
        recipe_links = await asyncio.gather(
            *[get_recipe_links(session, url) for url in list_pages]
        )
        recipe_links = list(chain.from_iterable(recipe_links))

        recipe_data = await asyncio.gather(
            *[scrape_recipe_details(session, url) for url in recipe_links]
        )

    with open(args.output, "w") as file:
        json.dump(recipe_data, file, indent=2)


if __name__ == "__main__":
    asyncio.run(main())
