# Pedro Barros 97937
# Vinícius Barros 97824
# Rodrigo Lima 98326
# Guilherme Monteiro 99499

import random
import re

# grupo de vendedores
group = ("Pedro", "Vinicius", "Rodrigo", "Guilherme")
wines = dict(
    opt1 = dict(name= "Vinho tinto suave", price=120.0, qtd=10),
    opt2 = dict(name= "Vinho tinto seco", price=140.0, qtd=7),
    opt3 = dict(name= "Vinho branco suave", price=200.0, qtd=16),
    opt4 = dict(name= "Vinho branco seco", price=210.0, qtd=11),
    opt5 = dict(name= "Vinho sem àlcool", price=100.0, qtd=0),
)
client = dict()

# main para inicializar o programa com as mensagens
def main():
    try:
        print("Bem vindo a vinheria Agnello.")
        sorted = group[sort()]
        print(f"O funcionário {sorted} vai acompanhá-lo nesta compra")
        print("-"*40)
        print("\nInforme o seu nome:")
        name = input()
        print("\nInforme o seu CEP:")
        zipCode = input()
        print("\nInforme o ano do seu nascimento")
        year = int(input())
        client.update({"name": name})
        client.update({"zipCode": zipCode})
        client.update({"year": year})
        client.update({"func": sorted})
        validate()
        products()
    except ValueError:
        print("Erro")
    finally:
        print("Programa encerrado")

# sorteando o funcionário
def sort():
    sorted = random.randint(0, 3)
    return sorted

# validando os dados
def validate():
    if re.search("\d{5}-\d{3}", client["zipCode"]):
        if re.search("\d", (client["name"])): 
            print("Seu nome não pode conter dígitos.")
            raise ValueError
        if re.search("\d{4}", str(client["year"])):
            if client["year"] > 2005:
                print("Você precisa ser maior de idade moleque!")
                raise ValueError
        else: 
            print("Seu ano de nascimento deve conter 4 dígitos. Seu velho!")
            raise ValueError
    else:
        print("Seu cep deve conter 5 dígitos, um traço e mais 3 dígitos.")
        raise ValueError
    
# atualizando o priduto
def products():
    print("-"*10, "Vinhos", "-"*10)
    for i in wines:
        if wines[i]["qtd"] > 0:
            print(f"{i}   {wines[i]['name']}  R$: {wines[i]['price']}  {wines[i]['qtd']}")
    print("\nEscolha as opções (opt1, opt2, opt3 ou op4):")
    opt = input()
    if opt != "opt1" and opt != "opt2" and opt != "opt3" and opt != "opt4":
        print("Opção inválida")
        raise ValueError
    print(f"Quantas garrafas você quer comprar do {wines[opt]['name']} ?")
    qtd = int(input())
    if qtd > wines[opt]["qtd"]:
        print("Não temos essa quantidade no estoque, seu cachaceiro!")
        raise ValueError
    client.update({"payment": dict(name = wines[opt]["name"], price = (wines[opt]["price"]*qtd), qtd = (qtd))})
    wines[opt]["qtd"] = wines[opt]["qtd"] - qtd
    print("\n")
    for i in wines:
        if wines[i]["qtd"] > 0:
            print(f"{i}   {wines[i]['name']}  R$: {wines[i]['price']}  {wines[i]['qtd']}")
    print("-"*40)
    print("Compra final:")
    print(f"{client['payment']['name']}  R$: {client['payment']['price']}  {client['payment']['qtd']}")
    print(f"Nome do cliente: {client['name']}")
    print("Obrigado por comprar com a Agnello")
    print("Favor transferir o valor para o pix do professor Gilberto. Chave: Astrogildo")
    

main()
