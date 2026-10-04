import pandas as pd


def tranform_products(raw_data):
    """Maps product data to a clean and standardized schema."""
    df = pd.DataFrame(raw_data)

    # Rename columns
    df = df.rename(
        columns={
            "id": "product_id",
            "title": "product_name",
            "price": "product_price",
            "description": "description",
            "category": "product_category"
        }
    )

    if "rating" in df.columns:
        df["rating_rate"] = df["rating"].apply(
            lambda x: x.get('rate') if isinstance(x, dict) else None
        )

        df["rating_count"] = df["rating"].apply(
            lambda x: x.get('count') if isinstance(x, dict) else None
        )

        df = df.drop(columns=["rating"])

    # Column selection & type Casting
    df["product_price"] = df["product_price"].astype(float)

    selected_cols = [
        "product_id", "product_name", "product_price", "description",
        "product_category", "rating_rate", "rating_count"
    ]

    return df[selected_cols]


def transform_users(raw_data):
    """This flattens the nested JSON structure (address, name)."""

    df = pd.json_normalize(raw_data)

    df = df.rename(
        columns={
            "id": "user_id",
            "email": "email",
            "username": "username",
            "phone": "phone",
            "name.firstname": "FirstName",
            "name.lastname": "LastName",
            "address.city": "city",
            "address.street": "street",
            "address.number": "house_number",
            "address.zipcode": "zipcode",
            "address.geolocation.lat": "latitude",
            "address.geolocation.long": "longitude"
        }
    )

    selected_cols = [
        "user_id", "email", "username", "FirstName", "LastName",
        "phone", "city", "street", "house_number", "zipcode", "latitude", "longitude"
    ]

    return df[selected_cols]


def transform_carts(raw_data):
    """Explodes/normalizes the nested product list within the carts."""

    carts_list = []

    for cart in raw_data:
        for item in cart.get("products", []):
            carts_list.append(
                {
                    "cart_id": cart.get("id"),
                    "user_id": cart.get("userId"),
                    "date": cart.get("date"),
                    "product_id": item.get("productId"),
                    "quantity": item.get("quantity")
                }
            )

    df = pd.DataFrame(carts_list)
    df["date"] = pd.to_datetime(df["date"])

    return df
