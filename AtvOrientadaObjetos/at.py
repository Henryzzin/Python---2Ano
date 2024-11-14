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
    def __init__(self, idade, nome, cpf, endereco, sexo):
        super().__init__(idade, nome, cpf, endereco, sexo)
        self.esposa=None
        self.filhos=[]

    def resumo(self):
        print("Nome: ", self.nome)
        print("Idade: ", self.idade)
        print("CPF: ", self.cpf)
        print("Endereço: ", self.endereco)
        print("Sexo: ", self.sexo)

    def adicionarEsposa(self, esposa):
        self.esposa=esposa
    def adicionarFilhos(self, filhos):
        self.filhos=filhos

class Mae(Pessoa):
    def __init__(self, idade, nome, cpf, endereco, sexo):
        super().__init__(idade, nome, cpf, endereco, sexo)
        self.esposa=None
        self.filhos=[]

    def resumo(self):
        print("Nome: ", self.nome)
        print("Idade: ", self.idade)
        print("CPF: ", self.cpf)
        print("Endereço: ", self.endereco)
        print("Sexo: ", self.sexo)

    def adicionarEsposo(self, pai):
        self.pai=pai
    def adicionarFilhos(self, filhos):
        self.filhos=filhos

class Filhos(Pessoa):
    def __init__(self, idade, nome, cpf, endereco, sexo):
        super().__init__(idade, nome, cpf, endereco, sexo)
        self.esposo=None
        self.esposa=None

    def resumo(self):
        print("Nome: ", self.nome)
        print("Idade: ", self.idade)
        print("CPF: ", self.cpf)
        print("Endereço: ", self.endereco)
        print("Sexo: ", self.sexo)

    def adicionarPaiMae(self, esposo, esposa):
        self.pai=esposo
        self.mae=esposa

filho=Filhos(18, 'João', '091.142.719-82', 'Rua Marga', 'Masculino')
esposo=Pai(44, 'Eduardo', '253.302.196-54', 'Rua Antonieta', 'Masculino')
esposa=Mae(54, 'Sofia', '381.313.924-31', 'Rua Antonieta', 'Feminino')

Pai.adicionarEsposa(esposa)
Pai.adicionarFilhos(filho)
Mae.adicionarFilhos(filho)
Mae.adicionarEsposo(esposo)
Filhos.adicionarPaiMae(esposo, esposa)
