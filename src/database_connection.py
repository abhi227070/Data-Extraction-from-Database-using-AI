import os
from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase

def database_connection():
    load_dotenv()
    db = SQLDatabase.from_uri(f"mysql+pymysql://{os.environ['db_user']}:{os.environ['db_password']}@{os.environ['db_host']}/{os.environ['db_database']}",sample_rows_in_table_info = 3)
    return db