
# Clase Banco
# atributos: cuentas:list[Cuentas]
# class abstracta  #

# Clase Cuenta (Banco)

# nombre, id, cunato dinero
# self.list.append(cuenta)

#list:cuenta=>[]
#self.append(cuenta)
#list:cuenta=>[cuenta.list:cuenta=>[[]]
#self.append(cuenta)=>[[[]],[[]]


#class Banco
#atributos: cuentas:list[Cuentas]  


#crear Banco
#crear cuenta
#Banco.append(cuenta)  



class CuentaBanco:

    def __init__(self, name:str, balance:int=0, id:str = None) -> None:
        self.name = name
        self.balance = balance
        self.id = id

    def check_balance(self) -> str:
        return f'Current Balance: {self.balance}'

    def deposit(self, amount)->None:
        self.balance += amount
    
    def withdraw(self, amount) -> None:
        if amount > self.balance:
            return 'Insufficient Funds'
        self.balance - amount
    
    

#Accion | Output

#Alice tiene $ 1000

#Alice checa su dinero : $1000

#Alice deposita $200

#Alice retira $800

#Alice checa su dinero: $400


##########################################








