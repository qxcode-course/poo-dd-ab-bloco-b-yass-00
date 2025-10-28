class Grafite:
    def __init__(self, thickness: float, hardness: str, size: int):
        self.__thickness = thickness
        self.__hardness = hardness
        self.__size = size

    def getThickness(self):
        return self.__thickness
    
    def getHardness(self):
        return self.__hardness
    
    def getSize(self):
        return self.__size
    
    def setSize(self, valor: int):
        self.__size = valor

    def usagePerSheet(self):
        if self.__hardness == "HB":
            return 1
        if self.__hardness == "2B":
            return 2
        if self.__hardness == "4B":
            return 4
        if self.__hardness == "6B":
            return 6
    
    def __str__(self):
        return f"{self.getThickness():.1f}:{self.getHardness()}:{self.getSize()}"
    
class Lapiseira:
    def __init__(self, espessura: float):
        self.__espessura = espessura
        self.__grafite: Grafite| None = None

    def getGrafite(self):
        return self.__grafite
    
    def getEspessura(self):
        return self.__espessura
    
    def temGrafite(self) -> bool:
        return self.__grafite != None
                       
    def remover(self) -> Grafite | None:
        aux = self.__grafite
        self.__grafite = None
        return aux
    
    def escrever(self):
        if self.__grafite == None:
            print("fail: nao existe grafite")
            return
        if self.__grafite.getSize() <= 10:
            print("fail: tamanho insuficiente")
            return
        uso = self.__grafite.usagePerSheet()
        tamanhoFinal = self.__grafite.getSize() - uso 

        if tamanhoFinal < 10:
            print("fail: folha incompleta")
            self.__grafite.setSize(10)
            return
        self.__grafite.setSize(tamanhoFinal)
        
    def inserir(self, grafite: Grafite):
        if self.getEspessura() != grafite.getThickness():
            print("fail: calibre incompativel")
        elif self.temGrafite():
            print("fail: ja existe grafite")
        else:
            self.__grafite = grafite


        

    def __str__(self):
        grafite = ""
        if self.__grafite != None:
            grafite = f"[{self.__grafite}]"
        else:
            grafite = "null"
        return f"calibre: {self.getEspessura():.1f}, grafite: {grafite}"
    

def main():
    lapiseira = Lapiseira(0)

    while True:
        line = input()
        print("$" + line)
        caixinha = line.split(" ")

        if caixinha[0] == "end":
            break
        if caixinha[0] == "show":
            print(lapiseira)
        if caixinha[0] == "init":
            calibre = float(caixinha[1])
            lapiseira = Lapiseira(calibre)
        elif caixinha[0] == "insert":
            calibre_g = float(caixinha[1])
            espessura = caixinha[2]
            tam = int(caixinha[3])
            grafite = Grafite(calibre_g, espessura, tam)
            lapiseira.inserir(grafite)
        elif caixinha[0] == "remove":
            lapiseira.remover()
        elif caixinha[0] == "write":
            lapiseira.escrever()


main()


        



        
        
    
