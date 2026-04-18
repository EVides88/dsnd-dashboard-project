from sqlite3 import connect
from pathlib import Path
from functools import wraps
import pandas as pd

# Using pathlib, create a `db_path` variable
# that points to the absolute path for the `employee_events.db` file
#### YOUR CODE HERE

import sqlite3
from pathlib import Path
from functools import wraps

db_path = Path(__file__).resolve().parent / "employee_events.db"

def execute_sql(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        query = func(*args, **kwargs)

        cursor.execute(query)
        results = cursor.fetchall()

        conn.close()

        return results

    return wrapper

# OPTION 1: MIXIN
# Define a class called `QueryMixin`
class QueryMixin:
    
    pass
    
    # Define a method named `pandas_query`
    # that receives an sql query as a string
    # and returns the query's result
    # as a pandas dataframe
    #### YOUR CODE HERE

    # Define a method named `query`
    # that receives an sql_query as a string
    # and returns the query's result as
    # a list of tuples. (You will need
    # to use an sqlite3 cursor)
    #### YOUR CODE HERE
    

 
 # Leave this code unchanged
def query(func):
    """
    Decorator that runs a standard sql execution
    and returns a list of tuples
    """

    @wraps(func)
    def run_query(*args, **kwargs):
        query_string = func(*args, **kwargs)
        connection = connect(db_path)
        cursor = connection.cursor()
        result = cursor.execute(query_string).fetchall()
        connection.close()
        return result
    
    return run_query
