# this file represent the state of the database
import csv
from reader import Reader
from objects import *
from writer import Writer

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

        self.tables_info, _ = Reader.read_table('tables')
        self.columns, _ = Reader.read_table('columns')
        self.table_names = set()
        for key in self.tables_info:
            self.table_names.add(self.tables_info[key][1])

        """
        In self.tables will be all the tables in the database

        self.tables[table_name] returns a table with that table_name
        """
        self.tables = {}

        for _,info_row in self.tables_info.items():
            # get columns tuples
            # TODO do some checks
            columns = []
            for _,col_row in self.columns.items():
                if col_row[0] == info_row[1]:
                    columns.append((col_row[2],col_row[1]))
            print(columns)
            print(info_row)
            if info_row[2] == 'table':
                self.tables[info_row[1]] = Table(info_row[1],columns)
            elif info_row[2] == 'view':
                self.tables[info_row[1]] = View(info_row[1],columns)
            else:
                raise Exception('Invalid table object type')


    def __shutdown__(self):
        print('state is goind to sleep...')
        print('write back to disk all tables')

        for _,t in self.tables.items():
            Writer.back_to_disk(t)
        
        print('Done')
            
if __name__ == '__main__':
    st = State.get_instance()
    print(st.tables_info)
    print(st.tables['testtable2'])
    print('#######')
    print(st.columns)
    st.__shutdown__()