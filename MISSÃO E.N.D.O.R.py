import time,subprocess,random

def fala(fala,falante):
    palavra = ""
    for l in fala:
        subprocess.run("cls", shell=True)
        print(falante + ":")
        print(palavra + "_")
        palavra = palavra + l
        time.sleep(0.1)
    subprocess.run("cls", shell=True)
    print(falante + ":")
    print(palavra)
    palavra = palavra + l
fala("MISSÃO E.N.D.O.R.","")
if input("aperte enter para iniciar") != "":
    fala("oi curioso,eu sou que nem você,mas não tem nada aqui para você,agora tchau  ","Rafael Lopes(o dev)")
veiculos = {"at-at":{"combustivel":95,"integridade":100,"suprimentos":100,"velocidade":15,"gasto necessario":5},"at-st":{"combustivel":75,"integridade":55,"suprimentos":35,"velocidade":35,"gasto necessario":5},"speeder bike":{"combustivel":40,"integridade":15,"suprimentos":15,"velocidade":95,"gasto necessario":5},"a pe":{"combustivel":12,"integridade":10,"suprimentos":6,"velocidade":12,"gasto necessario":5}}
fala("Scout Trooper, memorize os parâmetros da sua operação.\nO AT-AT é uma fortaleza móvel — quase impenetrável, mas extremamente lento.\nO AT-ST oferece equilíbrio entre mobilidade e poder de fogo.\nA Speeder Bike é velocidade pura, ideal para reconhecimento, porém frágil.\nE a pé, você depende de discrição e resistência, com baixa capacidade de combate direto.\n\nCada opção define não apenas sua mobilidade, mas também sua sobrevivência.\nQual veículo você escolhe para esta missão?","Darth Vader")
while True:
    veiculo = input("")
    if veiculo not in veiculos:
        fala("bem,não acho que temos esse tipo de veiculo por aqui,se importaria em escolher outro?","Darth Vader")
    else:
        break
status = veiculos[veiculo]
sequencia = {"sem dormir":0,"seguidos andando":0,"sem comer":0}
fala("MISSÃO INICIADA,BOA SORTE","Alto Falante")
distancia = random.randint(200,1000)
dia = 0
while distancia > 0:
    dia += 1
    fala(str(dia),"Sistema do Veiculo")
    dist = "o objetivo esta a " + str(distancia) + " quilometros"
    fala(dist,"Sistema do Veiculo")
    fala(str(status),"Sistema do Veiculo")
    açao = input("o que deseja fazer:\n1-seguir em frente\n2-procurar suprimentos\n3-reparar a nave\n4-descansar\n5-comer\n6-procurar combustivel\n")
    if açao == "1":
        distancia -= status["velocidade"]
        status["combustivel"] -= status["gasto necessario"]
        sequencia["seguidos andando"] += 1
    elif açao == "2":
        perdido = False
        while True:
            fala("o que devo fazer agora: (p)rocurar mais recursos ou (s)air daqui","Você")
            sub_açao = input()
            if sub_açao == "p":
                status["suprimentos"] += (suprimentos := random.randint(0,5))
                suprimentos = "otimo,mais " + str(suprimentos)
                fala(suprimentos,"Você")
            elif sub_açao == "s":
                break
            if random.randint(1,8) == 1:
                print("☠️você morreu atacado por um grupo de ewoks☠️")
                break
            if random.randint(1,10) == 1:
                perdido = True
        if perdido:
            print("☠️você morreu perdido na floresta☠️")
            break
    elif açao == "3":
        gasto = int(input("quanto de dano deseja reparar"))
        status["suprimentos"] -= gasto
        status["integridade"] += gasto
        sequencia["seguidos andando"] = 0    
    elif açao == "4":
        print("o grupo parou para descansar")
        sequencia["sem dormir"] = -1
        sequencia["seguidos andando"] = 0
    elif açao == "5":
        status["suprimentos"] -= 5
        sequencia["sem comer"] = -1
        sequencia["seguidos andando"] = 0
        if random.randint(1,25) == 1:
            print("☠️você morreu envenenado☠️")
            break  
    elif açao == "6":
        fala("quanto combustivel sera que eu pego?","Você")
        combustivel = int(input())
        if random.randint(1,101) <= combustivel:
            status["integridade"] -= combustivel / 1.5
        status["combustivel"] += combustivel
    sequencia["sem comer"] += 1
    sequencia["sem dormir"] += 1
    if sequencia["sem comer"] >= 4:
        print("☠️você morreu de fome☠️")
        break
    if sequencia["sem dormir"] >= 3:
        print("☠️você morreu de sono☠️")
        break
    if status["combustivel"] <= 0:
        if veiculo == "a pe":
            print("☠️você morreu por falta de energia☠️")
            break
        else:
            print("💢seu veiculo ficou sem combustivel,agora continue a pe essa missão💢")
            veiculo = "a pe"
            status = veiculos[veiculo]

    if status["integridade"] <= 0:
        if veiculo == "a pe":
            print("☠️você morreu por danos serios☠️")
            break
        else:
            print("💢seu veiculo foi destruido,agora continue a pe essa missao💢")
            veiculo = "a pe"
            status = veiculos[veiculo]
    if status["suprimentos"] <= 0:
        print("☠️você morreu por falta de suprimentos o suficiente para comer☠️")
        break
    if status["suprimentos"] > veiculos[veiculo]["suprimentos"]:
        status["suprimentos"] = veiculos[veiculo]["suprimentos"]
    if status["combustivel"] > veiculos[veiculo]["combustivel"]:
        status["combustivel"] = veiculos[veiculo]["combustivel"]
    if status["integridade"] > veiculos[veiculo]["integridade"]:
        status["integridade"] = veiculos[veiculo]["integridade"]
else:
    fala("Scout Trooper,\nSua missão foi um sucesso. Não importa se você utilizou um AT-AT, um AT-ST, uma Speeder Bike ou foi a pé: você cumpriu seu dever para com o Império.\nDevo admitir que estou impressionado por você ter retornado vivo. As chances não estavam ao seu favor.\nConsidere isso um reconhecimento do seu desempenho.\nPrepare-se. Sua próxima missão pode ser ainda mais difícil.\n\nPelo Império.","Darth Vader")
    print("🏅voce ganhou🏅")
time.sleep(10)