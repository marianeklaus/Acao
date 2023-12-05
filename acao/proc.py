#Instanciando o objeto

class Acao:
    def __init__(self, emissor, codigo_b3):
        self.emissor = emissor
        self.codigo_b3 = codigo_b3
    def __str__(self):
        return f"""Este é um objeto da classe Ação e o emissor da ação é 
        {self.emissor} e o código é {self.codigo_b3}"""
    def negociar(self):
        print("Médoto negociar () Não implementado")
        NotImplemented