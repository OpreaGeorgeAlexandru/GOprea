# this file will execute commands
from validator import Validator
from config import Config
from state import State

class Executer:

    @staticmethod
    def create_table(table_name,columns, group_owner = Config.ANONIM_GROUP):
        Validator.name(table_name)
        Validator.columns(columns)

        # check if TABLE table_name already exists
        if table_name in State.get_instance().table_names:
            raise Exception("this table already exists")
        
        