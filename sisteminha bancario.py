import json
from getpass import getpass

dados = "usuario"
senha = "pkmplus1009"
with open("titulares.json","r") as f:
    titulares = json.loads(f.read())
with open("contas.json","r") as f:
    contas = json.loads(f.read())
prox_ids = {"titulares":3,"contas":1003}
def usuario(titulares,contas):
    cpf = input("qual o seu cpf: ")
    senha = input("qual sua senha: ")
    for titular in contas:
        if titulares[contas[titular]["id_titular"]]["cpf"] == cpf:
            if titulares[contas[titular]["id_titular"]]["senha"] == senha:
                conta = titular
                titular = contas[titular]["id_titular"]
                return titular,conta
    return None
def adm(senha):
    if getpass("senha: ",echo_char="*") == senha:
        dados = "adm"
        return dados
def adicionar_titular(titulares,prox_ids):
    nome = input("nome: ")
    cpf = input("cpf: ")
    senha = getpass("senha: ",echo_char="*")
    titulares[prox_ids["titulares"]] = {"nome":nome,"cpf":cpf,"senha":senha,"status":"ativo"}
    prox_ids["titulares"] = prox_ids["titulares"] + 1
    with open("ids.json","w") as f:
        f.write(json.dumps(prox_ids,indent=4))
    return titulares,prox_ids
def mostrar_titulares(titulares,item):
    print(f"nome: {titulares[item]["nome"]}\ncpf: {titulares[item]["cpf"]}\nstatus: {titulares[item]["status"]}\n")
def adicionar_conta(contas,prox_ids):
    saldo = input("saldo: ")
    contas[prox_ids["contas"]] = {"id":prox_ids["titulares"],"saldo":saldo,"status":"ativo"}
    prox_ids["contas"] = prox_ids["contas"] + 1
    with open("ids.json","w") as f:
        f.write(json.dumps(prox_ids,indent=4))
def mostrar_contas(contas,titulares,item):
    id_titular = contas[item]["id_titular"]
    print(f"id_titular: {id_titular}\nnome do titular: {titulares[id_titular]["nome"]}\ncpf do titular: {titulares[id_titular]["cpf"]}\nsaldo: {contas[item]["saldo"]}\nstatus da conta: {contas[item]["status"]}")
def depositar(contas,id):
    valor = float(input("quanto sera depositado: "))
    if contas[id]["status"] == "ativa" and valor > 0:
        contas[id]["saldo"] += valor
        print(f"R${valor} foram depositados na conta {id}")
def sacar(contas,id):
    valor = float(input("quanto sera sacado: "))
    if contas[id]["status"] == "ativa" and valor > 0 and contas[id]["saldo"] >= valor:
        contas[id]["saldo"] -= valor
        print(f"R${valor} foram sacados da conta {id}")
def transferir(contas,id1):
    id2 = input("qual o id da conta de destino: ")
    valor = int(input("qual valor sera transferido: "))
    if contas[id1]["status"] == "ativo" and contas[id2]["status"] == "ativo" and valor > 0 and contas[id2]["saldo"] >= valor:
        contas[id1]["saldo"] -= valor
        contas[id2]["saldo"] += valor
        print(f"R${valor} foram transferidos da conta {id1} para a {id2}")
def relatorios(dicionario,status):
    for item in dicionario:
        if dicionario[item]["status"] == status:
            print(item)
def travar(dicionario):
    id = input(f"id: ")
    dicionario[id]["status"] = "bloqueado"
def destravar(dicionario):
    id = input(f"id: ")
    dicionario[id]["status"] = "ativo"
while True:
    funçao = input("voce e um (u)suario ou um (a)dmin: ")
    if funçao in ["u","usuario"]:
        titular,conta = usuario(titulares,contas)
        break
    elif funçao in ["a","admin"]:
        dados = adm(senha)
        break
while True:
    solicitaçao1 = input("o que deseja olhar,(t)itulares,(c)ontas,(o)peraçoes,(r)elatorios ou (s)air: ")
    if solicitaçao1 in ["s","sair"]:
        break
    elif solicitaçao1 in ["t","titulares"]:
        solicitaçao2 = input("voce deseja (c)adastrar,(b)uscar,(e)xibir,(t)ravar ou (d)estravar titulares: ")
        if solicitaçao2 in ["c","cadastrar"]:
            if dados == "adm":
                titulares,prox_ids = adicionar_titular(titulares,prox_ids)
                print("titular adicionado")
            else:
                print("é preciso uma permissao de adm para isso.")
        elif solicitaçao2 in ["e","exibir"]:
            if dados == "adm":
                for item in titulares:
                    mostrar_titulares(titulares,item)
            else:
                    mostrar_titulares(titulares,titular)
        elif solicitaçao2 in ["b","buscar"]:
            if dados == "adm":
                id = int(input("qual o id da pessoa procurada: "))
                mostrar_titulares(titulares,id)
            else:
                mostrar_titulares(titulares,titular)
        elif solicitaçao2 in ["t","travar"]:
            if dados == "adm":
                travar(titulares)
            else:
                print("é preciso uma permissao de adm para isso.")
        elif solicitaçao2 in ["d","destravar"]:
            if dados == "adm":
                destravar(titulares)
            else:
                print("é preciso uma permissao de adm para isso.")
    elif solicitaçao1 in ["c","contas"]:
        solicitaçao2 = input("voce deseja (c)adastrar,(b)uscar,(e)xibir,(t)ravar ou (d)estravar contas: ")
        if solicitaçao2 in ["c","cadastrar"]:
            if dados == "adm":
                contas,prox_ids = adicionar_conta(contas,prox_ids)
                print("conta adicionada")
            else:
                print("é preciso uma permissao de adm para isso.")
        elif solicitaçao2 in ["e","exibir"]:
            if dados == "adm":
                print(contas)
                for item in contas:
                    mostrar_contas(contas,titulares,item)
            else:
                        mostrar_contas(contas,titulares,conta)
        elif solicitaçao2 in ["b","buscar"]:
            if dados == "adm":
                id = input("qual o id da conta procurada: ")
                mostrar_contas(contas,titulares,id)
            else:
                mostrar_contas(contas,titulares,conta)
        elif solicitaçao2 in ["t","travar"]:
            if dados == "adm":
                travar(contas)
            else:
                print("é preciso uma permissao de adm para isso.")
        elif solicitaçao2 in ["d","destravar"]:
            if dados == "adm":
                destravar(contas)
            else:
                print("é preciso uma permissao de adm para isso.")
    elif solicitaçao1 in ["o","operaçoes"]:
        solicitaçao2 = input("voce deseja (d)epositar,(s)acar ou (t)ransferir: ")
        if solicitaçao2 in ["d","depositar"]:
            if dados == "adm":
                id = int(input("qual o id da conta do deposito: "))
                depositar(contas,id)
            else:
                depositar(contas,conta)
        elif solicitaçao2 in ["s","saque"]:
            if dados == "adm":
                id = input("qual o id da conta do saque: ")
                sacar(contas,id)
            else:
                sacar(contas,conta)
        elif solicitaçao2 in ["t","transferir"]:
            if dados == "adm":
                id1 = input("qual o id da conta de origem: ")
                transferir(contas,id1)
            else:
                transferir(contas,conta)
    elif solicitaçao1 in ["r","relatorios"]:
        if dados == "adm":
            solicitaçao2 = input("voce deseja ver as(c)ontas(a)tivas,(c)ontas(b)loqueadas,(t)itulares(a)tivos ou (t)itulares(b)loqueados: ")
            if solicitaçao2 in ["ca","contas ativas"]:
                relatorios(contas,"ativa")
            elif solicitaçao2 in ["cb","contas bloqueadas"]:
                relatorios(contas,"bloqueado")
            elif solicitaçao2 in ["ta","titulares ativos"]:
                relatorios(titulares,"ativo")
            elif solicitaçao2 in ["tb","titulares bloqueados"]:
                relatorios(titulares,"bloqueado")
    else:
        print("ação inexistente,tente novamente")
    with open("titulares.json","w") as f:
      f.write(json.dumps(titulares,indent=4))
    with open("contas.json","w") as f:
      f.write(json.dumps(contas,indent=4))