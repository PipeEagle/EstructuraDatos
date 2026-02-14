nota = float (input("Ingrese la nota del estudiante: "))

# Evaluar la nota y mostrar el resultado con condicionales (IF, ELIF, ELSE)

if nota < 5:
    print("El estudiante ha reprobado.")
elif nota >= 5 and nota < 7:
    print("El estudiante ha aprobado con una nota regular.")
elif nota >= 7 and nota < 9:
    print("El estudiante ha aprobado con una nota buena.")
elif nota >= 9 and nota <= 10:
    print("El estudiante ha aprobado con una nota excelente.")
else:
    print("La nota ingresada no es válida.") 
    
#Bucles con WHILE

contador = 10

while contador > 0:
    print("El contador es: ", contador)
    contador -= 1 
    
# For con range

for i in [0, 1, 2, 3, 4]:
    print("El valor de i es: ", i)  

#










