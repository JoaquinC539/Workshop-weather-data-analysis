
## Son operaciones de if y else en una linea de codigo o en lamb

# x=a>16?true:false

mayor16 = lambda edad:True if(edad>16) else False


# mayor50_menor25=lambda edad: True if (edad > 50) or (edad < 25) else False
mayor50_menor25=lambda edad:  True if (edad > 50) else True if(edad < 25) else False

print(mayor50_menor25(51))
print(mayor50_menor25(100))
print(mayor50_menor25(23))
print(mayor50_menor25(32))

a=19
b=58

miValor="Yo soy mayor" if(a>b) else "No soy Mayor"
print(miValor)
