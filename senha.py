# Jogo da Advinha
# Explicar como funciona o jogo
# fazer o Usuário (Aquele(a) Arrombado(a)) perguntar o valor (De 0 a 9) de cada fileira
# Quando o usuário completar cada fileira, ela será prescrita
# Cada fileira deve ter uma variável que vai ser alterada cada rodada
# O número dito pelo jogador caso acerte ou erre o número da fileira, o programa dirá
# Caso tenha dúvida, não conte comigo
import random 
h = []
v = 0
a = random.randint(0,9)
b = random.randint(0,9)
c = random.randint(0,9)
d = random.randint(0,9)
j = [a, b, c, d]
lj = []
while j != lj :
    W = int(input("Primeiro número: "))
    lj = [W]
    X = int(input("Segundo número: "))
    lj = [W, X]
    Y = int(input("Terceiro número: "))
    lj = [W, X, Y]
    Z = int(input("Quarto número: "))
    lj = [W, X, Y, Z]
    print("")
    for i in j :
        if i == W :
            v = v + 1  
        else :
            if i == X :
                v = v + 1
            else :
                if i == Y :
                    v = v + 1
                else :
                    if i == Z :
                        v = v + 1
    if v == 1 :
        print(f"Há {v} resposta certa")
    elif v <= 0 :
        print(f"Não há nenhuma resposta certa")
    else :
        if v == 4 :
            print("Parabéns, Você ganhou!")
        else :
            print(f"Há {v} respostas certas")
    v = 0
    h.append(lj)
    print(f"Histórico = {h}")
