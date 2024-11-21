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
        super().resumo()
        
        print(f"{self.esposa.nome} é a mulher de {self.nome}" if self.esposa else f"{self.nome} não tem esposa")
        print(f"{self.nome} tem {len(self.filhos)} filhos")
        print(f"Seus filhos se chamam: {[filho.nome for filho in self.filhos]}") 


    def adicionarFilhos(self, filho):
        if isinstance(filho, Filho):
            self.filhos.append(filho)
        else: 
            print("O objeto fornecido não é uma instância da classe Filho.")

class Mae(Pessoa):
    def __init__(self, idade, nome, cpf, endereco, sexo):
        super().__init__(idade, nome, cpf, endereco, sexo)
        self.esposa=None
        self.filhos=[]

    def resumo(self):
        super().resumo()
        print(f"{self.esposo.nome} é o marido de {self.nome}" if self.esposo else f"{self.nome} não tem esposo")
        print(f"{self.nome} tem {len(self.filhos)} filhos")
        print(f"Seus filhos se chamam: {[filho.nome for filho in self.filhos]}") 


    def adicionarFilhos(self, filho):
        if isinstance(filho, Filho):
            self.filhos.append(filho)
        else: 
            print("O objeto fornecido não é uma instância da classe Filho.")

class Filho(Pessoa):
    def __init__(self, idade, nome, cpf, endereco, sexo):
        super().__init__(idade, nome, cpf, endereco, sexo)
        self.pai=None
        self.mae=None

    def resumo(self):
        super().resumo()
        print(f"{self.pai.nome} é pai de {self.nome}" if self.pai else f"{self.nome} não tem pai definido")
        print(f"{self.mae.nome} é mãe de {self.nome}" if self.mae else f"{self.nome} não tem mãe definida") 

    def adicionarPaiMae(self, pai, mae):
        if isinstance(pai, Pai) and isinstance(mae, Mae):
            self.pai=pai
            self.mae=mae
            pai.adicionarFilhos(self)
            mae.adicionarFilhos(self)
        else:
            print("Os objetos fornecidos não são instâncias das classes Pai e Mae.") 

filho=Filho(18, 'João', '091.142.719-82', 'Rua Marga', 'Masculino')
esposo=Pai(44, 'Eduardo', '253.302.196-54', 'Rua Antonieta', 'Masculino')
esposa=Mae(54, 'Sofia', '381.313.924-31', 'Rua Antonieta', 'Feminino')

esposo.adicionarFilhos(filho)
esposa.adicionarFilhos(filho)
filho.adicionarPaiMae(esposo, esposa)
