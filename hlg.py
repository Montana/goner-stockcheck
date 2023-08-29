import requests
from bs4 import BeautifulSoup

def check_product_stock(product_url):
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
    }

    response = requests.get(product_url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        availability_element = soup.select_one(".availability")

        if availability_element:
            if "out of stock" in availability_element.get_text().lower():
                return False
            else:
                return True
        else:
            return None
    else:
        print("Failed to fetch the product page.")
        return None


def main():
    product_url = "https://shop.howlonggone.com/products/gonetourage-hat-navy-blue"

    stock_status = check_product_stock(product_url)

    if stock_status is None:
        print("Failed to determine stock status.")
    elif stock_status:
        print("Product is in stock.")
    else:
        print("Product is out of stock.")


if __name__ == "__main__":
    main()
