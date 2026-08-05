import time,subprocess
palavra = ""
for l in "hello\n world":
    subprocess.run("cls", shell=True)
    palavra = palavra + l
    print(palavra)
    time.sleep(0.5)