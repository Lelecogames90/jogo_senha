# Jogo da Advinha
# Explicar como funciona o jogo
# fazer o Usuário (Aquele(a) Arrombado(a)) perguntar o valor (De 0 a 9) de cada fileira
# Quando o usuário completar cada fileira, ela será prescrita
# Cada fileira deve ter uma variável que vai ser alterada cada rodada
# O número dito pelo jogador caso acerte ou erre o número da fileira, o programa dirá
# Caso tenha dúvida, não conte comigo

v = 0

a = "1"
b = "3"
c = "9"
d = "5"

j = [a, b, c, d]
lj = []

while j != lj :
    W = input("Primeiro número: ")
    lj = [W]
    X = input("Segundo número: ")
    lj = [W, X]
    Y = input("Terceiro número: ")
    lj = [W, X, Y]
    Z = input("Quarto número: ")
    lj = [W, X, Y, Z]

    print(lj)
    print("==========================")
    print(j)
    print("")
    v = 0
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
        print(f"Há {v} respostas certas")
