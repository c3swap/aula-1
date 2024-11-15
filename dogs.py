nome_cachorro = input("Qual o nome do teu dog fi?:\n")
idade_cachorro = int(input("Qual a idade do teu dog?:\n"))
calculo_idade = idade_cachorro*7
porte_pet = int(input("Qual o porte do teu pet? \n 1:pequeno \n 2:médio \n 3:grande \n: "))
quantia_banhos = int(input("Quantas vezes, em média, seu dog banha a cada 12 meses?: "))

if porte_pet == 1 :
    porte_P = float(50-5)*quantia_banhos
    print(f"eai, {nome_cachorro} tem {calculo_idade} anos e nos ultimos meses, os lucros nos ultimos 12 meses foram {porte_P}. ")
    
elif porte_pet == 2:
    porte_M = float(60-15)*quantia_banhos
    print(f"eai, {nome_cachorro} tem {calculo_idade} anos e nos ultimos meses, os lucros nos ultimos 12 meses foram {porte_M}. ")
    
elif porte_pet == 3 :
    porte_G = float(75-20)*quantia_banhos
    print(f"eai, {nome_cachorro} tem {calculo_idade} anos e nos ultimos meses, os lucros nos ultimos 12 meses foram {porte_G}. ")

else:
    print("tu é burro ao ponto de errar 3 numeros?")