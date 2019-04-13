from validator import Validator
from config import Config

"""
Get the column type of a column
"""
def get_column_type(column_name):
    Validator.name(column_name)
    
    t = column_name.split('_')[-1]

    if t not in Config.column_types:
        # not a column type
        return 'nat'
    return t

if __name__ == '__main__':
    print(get_column_type("subject_pid"))
    print(get_column_type("subject_id"))
    print(get_column_type("subject__id_asd_fid"))
    print(get_column_type("subject_pid_asd_uid"))