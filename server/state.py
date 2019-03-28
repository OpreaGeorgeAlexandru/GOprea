# this file represent the state of the database
import csv

class State:

    def __init__(self):
        # every table has a table_name as a primary key in the self.tables hash
        self.tables = {}
