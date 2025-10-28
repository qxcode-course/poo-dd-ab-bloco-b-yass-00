class Pessoa:
    def __init__(self, nome: str, dinheiro: int):
        self.__nome = nome
        self.__dinheiro = dinheiro 

    def getNome(self):
        return self.__nome
    
    def getDinheiro(self):
        return self.__dinheiro
    
    def setNome(self, nome: str):
        self.__nome = nome
    
    def setDinheiro(self, dinheiro: int):
        self.__dinheiro = dinheiro 

    def pagar(self, valor: int):
        self.__dinheiro -= valor 
    
    def receber(self, valor: int):
        self.__dinheiro += valor 
    
    def __str__(self):
        return f"{self.getNome()}:{self.getDinheiro()}"
    
class Moto:
    def __init__(self):
        self.__motorista: Pessoa | None = None
        self.__passageiro: Pessoa | None = None
        self.__custo: int = 0

    def getMotorista(self):
        return self.__motorista 
    
    def getPassageiro(self):
        return self.__passageiro
    
    def getCusto(self):
        return self.__custo 
    
    def subirMotorista(self, motorista: Pessoa):
        if self.__motorista != None:
            print("fail: ja tem motorista na moto")
        else:
            self.__motorista = motorista 

    def subirPassageiro(self, passageiro: Pessoa):
        if self.__passageiro != None:
            print("fail: ja tem passageiro na moto")
        else:
            self.__passageiro = passageiro
        
    def rodando(self, km: int):
        if self.getMotorista() == None:
            print("fail: nao ha motorista na moto")
            return
        if self.getPassageiro() == None:
            print("fail: nao ha passageiro na moto")
            return
        
        self.__custo += km

    def saltar(self):
        if self.getPassageiro().getDinheiro() < self.getCusto():
            print("fail: Passenger does not have enough money")
            self.getPassageiro().pagar(self.getCusto())
            self.getMotorista().receber(self.getCusto())
            self.getPassageiro().setDinheiro(0)
            print(f"{self.getPassageiro()} left")
            self.__passageiro = None
            self.__custo = 0
        else:
            self.getPassageiro().pagar(self.getCusto())
            self.getMotorista().receber(self.getCusto())
            print(f"{self.getPassageiro()} left")
            self.__passageiro = None
            self.__custo = 0

    
    def __str__(self):
        return f"Cost: {self.__custo}, Driver: {self.__motorista}, Passenger: {self.__passageiro}"
    

def main():
    motouber = Moto()

    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(motouber)
        elif args[0] == "setDriver":
            nome = args[1]
            dinheiro = int(args[2])
            motorista = Pessoa(nome, dinheiro)
            motouber.subirMotorista(motorista)
        elif args[0] == "setPass":
            nomep = args[1]
            dinheirop = int(args[2])
            passageiro = Pessoa(nomep, dinheirop)
            motouber.subirPassageiro(passageiro)
        elif args[0] == "leavePass":
            motouber.saltar()
        elif args[0] == "drive":
            km = int(args[1])
            motouber.rodando(km)
main()