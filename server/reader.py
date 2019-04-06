import csv
from validator import Validator
import helpers

class Reader:
    """
    Every table is dictonary

    Function that read a csv table and return a dict that represents that table
    """
    @staticmethod
    def read_table(table_name):
        Validator.name(table_name)
        table = {}
        with open('data\\' + table_name + '.csv', 'r') as csvFile:
            reader = csv.reader(csvFile)
            # get every column_name in the header and find primary key 
            pid = -1
            for i,row in enumerate(reader):
                if i == 0:
                    for j,e in enumerate(row):
                        if helpers.get_column_type(e) == 'pid':
                            pid = j
                            break
                print(row)
                if pid == -1:
                    table[i] = row
                else:
                    table[row[pid]] = row
        csvFile.close()
        
        return table

if __name__ == '__main__':
    print(Reader.read_table('tables'))
    print(Reader.read_table('columns'))
    