# this file will execute commands
from validator import Validator
from config import Config
from state import State
from writer import Writer

class Executer:

    @staticmethod
    def create_table(table_name,columns, group_owner = Config.ANONIM_GROUP):
        Validator.name(table_name)
        Validator.columns(columns)

        # check if TABLE table_name already exists
        if table_name in State.get_instance().table_names:
            raise Exception("this table already exists")
        
        Writer.new_table(table_name,columns)


if __name__ == '__main__':
    pass
    state = State()
    print('state.tables= ' + str(state.tables))
    Executer.create_table('t1',[('int','t1_pid')])
    print('state.tables= ' + str(state.tables))
    state.__shutdown__()



