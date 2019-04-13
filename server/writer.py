# writer class

import csv
from objects import Table
from validator import Validator
import os

class Writer:

    def __init__(self):
        self.delimiter = ','


    """
    Write on this and in the memory a new table
    """
    @staticmethod
    def new_table(table_name,columns):
        Validator.name(table_name)
        Validator.columns(columns)
        
        from state import State
        state = State.get_instance()

        # TODO decoment this
        #if os.path.exists('goprea\\' + table.table_name + ".goprea"):
        #    raise SystemError('the table ' + table.table_name + ' already exists')
       
        with open('goprea\\' + table_name + ".goprea",'w+') as gf:
            gf.write(Table(table_name,columns,load_table=False).to_goprea())
        
        # add the table in the tables hash
        state.tables[table_name] = Table(table_name,columns,load_table=False)

        # add the table in the tables.csv
        state.tables_info[len(state.tables_info)+1] = ['defaultDB',table_name,'table']

        # add the table columns in columns
        for tup in columns:
            state.columns[len(state.columns)+1] = [table_name,tup[1],tup[0]]
        
    """
    Write back to disk the table
    """
    @staticmethod
    def back_to_disk(table : Table):
        with open('data\\' + table.table_name + ".csv",'w+') as csv_file:
            fieldnames = []
            for t in table.columns:
                fieldnames.append(t[1])

            csv_writer = csv.writer(csv_file,delimiter = ',')
            csv_writer.writerow(fieldnames)

            for _,row in table.content.items():
                print(row)
                if row != []:
                    csv_writer.writerow(row)
            



            