class Alunos():
    def __init__(self, nome, *notas):
        self.nome = nome
        self.notas = list(notas) 


    def calcular_media(self):
        if self.notas:
            media = sum(self.notas) / len(self.notas)
            return media
    
    def resultado(self):
        if self.calcular_media() >= 7:
            resultado = "Aprovado"
        else:
            resultado = "Reprovado"
        return resultado

def menu_programa():
    Menu = {
        1: "Adicionar Aluno",
        2: "Listar Alunos",
        3:  "Atualizar Notas",
        4:  "Remover Aluno",
        5:  "Sair"
    }
    for keys, info in Menu.items():
        print(f"{keys} - {info}")        

def adicionar_aluno():
    nome = input("Digite seu nome: ")
    notas = list(map(float, input("Digite suas notas separadas por espaço: ").split()))
    aluno = Alunos(nome, *notas)

def listar_alunos():
    pass

def atualizar_notas():
    pass

def remover_aluno():
    pass


def programa():
    while True:
        try:
            menu_programa()
            escolha = input("Escolha uma opção: ")
            escolher = int(escolha)
            match escolher:
                case 1:
                    adicionar_aluno()
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    pass
                case _:
                    print("Opção inválida, tente novamente.")
                    continue
        except ValueError:
            print("Opção não válida, tente novamente.")
            continue


