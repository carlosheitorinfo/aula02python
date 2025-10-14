"""# Estruturas de repetição
for numero in range(1,6):
    print(f"Contagem:{numero}")


# Validação de senha
senha = ""
while senha != "python":
    senha = input("Digite a senha: ")
print("Acesso permitido")


# Contagem regressiva
import time
for segundos in range(5,0,-1):
    print(f"Inicio em {segundos}... ")
    time.sleep(1)
print("Começou!")


# Cálculo de média
total = 0
contador = 0
while True:
    numero = int(input("Digite um número (0 para sair): "))
    if numero == 0:
        break
    total += numero
    contador += 1
    if total != 0:
        media = total / contador 
        print(f"Soma total: {total}")
        print(f"Soma contador: {contador}")
        print(f"Média dos números: {media:.2f}")


# Tabuada personalizada
numero = int(input("Gerar tabuada de: "))
inicio  = int(input("Início: "))
fim = int(input("Fim: "))
for i in range(inicio, fim + 1):
    print(f"{numero} x {i} = {numero * i}")"""


# Validação de senha com limite de tentativas
tentativas = 3
senha_correta = "admin"
while tentativas > 0:
    senha = input("Digite a senha: ")
    if senha == senha_correta:
        print("Acesso permitido")
        break
    else:
        tentativas -= 1
        print(f"Senha incorreta. Restam {tentativas} tentativas.")
if tentativas == 0:
    print("Acesso bloqueado por tentativas excedidas.")





