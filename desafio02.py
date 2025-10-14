#Desafio 2 – Cálculo de Média de Temperaturas Semanais Peça as temperaturas de 7 dias usando for.Calcule e exiba:
#a média da semana
#a maior temperatura
#a menor temperatura

total = 0
tmp = []
for i in range(1,8):
    t = input(f"Digite a temperatura do dia {i} : ")
    tmp.append(float(t))
    total += float(t)
dias = 7
media = total / dias 
tmax= max(tmp)
tmin= min(tmp)

#media = sum(tmp) / len(tmp)

print (str(f"A média das temperaturas foi de: {media:.2f}"))
print (str(f"A temperatura mais alta foi: {tmax}"))
print (str(f"A temperatura mais baixa foi: {tmin}"))






