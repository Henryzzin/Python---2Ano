class Pessoa:
    def __init__(self, idade, nome, cpf, endereco, sexo):
        self.idade=idade
        self.nome=nome
        self.cpf=cpf
        self.endereco=endereco
        self.sexo=sexo

    def resumo(self):
        print("Nome: ", self.nome)
        print("Idade: ", self.idade)
        print("CPF: ", self.cpf)
        print("Endereco: ", self.endereco)
        print("Sexo: ", self.sexo)

class Pai(Pessoa): 
    def __init__(self, idade, nome, cpf, endereco, sexo, esposa, filhos):
        super().__init__(idade, nome, cpf, endereco, sexo)
        self.esposa=esposa
        self.filhos=filhos

    def resumo(self):
        print("Nome: ", self.nome)
        print("Idade: ", self.idade)
        print("CPF: ", self.cpf)
        print("Endereco: ", self.endereco)
        print("Sexo: ", self.sexo)

class Mae(Pessoa):
    def __init__(self, idade, nome, cpf, endereco, sexo, esposo, filhos):
        super().__init__(idade, nome, cpf, endereco, sexo)
        self.esposa=esposo
        self.filhos=filhos

    def resumo(self):
        print("Nome: ", self.nome)
        print("Idade: ", self.idade)
        print("CPF: ", self.cpf)
        print("Endereco: ", self.endereco)
        print("Sexo: ", self.sexo)

    def adicionarFilho(self, filhos):


class Filhos(Pessoa):
    def __init__(self, idade, nome, cpf, endereco, sexo, pai, mae):
        super().__init__(idade, nome, cpf, endereco, sexo)
        self.pai=pai
        self.mae=mae

    def resumo(self):
        print("Nome: ", self.nome)
        print("Idade: ", self.idade)
        print("CPF: ", self.cpf)
        print("Endereco: ", self.endereco)
        print("Sexo: ", self.sexo)

    filho=Filhos(18, 'João', '091.142.719-82', 'Rua Marga', 'Masculino', 'Jonas', 'Marta')
