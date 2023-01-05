from functools import partial


class Foo:
    def __init__(self):
        self.public = 'isso é protegido -> PROTEGIDO'
        self._protected = 'Isso é protegido ->  OUTRO PROTEGIDO '
        self.__exemplo = 'isso é private -> PRIVADO'

    def metodo_publico(self):
        # self._metodo_protected()
        # print(self._exemplo)
        self._modo_private()
        return 'metodo_publico'

    def _metodo_protected(self):
        print('metodo._protected')
        return '_metodo_protected'

    def _modo_private(self):
        print('_metodo_private')
        return '_metodo_private'


f = Foo()
# print(f.public)
print(f.metodo_publico())

