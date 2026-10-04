from .config import get_db_engine


def load_to_mssql(df, table_name, mode='replace', dtype=None):
    """
    Loads the DataFrame into an MS SQL Server table.
    Mode options: 'replace' or 'append'
    dtype: optional dict mapping column name -> SQLAlchemy type, to force
    explicit column types instead of relying on pandas' auto-inference
    (which can occasionally clash with reserved SQL Server type names).
    """

    engine = get_db_engine()

    df.to_sql(
        name=table_name,
        con=engine,
        if_exists=mode,
        index=False,
        dtype=dtype
    )

    print(f"Loaded {len(df)} records into table: '{table_name}'")



# from .config import get_db_engine


# def load_to_mssql(df, table_name, mode='replace'):
#     """
#     Loads the DataFrame into an MS SQL Server table.
#     Mode options: 'replace' or 'append'
#     """

#     engine = get_db_engine()

#     df.to_sql(
#         name=table_name,
#         con=engine,
#         if_exists=mode,
#         index=False
#     )

#     print(f"Loaded {len(df)} records into table: '{table_name}'")