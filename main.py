
# Função para determinar o momento no ponto A
def momento_em_A(dados):
    M_a = 0
    for F in dados:
        M_a += F[0]*F[1]
    return M_a

# Função para determinar a função resultante do sistema
def forca_resultante(dados):
    R = 0
    for F in dados:
        R += F[0]
    return R

# Função para determinar a distância Xc
def X_c(dados):
    M_a = momento_em_A(dados)
    R = forca_resultante(dados)
    xc = M_a/R
    print(f"x_c = {xc} m")
    print(f"x_c ~= {round(xc,3)} m")

    dados.clear()
    print()


dados = []

# PROBLEMA RESOLVIDO 3.8 C)
print("PROBLEMA RESOLVIDO 3.8 C)")

# Força 1
F1 = {
    "Valor": 150,
    "Distância em relação ao ponto A": 0
}
dados.append(list(F1.values()))

# Força 2
F2 = {
    "Valor": -600,
    "Distância em relação ao ponto A": 1.6
}
dados.append(list(F2.values()))

# Força 3
F3 = {
    "Valor": 100,
    "Distância em relação ao ponto A": 2.8
}
dados.append(list(F3.values()))

# Força 4
F4 = {
    "Valor": -250,
    "Distância em relação ao ponto A": 4.8
}
dados.append(list(F4.values()))

X_c(dados)

# PROBLEMA 3.106 a)
print("PROBLEMA 3.106 a)")

# Força 1
F1 = {
    "Valor": -18,
    "Distância em relação ao ponto A": 0.25
}
dados.append(list(F1.values()))

# Força 2
F2 = {
    "Valor": -18,
    "Distância em relação ao ponto A": 1.11
}
dados.append(list(F2.values()))

# Força 3
F3 = {
    "Valor": -15,
    "Distância em relação ao ponto A": 1.71
}
dados.append(list(F3.values()))

X_c(dados)

# PROBLEMA GENÉRICO
dnv = 0
while (not dnv):
    n = int(input("Há quantas forças no sistema: "))
    for i in range(1, n+1):
        print(f"*FORÇA 0{i}*")
        val = float(input("Digite o valor da força: "))
        d = float(input("Digite a distância dessa força em relação ao ponto A: "))
        dados.append([val, d])
        print()

    X_c(dados)

    print("Deseja realizar outro problema genérico?")
    print("0- SIM")
    print("1- NÃO")
    dnv = int(input())
    print()
