numero = int(input("Escolha um número para fazermos a multiplicação: "))

print("Aqui está sua multiplicação!")

for i in range(1,11):
  resultado = numero * i
  print(f"{numero} x {i} = {resultado}")