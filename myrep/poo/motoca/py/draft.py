class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.__nome: str = nome
        self.__idade: int = idade

    def getNome(self):
        return self.__nome
    
    def setNome(self, value):
        self.__nome = value

    def getIdade(self):   
        return self.__idade
    
    def setIdade(self, value):
        self.__idade = value

    def show(self) -> None:
        print(self)

    def __str__(self):
        return f"{self.getNome()}:{self.getIdade()}"
    
class Moto:
    def __init__(self, potencia: int):
        self.__potencia: int = potencia
        self.__passageiro: Pessoa | None = None
        self.__tempo: int = 0

    def getPotencia(self):
        return self.__potencia
    
    def getPassageiro(self):
        return self.__passageiro
    
    def getTempo(self):
        return self.__tempo
    
    def inserir(self, passageiro: Pessoa) -> bool:
        if self.__passageiro != None:
            print("fail: busy motorcycle")
            return False
        else:
            self.__passageiro = passageiro
            return True
        
    def buy(self, min: int):
        self.__tempo += min

    def honk(self):
        return "P" + "e" *self.__potencia + "m"
    
    def drive(self, min: int):
        if self.__tempo <= 0:
            print("fail: buy time first")
            return
        if self.__passageiro == None:
            print("fail: empty motorcycle")
            return
        if self.__passageiro.getIdade() > 10:
            print("fail: too old to drive")
            return #era pra ter alguma coisa aq?
        if min > self.__tempo:
            print(f"fail: time finished after {self.__tempo} minutes")
            self.__tempo = 0
            return
        self.__tempo -= min

    def remover(self) -> Pessoa | None:
        if self.__passageiro == None:
            print("fail: empty motorcycle")
            return None
        aux = self.__passageiro
        self.__passageiro = None
        return aux
    
    def show(self) -> None:
        print(self)

    def __str__(self):
        passageiro = f"({self.__passageiro})" if self.__passageiro != None else "(empty)"
        return f"power:{self.getPotencia()}, time:{self.getTempo()}, person:{passageiro}"

        #passageiro = f"({self.__passageiro})"
        #if self.__passageiro != None else "(empty)"
            #return f"power:{self.getPotencia()}, time:{self.getTempo()}, person:{passageiro}"
        
def main():
    motoca = Moto(1)

    while True:
        line = input()
        print("$" + line)
        caixinha = line.split(" ")

        if caixinha[0] == "end":
            break
        if caixinha[0] == "init":
            potencia = int(caixinha[1])
            motoca = Moto(potencia)
        elif caixinha[0] == "show":
            print(motoca)
        elif caixinha[0] == "enter":
            nome = caixinha[1]
            idade = int(caixinha[2])
            pessoa = Pessoa(nome, idade)
            motoca.inserir(pessoa)
        elif caixinha[0] == "leave":
            pessoa = motoca.remover()
            if pessoa != None:
                print(pessoa)
        elif caixinha [0] ==  "buy":
            min = int(caixinha[1])
            motoca.buy(min)
        elif caixinha[0] == "drive":
            min = int(caixinha[1])
            motoca.drive(min)
        elif caixinha[0] == "honk":
            print(motoca.honk())
        
        

    
    
main()
            

        