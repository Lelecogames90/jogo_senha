# Jogo da Advinha
# Explicar como funciona o jogo
# fazer o Usuário (Aquele(a) Arrombado(a)) perguntar o valor (De 0 a 9) de cada fileira
# Quando o usuário completar cada fileira, ela será prescrita
# Cada fileira deve ter uma variável que vai ser alterada cada rodada
# O número dito pelo jogador caso acerte ou erre o número da fileira, o programa dirá
# Caso tenha dúvida, não conte comigo

'''
f1 = Fileira 1
f2 = Fileria 2
f3 = Fileria 3
f4 = Fileira 4
j = Jogo
lj = Listad do Jogador
'''
print("============ Jogo da Senha ============")
x = input("Você tem alguma dúvida? ")
print("Não ligo, se vira aí!")
print("")
print("")
print("")
f1 = str("3")
f2 = str("4")
f3 = str("2")
f4 = str("9")
j = str([f1, f2, f3, f4])
lj = []
F1 = input("Primeiro dígito: ")
lj = [F1]
print(lj)
print("=====================")
print(j)
print("")
F2 = input("Segundo digito: ")
lj = [F1, F2]
print(lj)
print("=====================")
print(j)
print("")
F3 = input("Terceiro digito: ")
lj = [F1, F2, F3]
print(lj)
print("=====================")
print(j)
print("")
F4 = input("Quarto digito: ")
lj = [F1, F2, F3, F4]
print(lj)
print("=====================")
print(j)
print("")
if lj == j :
    print("Meus parabéns, de primeira!")
else :
    while lj != j :
        print("")
        print("")
        F1 = input("Digite novamente o primeiro digito: ")
        lj.insert(0, F1)
        F2 = input("Digite novamente o segundo digito: ")
        lj.insert(1, F2)
        F3 = input("Digite novamente o terceiro digito: ")
        lj.insert(2, F3)
        F4 = input("Digite novamente o quarto digito: ")
        lj.insert(3, F4)
print("Fim de jogo, você acertou! ")
print("=======================================")
