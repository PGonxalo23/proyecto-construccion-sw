print("=== CALCULADORA ===")

numero1 = float(input("Ingresa el primer número: "))
operador = input("Ingresa la operación (+, -, *, /): ")
numero2 = float(input("Ingresa el segundo número: "))

if operador == "+":
    resultado = numero1 + numero2

elif operador == "-":
    resultado = numero1 - numero2

elif operador == "*":
    resultado = numero1 * numero2

elif operador == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        resultado = "No se puede dividir entre cero"

else:
    resultado = "Operación no válida"

print("Resultado:", resultado)
