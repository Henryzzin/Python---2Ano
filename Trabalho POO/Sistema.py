import datetime
import time

class Funcionario:
    # Construtor
    def __init__(self, _nome, _cargo, _salario, _cpf, _data_contratacao, _id): 
        self.nome = _nome
        self.cargo = _cargo
        self.salario = _salario
        self.cpf = _cpf
        self.data_contratacao = _data_contratacao
        self.id = _id


    #Gets e Sets
    def setNomeFunc(self, _nome): 
        self.nome = _nome
    
    def getNomeFunc(self):
        return self.nome

    def setIDFunc(self, _id): 
        self.id = _id
    
    def getIDFunc(self):
        return self.id
    
    def setCargoFunc(self, _cargo):
        self.cargo = _cargo

    def getCargoFunc(self):
        return self.cargo

    def setSalarioFunc(self, _salario):
        self.salario = _salario

    def getSalarioFunc(self):
        return self.salario

    def setCPF(self, _cpf):
        self.cpf = _cpf

    def getCPF(self):
        return self.cpf
    
    def setDataContratacao(self, _data_contratacao): # Talvez tenha editar 
        self.data_contratacao = _data_contratacao
    
    def getDataContratacao(self):
        return self.data_contratacao
    


class System ():
       

    # Criar funcionario e adicionar informações
    def criarFuncionario(lista_funcionarios, _id):
        print("Digite as informações necessárias:")
        _nome = input("Nome: ")
        _cargo = input("Cargo: ")
        _salario = float(input("Salario: "))
        _cpf = input("CPF: ")
        id = _id 
        ano_contratacao = int(input("Digite o ano de contratação: ")) 
        mes_contratacao = int(input("Digite o mês de contratação: "))
        dia_contratacao = int(input("Digite o dia de contratação: "))
        _data_contratacao = datetime.datetime(ano_contratacao, mes_contratacao, dia_contratacao)

        
        lista_funcionarios.append(Funcionario(_nome, _cargo, _salario, _cpf, _data_contratacao, id) )
        

    # Não sei como fazer
    def listarFuncionarios(lista_funcionarios):
        print("\nLista de FUNCIONÁRIOS: \n")
        for i in range (0, len(lista_funcionarios)):
            time.sleep(1.5)
            print(lista_funcionarios[i].nome)
            time.sleep(0.5) 
            print("   ID:", lista_funcionarios[i].id)
            time.sleep(0.5)  
            print("   Cargo:", lista_funcionarios[i].cargo)
            time.sleep(0.5)  
            print("   Salário:", lista_funcionarios[i].salario)
            time.sleep(0.5)  
            print("   CPF:", lista_funcionarios[i].cpf)
            time.sleep(0.5)  
            print("   Data da Contratação:", lista_funcionarios[i].data_contratacao)
            time.sleep(0.5)  

    def atualizarFuncionario(lista_funcionarios):
        System.listarFuncionarios(lista_funcionarios)
        escolherNome = input("Digite o nome do funcionário que deseja atualizar: ")
        escolherID = input("Digite o id do funcionário que deseja atualizar: ")
        for i in range (0, len(lista_funcionarios)):
            if(escolherID == lista_funcionarios[i].id):
                time.sleep(1.5)
                print("Qual informação você deseja atualizar?")
                print("1. Nome")
                print("2. Cargo")
                print("3. Salário")
                print("4. CPF")
                print("5. Data de Contratação")
                print("6. Cancelar Atualização")
                print("----------------------------------------------------")

                _opcao = int(input("Digite o numero correspondente à ação que deseja fazer: "))
                time.sleep(0.75)
                match _opcao:
                        case 1:
                            _nome = input("Digite o nome atualizado do funcionario: ")
                            lista_funcionarios[i].setNomeFunc(_nome)
                            time.sleep(0.5)  
                        case 2:
                            _cargo = input("Digite o cargo atualizado do funcionario: ")
                            lista_funcionarios[i].setCargoFunc(_cargo)
                            time.sleep(0.5)  
                        case 3:
                            _salario = int(input("Digite o salario atualizado do funcionario: "))
                            lista_funcionarios[i].setSalarioFunc(_salario)
                            time.sleep(0.5)  
                        case 4:
                            _cpf = input("Digite o CPF atualizado do funcionario:")
                            lista_funcionarios[i].setCPF(_cpf)
                            time.sleep(0.5)  
                        case 5:
                            ano_contratacao = int(input("Digite o ano de contratação: "))
                            mes_contratacao = int(input("Digite o mes de contratação: "))
                            dia_contratacao = int(input("Digite o dia de contratação: "))
                            _data_contratacao = datetime.datetime(ano_contratacao, mes_contratacao, dia_contratacao)
                            lista_funcionarios[i].setDataContratacao(_data_contratacao)
                            time.sleep(0.5)  
                        case 6:
                            print("Saindo")

                        case _:
                            print("O numero digitado não corresponde as opções acima, digite novamente")
                            time.sleep(0.75)
                            System.atualizarFuncionario(lista_funcionarios)
            else:
                print("O nome digitado não existe.")
                time.sleep(0.75)
                
    
    def deletarFuncionario(lista_funcionarios):
        nomeID = input("Digite o ID do funcionário que deseja deletar: ")
        for i in range (0, len(lista_funcionarios)):
            if(nomeID == lista_funcionarios[i].id):
                del lista_funcionarios[i]
                time.sleep(0.75)
                


    
    