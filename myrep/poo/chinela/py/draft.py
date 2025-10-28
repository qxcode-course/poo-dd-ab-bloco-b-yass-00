class Chinela:
    def __init__(self):
        self.__tamanho = 0

    def getTamanho(self):
        return self.__tamanho
    
    def setTamanho(self, pezao: int):
        if pezao < 20 or pezao > 50 or pezao % 2 != 0:
            print("fail: uma prancha n um pe")
        else:
            self.__tamanho = pezao

    def show(self) -> None:
        print(self)

    def __str__(self):
        return (f"seu pezao e igual: {self.getTamanho()}")
    

def main():
    chinela = Chinela()

    while True:
        line = input()
        print("$" + line)
        caixinhas = line.split(" ")

        if caixinhas[0] == "end":
            break
        elif caixinhas[0] == "criar":
            pezao = int(caixinhas[1])
            chinela.setTamanho(pezao)
        elif caixinhas[0] == "show":
            print(chinela)

main()