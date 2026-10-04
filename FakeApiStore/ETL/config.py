import os
from pathlib import Path
from urllib.parse import quote_plus
from sqlalchemy import create_engine
from dotenv import load_dotenv

ENV_PATH = Path(__file__).resolve().parent.parent / ".env"

load_dotenv(dotenv_path=ENV_PATH, override=True)

# API Base URL
BASE_URL = "https://fakestoreapi.com"

# SQL Server Configuration
server = os.getenv("DB_SERVER")
database = os.getenv("DB_DATABASE")
username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")

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

driver = quote_plus("ODBC Driver 17 for SQL Server")

CONNECTION_STRING = (
    f"mssql+pyodbc://{quote_plus(username)}:{quote_plus(password)}"
    f"@{server}/{database}?driver={driver}"
)


def get_db_engine():
    """It Returns SQL Server Engine Instance"""

    return create_engine(CONNECTION_STRING)



# # def get_db_engine():
# #     """It Returns SQL Server Engine Instance"""

# #     return create_engine(CONNECTION_STRING)
