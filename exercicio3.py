categoria = input("Digite a categoria do cliente (comum, vip, parceiro): ")
valor = float(input("Digite o valor da compra: "))

if categoria == "vip":
    desconto = 0.15
elif categoria == "parceiro":
    desconto = 0.10
else:
    desconto = 0.05
valor_final = valor - (valor * desconto)
print(f"Desconto aplicado: {desconto*100:.0f}%")
print(f"Total a pagar com desconto: R${valor_final:.2f}")
               