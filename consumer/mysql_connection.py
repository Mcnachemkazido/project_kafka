import pymysql
import os
from dotenv import load_dotenv
load_dotenv()


SQL_HOST=os.getenv("TEST_SQL_HOST")
SQL_USER=os.getenv("TEST_SQL_USER")
SQL_PASS=os.getenv("TEST_SQL_PASS")


connection = pymysql.connect(
     host= SQL_HOST,
     user= SQL_USER,
     password= SQL_PASS)



