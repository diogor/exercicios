eleitores = {
    "total": 1000,
    "validos": 800,
    "brancos": 150,
    "nulos": 50,
}


class Percentuais:
    def __init__(self, eleitores):
        self.eleitores = eleitores

    def votos_validos(self):
        return (self.eleitores["validos"] / self.eleitores["total"]) * 100

    def votos_brancos(self):
        return (self.eleitores["brancos"] / self.eleitores["total"]) * 100

    def votos_nulos(self):
        return (self.eleitores["nulos"] / self.eleitores["total"]) * 100


if __name__ == "__main__":
    percentuais = Percentuais(eleitores)
    print(f"Percentual de votos válidos: {percentuais.votos_validos():.2f}%")
    print(f"Percentual de votos brancos: {percentuais.votos_brancos():.2f}%")
    print(f"Percentual de votos nulos: {percentuais.votos_nulos():.2f}%")
