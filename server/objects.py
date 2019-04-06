# file with DB object types
from validator import Validator
import abc

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

class Table(Gopreable):

    def __init__(self,table_name,columns,content = {}):
        Validator.name(table_name)
        Validator.columns(columns)
        self.table_name = table_name
        self.columns = columns
        self.content = content

    def get_content(self):
        return self.content

    def to_goprea(self):
        query = "create table " + self.table_name + " ( "
        
        for t in self.columns:
            query += t[0] + " " + t[1] + ", "

        query = query[:-2] + " )"

        return query
