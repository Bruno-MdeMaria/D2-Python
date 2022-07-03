print("Olá, Seja bem vindo a calculadora de gorgeta!")
conta= float(input("Qual o total da conta? $"))
corg = int(input("Qual o percentuial de gogeta que gostaria de dar? 10, 12 ou 15?"))
pess = int(input("Com quantas pessoas vai dividir a conta?"))
fatura = (corg/100 * conta + conta)
total = round(fatura / pess, 2)
total_novo_formato = "{:.2f}".format(total)
print(f"Então cada pessoa deverá pagar: ${total_novo_formato}")



#conta_corg = round(int(corg)/100,2)* int(conta)+int(conta)
#print(conta_corg)
#result = round(conta_corg / int(pess) , 2)
#print(result)
##print(f"Então cada pessoa deverá pagar: ${round(result,2)}")