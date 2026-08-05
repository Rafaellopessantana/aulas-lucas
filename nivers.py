from datetime import date,datetime
import json
aniversarios = {}
today = date.today()
while True:
  escolha = input("o que deseja fazer hoje??\n1-cadastrar pessoa\n2-buscar pessoa\n3-remover pessoa\n4-exibir lista completa\n5-exibir lista do dia\n6-exibir lista do mes\n7-salvar agenda\n8-carregar agenda\n0-encerrar\n")
  if escolha == "0":
    break
  elif escolha == "1":
    pessoa = input("qual o nome da pessoa: ")
    nascimento = input(f"qual a data de nascimento de {pessoa}: ")
    aniversarios[pessoa] = nascimento
    print("pessoa cadastrada com sucesso")
  elif escolha == "2":
    pessoa = input("qual o nome da pessoa que voce deseja ver: ")
    for i in aniversarios:
      if pessoa in i:
        print(print(f"{i}: {aniversarios[i]}"))
  elif escolha == "3":
    pessoa = input("qual o nome da pessoa que voce deseja remover: ")
    del aniversarios[pessoa]
    print("pessoa removida com sucesso")
  elif escolha == "4":
    print(aniversarios)
  elif escolha == "5":
    for pessoa in aniversarios:
      data = datetime.strptime(aniversarios[pessoa],"%d/%m/%Y")
      if data.day == today.day and data.month == today.month:
        print(f"{pessoa}: {aniversarios[pessoa]}")
  elif escolha == "6":
    for pessoa in aniversarios:
      data = datetime.strptime(aniversarios[pessoa],"%d/%m/%Y")
      if data.month == today.month:
        print(f"{pessoa}: {aniversarios[pessoa]}")
  elif escolha == "7":
    with open("agenda.json","w") as f:
      f.write(json.dumps(aniversarios,indent=4))
    print("agenda salva, use a opção 8 para carrega-la apos o uso.")
  elif escolha == "8":
    with open("agenda.json","r") as f:
      aniversarios = json.loads(f.read())
  else:
    print(f"erro 515: {escolha} não é uma das opções.")