class Data:

    def __init__(self, dia, mes, ano):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    def formatada(self):
        print(f'Sua Data é {self.__dia}/{self.__mes}/{self.__ano}')

    #print("Sua Data é {}/{}/{}".format(self.__dia,self.__mes,self.__ano))
