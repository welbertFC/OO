def cria_conta(numero,titular,saldo,limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def deposita(conta, valor):
    conta["saldo"] += valor

def saca(conta, extrair):
    conta["saldo"] -= extrair

def extrato(conta):
    print("saldo é {}".format(conta["saldo"]))