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
    


menu_programa()