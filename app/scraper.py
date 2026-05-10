from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

import json
import time

# Chrome setup
options = Options()
options.add_argument("--start-maximized")

# launch browser
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# technical queries to scrape
queries = [
    "java",
    ".net",
    "python",
    "developer",
    "backend",
    "frontend",
    "cloud",
    "software",
    "react",
    "spring",
    "django"
]

all_products = []

for query in queries:

    print(f"\nSearching for: {query}")

    url = f"https://www.shl.com/products/product-catalog/?type=1&q={query}"

    driver.get(url)

    time.sleep(5)

    links = driver.find_elements(By.TAG_NAME, "a")

    for link in links:

        text = link.text.strip()

        href = link.get_attribute("href")

        if (
            href
            and "/products/product-catalog/view/" in href
            and text
        ):

            product = {
                "name": text,
                "url": href
            }

            if product not in all_products:

                all_products.append(product)

                print("Added:", text)

driver.quit()

# save catalog
with open("catalog.json", "w", encoding="utf-8") as f:

    json.dump(all_products, f, indent=2)

print(f"\nSaved {len(all_products)} products!")