
class Conta:


    def __init__(self,numero,titular,saldo,limite):
        print("Construido objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite


    def extrato(self):
        print("Saldo {} do Titular {}".format(self.__saldo,self.__titular))

    def depositar(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return  valor_a_sacar <= valor_disponivel_a_sacar


    def sacar(self, extrair):
        self.valordesaque = self.__limite + self.__saldo
        if(self.__pode_sacar(extrair)):
            self.__saldo -= extrair
        else:
            print(f"O valor {extrair} ultrapassou seu limite ")
            print(f"seu Limite de saque é de {self.valordesaque} ")
            return self.extrato()

    def transferir(self,valor,destino):
        self.sacar(valor)
        destino.depositar(valor)

    @property
    def get_saldo(self):
        return self.__saldo

    @property
    def get_titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "0001"

    @staticmethod
    def codigos_bancos():
        return {'BB': "0001", 'Caixa': '104', 'Bradesco': "237"}







