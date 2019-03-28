# this file will execute commands
from validator import Validator
from config import Config

class Executer:

    @staticmethod
    def create_table(table_name,columns, group_owner = Config.ANONIM_GROUP):
        Validator.name(table_name)
        Validator.columns(columns)

        # check if table_name already exists