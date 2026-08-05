import os,time

animacoes = {"fechar":["_/","_|","_\\","_"],"andar":["\n  _/","  _/","_/","\n_","\n_/"],"carinho":["💕\n🤛\n_/","💕\n 🤛\n_/"," 💕\n 🤛\n_/"," 💕\n🤛\n_/"]}
while True:
    animacao = input("insira o nome da animação que deseja tocar(digite parar para parar): ")
    if animacao == "parar":
        break
    for i in range(5):
        for n in range(len(animacoes[animacao])):
            print(animacoes[animacao][n])
            time.sleep(0.5)
            os.system("cls")