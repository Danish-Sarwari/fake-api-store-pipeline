import requests
from .config import BASE_URL


def fetch_products_data():
    """Fetch the raw data from the /products endpoint"""

    response = requests.get(f"{BASE_URL}/products", timeout=10)
    response.raise_for_status()
    return response.json()


def fetch_users_data():
    """Fetch the raw data from the /users endpoint"""

    response = requests.get(f"{BASE_URL}/users", timeout=10)
    response.raise_for_status()

    return response.json()


def fetch_carts_data():
    """Fetch the raw data from the /carts endpoint"""

    response = requests.get(f"{BASE_URL}/carts", timeout=10)
    response.raise_for_status()

    return response.json()


# NOTE: removed `print(fetch_carts_data())` that used to sit here.
# It fired a live network request every time this module was *imported*
# (e.g. from main.py), which is a side effect a module should never have.
# If you want to test this file directly, use the block below instead:
if __name__ == "__main__":
    print(fetch_carts_data())