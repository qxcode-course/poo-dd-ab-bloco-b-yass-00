class Camisa:
    def __init__(self):
        self.__tamanho = ""

    def getTamanho(self) -> str:
        return self.__tamanho

    def setTamanho(self, tamain: str):
        t_val = ["PP", "P", "M", "G", "GG", "XG"]
        if tamain not in t_val:
            print("fail: Valor invalido, tente PP, P, M, G, GG ou XG")
        else:
            self.__tamanho = tamain

    def show(self) -> None:
        print(self)

    def __str__(self):
        return (f"size: ({self.getTamanho()})")

def main():
    camisa = Camisa()

    while True:
        line = input()
        print("$" + line)
        caixinhas = line.split(" ")

        if caixinhas[0] == "end":
            break
        elif caixinhas[0] == "size":
            tamain = caixinhas[1]
            camisa.setTamanho(tamain)
        elif caixinhas[0] == "show":
            print(camisa)
        


    


main()