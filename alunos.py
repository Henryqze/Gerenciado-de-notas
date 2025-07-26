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




