age = input("What is your current age?")

print (age)
age_int = int(age)
meses = age_int * 12
print(meses)
semanas = age_int*52
print(semanas)
dias = age_int*365
print(dias)

maximo_m = 90*12
maximo_s = 90*52
maximo_d = 90*365

print('quantos falta:')
fm = maximo_m-meses
print(fm)
fs = maximo_s-semanas
print(fs)
fd = maximo_d-dias
print(fd)

print(f"You have {fd} days, {fs} weeks, and {fm} months left.")

##abaixo o código mazis limpo e a resolução feita pela prof:
age = input("What is your current age?")

idade = int(age)
f_a = 90 - idade
f_m = f_a*12
f_s = f_a*52
f_d = f_a*365

print(f"You have {f_d} days, {f_s} weeks, and {f_m} months left.")
