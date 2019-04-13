# file with DB object types
from validator import Validator
import abc
from reader import Reader

class Gopreable(abc.ABC):

    # returns a query string that can create the object 
    @abc.abstractmethod
    def to_goprea(self):
        pass

    """
    this method is usefull because a view has a dynamic content
    but a table has a static content
    a view at each call of this method will calculate the content
    """
    @abc.abstractmethod
    def get_content(self):
        pass

    """
    This function will load the tableobject
    """
    @abc.abstractmethod
    def load(self):
        pass

    @abc.abstractmethod
    def get_type(self):
        pass
"""
Abstract class that abstracts a table object like a view or a table
"""
class TableObject(Gopreable):
    def __init__(self,table_name : str, columns : list, pid=-1,content = {}):
        Validator.name(table_name)
        Validator.columns(columns)
        self.table_name = table_name
        self.columns = columns
        self.content = content
        self.pid = pid

    def get_content(self):
        pass

    def to_goprea(self):
        pass

    def load(self):
        pass

    def get_type(self):
        return "table_object"
    
    def __str__(self):
        return "name:" + str(self.table_name)+ "\ncolumns:" + str(self.columns) + "\ncontent:" + str(self.content)

class Table(TableObject):

    def __init__(self,table_name : str, columns : list, pid=-1, content = {},load_table = True):
        super(Table,self).__init__(table_name,columns,pid,content)
        if load_table:
            self.load()
    """
    load the table from the disk
    """
    def load_from_disk(self):
        self.content, self.pid = Reader.read_table(self.table_name)
    
    def load(self):
        if len(self.content) == 0:
            self.load_from_disk()

    def get_content(self):
        return self.content

    def to_goprea(self):
        query = "create table " + self.table_name + " ( "
        
        for t in self.columns:
            query += t[0] + " " + t[1] + ", "

        query = query[:-2] + " )"

        return query

    def get_type(self):
        return "table"

class View(TableObject):
    def __init__(self,table_name : str, columns : list, pid=-1, content = {}):
        super(View,self).__init__(table_name,columns,pid,content)
        self.load()


    """
    load view
    """
    def load(self):
        #raise NotImplementedError("TODO")
        pass

    def get_content(self):
        return self.content
    
    def get_type(self):
        return "view"

    def to_goprea(self):
        query = "create table " + self.table_name + " ( "
        
        for t in self.columns:
            query += t[0] + " " + t[1] + ", "

        query = query[:-2] + " )"

        return query


if __name__ == '__main__':
    t = Table('tables',[('int','col1')])
    t.load_from_disk()
    print(t)