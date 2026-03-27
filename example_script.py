# Los textos con un 'numeral' (#) al principio son comentarios. 
# Python los ignora, sirven para que los humanos entendamos el código.

# 1. Variables y Entrada de Datos (Input)
nombre = input("¿Cómo te llamas? ")
edad_texto = input("¿Cuántos años tienes? ")

# Convertimos el texto de la edad a un número entero 
edad = int(edad_texto)

# 2. Salida de Datos (Print)
print(f"\n¡Hola, {nombre}! Qué gusto conocerte.")

# 3. Lógica Condicional (If / Else)
if edad >= 18:
    print("Veo que eres mayor de edad.")
else:
    print("Veo que eres menor de edad.")