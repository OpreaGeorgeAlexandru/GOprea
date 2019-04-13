from config import Config

class Validator:

    # a command must be a list of strings
    @staticmethod
    def command(com):
        if not isinstance(com,list):
            raise TypeError('A command should be a list of strings')
        for word in com:
            if not isinstance(word,str):
                raise TypeError('A command should be a list of strings')

    @staticmethod
    def name(nm):
        if not isinstance(nm,str):
            raise TypeError('A name should be a string: ' + nm)
        if nm[0] < 'a' or nm[0] > 'z':
            raise NameError('A name should start with a letter: ' + nm)
        # check for banned symbols
        items = Config.items() + Config.banned_symbols
        for c in nm:
            if c in items:
                raise NameError('A name should not contain a banned symbol, operator or delimiter')

    @staticmethod
    def columns(col):
        if not isinstance(col,list):
            raise SyntaxError('Column should be a list of tuples')
        for t in col:
            if not isinstance(t,tuple):
                raise SyntaxError('Column element should be a tuple')
            if t[0] not in Config.types:
                raise SyntaxError('Column element should a pair of [type] [name]')
            Validator.name(t[1])
    
    @staticmethod
    def table(tb):
        Validator.name(tb.table_name)
        Validator.columns(tb.columns)


