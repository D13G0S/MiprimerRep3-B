#Autor: Diego Hernández Sánchez
# 1. Inicio
# 2. Definir resultado, entrada, num1, num2 
#3 . Imprimir "Que operación quieres hacer?"
print ("Que operación quieres hacer?")
#4 . entrada = entrada de usuario
entrada= input ()
# 5 . Imprimir "Dame el primer numero"
print ("dame el primer numero")
# 6 . num1 = entrada de ususario 
num1= float(input())
# 7 . Imprimir "Dame el segundo numero"
print ("dame el segundo numero")
# 8 . num2 = entrada de ususario
num2= float (input())
# 9. Si entrada = "suma" entonces, 
resultado = 0
if entrada == "suma":
resultado = num1 + num2 # 9.1 resultado = num1 + num2
elif: operación == "resta": #antes: else:
  resultado = num1 - num2 #9.2. de lo contrario, resultado = num1 - num2
# 10. Imprimir "el resultado de" entrada "es " resultado
print ("El resultado de la", operación, "es",resultado)
#11 Fin