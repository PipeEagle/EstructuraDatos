for i in range(10): 
    if i == 3: 
        break 
    print(i, end=" ")


nota = 75
if nota >= 90:
    print("Excelente")
elif nota >= 70:
    print("Bueno")
elif nota >= 50:
    print("Regular")
else:
    print("Insuficiente")
    
for i in range(6):
    if i % 2 == 0:
        continue
    print(i, end=" ")

for i in range(5):
    pass

a = (1, 2, 3) 
print(type(a), len(a))

x = 10
if x > 5:
    print("Mayor")
else:
    print("Menor")
    
resultado = "" 
for i in range(3):
    for j in range(2):
        resultado += str(i) + str(j) + " "
print(resultado) 

mi_dict = {"nombre": "Ana", "edad": 25} 
print(mi_dict["nombre"])

suma = 0
for i in range(1, 4):
    suma += i
print(suma)