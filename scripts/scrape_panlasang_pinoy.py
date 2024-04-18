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


async def fetch_and_parse_html(session, url):
    """Fetch a webpage and return a parsed HTML."""
    async with session.get(url) as response:
        return BeautifulSoup(await response.text(), "html.parser")


def extract_elements(container, class_name):
    """Extract and return text from HTML elements based on class name."""
    return [
        element.text.strip()
        for element in container.find_all(class_=class_name)
    ]


async def fetch_recipe_links(session, link):
    """Fetch recipe links from a list page."""
    logging.info(f"Scraping: {link}")
    soup = await fetch_and_parse_html(session, link)
    a_tags = soup.find_all("a", class_="entry-title-link", href=True)
    return [a_tag["href"] for a_tag in a_tags]


async def fetch_recipe_details(session, link):
    """Fetch recipe details from a recipe page."""
    data = {
        "link": link,
        "name": None,
        "ingredients": None,
        "instructions": None,
    }

    logging.info(f"Scraping: {link}")
    soup = await fetch_and_parse_html(session, link)
    container = soup.find("div", class_="oc-recipe-container")

    if not container:
        logging.warning(f"Could not find recipe container: {link}")
        return data

    data["name"] = container.find("h2", class_=NAME_CLASS).text.strip()
    data["ingredients"] = extract_elements(container, INGREDIENT_CLASS)
    data["instructions"] = extract_elements(container, INSTRUCTION_CLASS)
    return data


def configure_argument_parser(description):
    """Create and return a configured argument parser."""
    parser = argparse.ArgumentParser(
        description=description,
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
        default="scraped_recipes.json",
    )
    return parser


async def main():
    """Main entry point of the script."""
    parser = configure_argument_parser("Scrape Panlasang Pinoy recipes")
    args = parser.parse_args()

    async with aiohttp.ClientSession() as session:
        list_pages = [f"{BASE_URL}/page/{i}" for i in range(1, args.pages + 1)]
        recipe_links = await asyncio.gather(
            *[fetch_recipe_links(session, url) for url in list_pages]
        )
        recipe_links = list(chain.from_iterable(recipe_links))

        recipe_data = await asyncio.gather(
            *[fetch_recipe_details(session, url) for url in recipe_links]
        )

    with open(args.output, "w") as file:
        json.dump(recipe_data, file, indent=2)


if __name__ == "__main__":
    asyncio.run(main())
