#jogo papel pedra tesoura(com contagem, jo-ken-po)
#teremos dois usuários
#usuário p1 e p2

#usuario p1 pede pedra, papel ou tesoura

#usuario p2 é a máquina onde a escolha é aleatória

#jo...
#ken...
#po...

#mostra o resultado dos dois usuários
#mostra quem venceu

import time
import random

def jokenpo():
    resultado = []
    p1 = []
    p2 = []

    pd = "pedra"
    pp = "papel"
    ts = "tesoura"
    while True:
        x = input("digite a sua escolha, \n (1) Pedra, (2) Papel, (3) Tesoura \n:")
        if x == "1":
            break
        elif x == "2":
            break
        elif x == "3":
            break
        else:
            print("Por favor, digitar somente os números indicados na tela")
            time.sleep(2)
            continue
    x = int(x)
    y = random.randrange(1,4)
    if y == 1:
        p2.append(pd)
    elif y == 2:
        p2.append(pp)
    elif y == 3:
        p2.append(ts)

    if x == y:
        resultado.append("empate")
        if x == 1:
            p1.append(pd)
        elif x == 2:
            p1.append(pp)
        elif x == 3:
            p1.append(ts)
    elif x == 1 and y == 2:
        resultado.append("Que pena, você perdeu ;-;")
        if x == 1:
            p1.append(pd)
        elif x == 2:
            p1.append(pp)
        elif x == 3:
            p1.append(ts)
    elif x == 1 and y == 3:
        resultado.append("Meus parabéns, você Venceu! ^^")
        if x == 1:
            p1.append(pd)
        elif x == 2:
            p1.append(pp)
        elif x == 3:
            p1.append(ts)
    elif x == 2 and y == 1:
        resultado.append("Meus parabéns, você Venceu! ^^")
        if x == 1:
            p1.append(pd)
        elif x == 2:
            p1.append(pp)
        elif x == 3:
            p1.append(ts)
    elif x == 2 and y == 3:
        resultado.append("Que pena, você perdeu ;-;")
        if x == 1:
            p1.append(pd)
        elif x == 2:
            p1.append(pp)
        elif x == 3:
            p1.append(ts)
    elif x == 3 and y == 1:
        resultado.append("Que pena, você perdeu ;-;")
        if x == 1:
            p1.append(pd)
        elif x == 2:
            p1.append(pp)
        elif x == 3:
            p1.append(ts)
    elif x == 3 and y == 2:
        resultado.append("Meus parabéns, você Venceu! ^^")
        if x == 1:
            p1.append(pd)
        elif x == 2:
            p1.append(pp)
        elif x == 3:
            p1.append(ts)
    print("foi feito as escolhas")
    time.sleep(1)
    print("JO.....")
    time.sleep(1)
    print("..KEN..")
    time.sleep(1)
    print(".....PÔ")
    time.sleep(2)
    print("A maquina escolheu {}!!" .format(p2))
    time.sleep(2)
    print("voce escolheu {}" .format(p1))
    time.sleep(2)
    print("O resultado é..")
    time.sleep(2)
    print("...")
    time.sleep(2)
    print(resultado)
    print(p1, "x", p2)

    while True:
        play_again = input("Jogar novamente? (sim/S) ou (não/N)? \n:")
        play_again = play_again.upper()
        print(play_again)
        if play_again == "S" or play_again == "SIM":
            jokenpo()
        elif play_again == "N" or play_again == "NAO":
            print("ok, saindo...")
            time.sleep(2)
            print("...")
            break
        else:
            print("Por favot, digitar somente os valores pedidos!!!")
            time.sleep(1)
            continue

while True: #caso o usuário digite um valor inválido, ele se repete
    print("*"*33)
    print("*******Bem vindo ao JoKenPô******")
    print("*"*33)
    play = input("Deseja Jogar? (sim/S) ou (não/N)? \n:")
    play= play.upper()
    print(play)
    if play == "S" or play == "SIM":
        jokenpo()
    elif play == "N" or play == "NAO":
        print("ok, saindo...")
        time.sleep(2)
        print("...")
        break
    else:
        print("Por favrt, digitar somente os valores pedidos!!!")
        time.sleep(1)
        continue