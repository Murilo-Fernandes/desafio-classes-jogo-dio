class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        if self.tipo == "mago":
            ataque = "magia"
        elif self.tipo == "guerreiro":
            ataque = "espada"
        elif self.tipo == "monge":
            ataque = "artes marciais"
        elif self.tipo == "ninja":
            ataque = "shuriken"
        else:
            ataque = "ataque desconhecido"

        print(f"O {self.tipo} atacou usando {ataque}.")

nome_heroi = input("Digite o nome do herói: ")
idade_heroi = int(input("Digite a idade do herói: "))
tipo_heroi = input("Digite o tipo do herói (mago, guerreiro, monge ou ninja): ")

heroi = Heroi(nome=nome_heroi, idade=idade_heroi, tipo=tipo_heroi)
heroi.atacar()
