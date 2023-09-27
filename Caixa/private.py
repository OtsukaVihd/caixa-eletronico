class Test:
    __variavel_static = 'variavel static'

    def __init__(self):
        self.__variavel = 'variavel'

    def __method(self):
        print('private method')

    @staticmethod
    def __static_method():
        print('private static method')