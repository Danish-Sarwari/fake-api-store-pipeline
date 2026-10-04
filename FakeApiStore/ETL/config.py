import os
from pathlib import Path
from urllib.parse import quote_plus
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Use an absolute path based on this file's location instead of a relative
# path, so it works no matter what directory the script is run from.
ENV_PATH = Path(__file__).resolve().parent.parent / ".env"
# override=True is required because Windows already defines a system
# environment variable called USERNAME (the logged-in OS user, e.g. "Danish").
# Without override=True, load_dotenv() silently keeps that OS value instead
# of the "sa" value from .env, causing SQL Server login to fail.
load_dotenv(dotenv_path=ENV_PATH, override=True)

# API Base URL
BASE_URL = "https://fakestoreapi.com"

# SQL Server Configuration
server = os.getenv("DB_SERVER")
database = os.getenv("DB_DATABASE")
username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")

# Fail loudly and clearly if any value is missing, instead of letting a
# None flow into quote_plus() later and raise a confusing TypeError.
_missing = [
    name for name, val in
    [("DB_SERVER", server), ("DB_DATABASE", database), ("DB_USERNAME", username), ("DB_PASSWORD", password)]
    if not val
]
if _missing:
    raise RuntimeError(
        f"Missing environment variable(s): {', '.join(_missing)}. "
        f"Check that {ENV_PATH} exists and is formatted as KEY=value (no quotes, no spaces around '=')."
    )

# FIX: raw spaces in "ODBC Driver 17 for SQL Server" are not valid inside a
# URL query string and can break parsing (or truncate the driver name).
# quote_plus() safely encodes the username, password, and driver name so
# special characters (spaces, @, :, /, %) never corrupt the connection URL.
driver = quote_plus("ODBC Driver 17 for SQL Server")

CONNECTION_STRING = (
    f"mssql+pyodbc://{quote_plus(username)}:{quote_plus(password)}"
    f"@{server}/{database}?driver={driver}"
)


def get_db_engine():
    """It Returns SQL Server Engine Instance"""

    return create_engine(CONNECTION_STRING)


# import os
# from pathlib import Path
# from urllib.parse import quote_plus
# from dotenv import load_dotenv
# from sqlalchemy import create_engine

# # 1. Dynamic Absolute Path Best Practice (Relative Path '../.env' bypass)
# ENV_PATH = Path(__file__).resolve().parent.parent / ".env"
# load_dotenv(dotenv_path=ENV_PATH)

# # API Base URL
# BASE_URL = "https://fakestoreapi.com"

# # 2. String Fallback Fix: None value protection (os.getenv return None avoid karne ke liye)
# server = os.getenv("SERVER", "localhost")
# database = os.getenv("DATABASE", "FakeStoreDB")
# username = os.getenv("USERNAME", "")
# password = os.getenv("PASSWORD", "")

# # 3. Safe String Encoding Fix (None-safe quote_plus)
# safe_user = quote_plus(str(username)) if username else ""
# safe_pass = quote_plus(str(password)) if password else ""
# driver = quote_plus("ODBC Driver 17 for SQL Server")

# # SQL Connection String
# CONNECTION_STRING = (
#     f"mssql+pyodbc://{safe_user}:{safe_pass}@{server}/{database}?driver={driver}"
# )


# def get_db_engine():
#     """It Returns SQL Server Engine Instance"""
#     # Debug trace print to verify loaded details
#     if not username or not password:
#         print("⚠️ Warning: Username or Password not loaded properly from .env!")

#     return create_engine(CONNECTION_STRING)



# # import os
# # from pathlib import Path
# # from urllib.parse import quote_plus
# # from sqlalchemy import create_engine
# # from dotenv import load_dotenv

# # # Use an absolute path based on this file's location instead of a relative
# # # path, so it works no matter what directory the script is run from.
# # # ENV_PATH = Path(__file__).resolve().parent.parent / ".env"
# # ENV_PATH = "../.env"
# # load_dotenv(dotenv_path=ENV_PATH)

# # # API Base URL
# # BASE_URL = "https://fakestoreapi.com"

# # # SQL Server Configuration
# # server = os.getenv("SERVER")
# # database = os.getenv("DATABASE")
# # username = os.getenv("USERNAME")
# # password = os.getenv("PASSWORD")

# # # FIX: raw spaces in "ODBC Driver 17 for SQL Server" are not valid inside a
# # # URL query string and can break parsing (or truncate the driver name).
# # # quote_plus() safely encodes the username, password, and driver name so
# # # special characters (spaces, @, :, /, %) never corrupt the connection URL.
# # driver = quote_plus("ODBC Driver 17 for SQL Server")

# # CONNECTION_STRING = (
# #     f"mssql+pyodbc://{quote_plus(username)}:{quote_plus(password)}"
# #     f"@{server}/{database}?driver={driver}"
# # )


# # def get_db_engine():
# #     """It Returns SQL Server Engine Instance"""

# #     return create_engine(CONNECTION_STRING)