total = 0
for i in range(1,8):
    tmp = float(input(f"Digite a temperatura do dia {i} : "))
total += i
dias = 7
media = total / dias 
talta = max(tmp)
tbaixa = min(tmp)
print(f"A média das temperaturas foi de: {media:.2f}")
print(f": {talta}")
print(f": {tbaixa}")




