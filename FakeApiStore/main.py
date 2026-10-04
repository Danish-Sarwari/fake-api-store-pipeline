from ETL.extract import fetch_products_data, fetch_users_data, fetch_carts_data
from ETL.transform import tranform_products, transform_users, transform_carts
from ETL.load import load_to_mssql
from sqlalchemy import DateTime


def run_pipeline():

    print("Starting FakeStore ETL Pipeline...\n")

    # 1. Process Products
    try:
        print("Fetching Products...")
        raw_products = fetch_products_data()
        df_products = tranform_products(raw_products)
        load_to_mssql(df_products, "products")
    except Exception as e:
        print(f"Products Pipeline Failed: {e}")

    # 2. Process Users
    try:
        print("Fetching Users...")
        raw_users = fetch_users_data()
        df_users = transform_users(raw_users)
        load_to_mssql(df_users, "users")
    except Exception as e:
        print(f"Users Pipeline Failed: {e}")

    # 3. Process Carts
    try:
        print("Fetching Carts...")
        raw_carts = fetch_carts_data()
        df_carts = transform_carts(raw_carts)
        load_to_mssql(df_carts, "carts", dtype={"date": DateTime()})
    except Exception as e:
        print(f"Carts Pipeline Failed: {e}")

    print("Pipeline Execution Finished!")


if __name__ == "__main__":
    run_pipeline()

#     print("Pipeline Execution Finished!")


# if __name__ == "__main__":
#     run_pipeline()
