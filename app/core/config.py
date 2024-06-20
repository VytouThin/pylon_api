# import os
# from dotenv import load_dotenv
# from sqlalchemy.engine.url import URL

# # Load environment variables from .env file
# load_dotenv()

# DATABASE = {
#     'drivername': 'mssql+pyodbc',
#     'username': os.getenv('DATABASE_USERNAME'),
#     'password': os.getenv('DATABASE_PASSWORD'),
#     'host': os.getenv('DATABASE_HOST'),
#     'port': os.getenv('DATABASE_PORT'),
#     'database': os.getenv('DATABASE_NAME'),
#     'query': {
#         'driver': 'ODBC Driver 17 for SQL Server'
#     }
# }


# DATABASE_URL = f"mssql+pyodbc://{os.getenv('DATABASE_USERNAME')}:{os.getenv('DATABASE_PASSWORD')}@{os.getenv('DATABASE_HOST')}/{os.getenv('DATABASE_NAME')}?driver=ODBC Driver 17 for SQL Server"

# # DATABASE_URL = str(URL(**DATABASE))

# print(DATABASE_URL)  # Optional: Print the DATABASE_URL to verify
