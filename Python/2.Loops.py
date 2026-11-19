print("Estructuras repetitivas")

# 1. Bucle For con range
print("\n--- Bucle For (range) ---")
for i in range(1, 11):
    print(f'Numero {i}')

# 2. Bucle For recorriendo un string
print("\n--- Bucle For (string) ---")
for letra in "Hola mundo":
    print(letra)

# 3. Bucle While
print("\n--- Bucle While ---")
contador = 1
while contador <= 3:
    print(f'Intento {contador}')
    contador += 1