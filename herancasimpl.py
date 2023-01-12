class Pessoa:
    cpf = '1234'

    def __init__(self, nome, sobrenome) -> None:
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print('classe PESSOA')
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Cliente(Pessoa):
    def falar_nome_classe(self):
        print('não sai da classe cliente')
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Aluno(Pessoa):
    cpf = 'cpf aluno: 42607564867'


client1 = Cliente('Marcus', 'Vinicius')
client1.falar_nome_classe()
aluno = Aluno('Marcus', 'Vinicius')
aluno.falar_nome_classe()
print(aluno.cpf)
