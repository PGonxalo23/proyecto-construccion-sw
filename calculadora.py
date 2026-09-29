import random


def calcular():
	print("🦄 ¡La calculadora mágica! 🦄")
	print("Elige una operación: +, -, *, /")

	while True:
		operacion = input("Operación (o escribe 'salir'): ").strip().lower()
		if operacion == "salir":
			print("¡Hasta la próxima aventura! 🌈")
			break
		if operacion not in ("+", "-", "*", "/"):
			print("Esa magia no existe. Prueba +, -, * o /.")
			continue

		try:
			a = float(input("Primer número: "))
			b = float(input("Segundo número: "))
		except ValueError:
			print("¡Uy! Escribe números, por favor.")
			continue

		if operacion == "+":
			resultado = a + b
		elif operacion == "-":
			resultado = a - b
		elif operacion == "*":
			resultado = a * b
		else:
			if b == 0:
				print("¡No podemos dividir entre cero! Intenta con otro número.")
				continue
			resultado = a / b

		felicitaciones = random.choice(("¡Genial!", "¡Eres un genio!", "¡Estupendo!"))
		print(f"{felicitaciones} El resultado es {resultado:g} ✨\n")


if __name__ == "__main__":
	calcular()
