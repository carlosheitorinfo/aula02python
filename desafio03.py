#Simulador de Caixa Eletrônico
#Peça um valor de saque. Use while para calcular quantas cédulas de 100, 50, 20 e 10 reais são necessárias. 
# Exiba o detalhamento do saque.(Exemplo: “2 notas de 100, 1 nota de 50, 1 nota de 20…")

valor = int(input('Qual valor você quer sacar? R$ '))
notas = [100, 50, 20, 10]
quantidade = []

i = 0
while valor > 0:
    if valor >= notas[i]:
        valor -= notas[i]
        quantidade.append(notas[i])
    else:
        i += 1

print("Detalhamento do saque:")
for nota in set(quantidade):
    print(f"{quantidade.count(nota)} notas de R$ {nota}")
