# this file represent the state of the database
import csv
from reader import Reader

"""
The state of the database

This class is a singleton
"""
class State:
    __instance = None

    @staticmethod
    def get_instance():
        if State.__instance == None:
            State()
        return State.__instance

    def __init__(self):
        # every table has a table_name as a primary key in the self.tables_info hash
        if State.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            State.__instance = self

        self.tables_info = Reader.read_table('tables')
        self.columns = Reader.read_table('columns')
        self.table_names = set()
        for key in self.tables_info:
            self.table_names.add(self.tables_info[key][1])

        """
        In self.tables will be all the tables in the database

        self.tables[table_name] returns a table with that table_name
        """



if __name__ == '__main__':
    st = State.get_instance()
    print(st.tables_info)
    print(st.table_names)