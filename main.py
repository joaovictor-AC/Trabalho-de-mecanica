''' 
Exercício 3.C1 - Uma viga AB está sujeita a diversas forças verticais como mostrado. Escreva um
programa de computador que pode ser usado para determinar a magnitude da resultante das forças e a distância x C ao ponto C, o ponto onde o
 a linha de ação da resultante intercepta AB. Use este programa para resolver
 (a) Exemplo de Problema. 3.8 c, (b) Prob. 3.106a.
'''
# Segue abaixo as funções para realização dos cálculos

# Função para determinar o momento no ponto A
def momento_em_A(dados):
    M_a = 0 # A variável M_a que representa o momento é instanciada com seu valor inicial igual a 0.
    for F in dados:
        M_a += F[0]*F[1] # Cria-se um loop no array dados e incrementa a variável M_a com o valor da força F[0] multiplicado pela distância F[1].
    return M_a

# Função para determinar a função resultante do sistema
def forca_resultante(dados):
    R = 0 # A variável R que representa a força resultante é instanciada com seu valor inicial igual a 0.
    for F in dados:
        R += F[0] # Cria-se um loop no array dados e incrementa a variável R com o valor da força F[0].
    return R

# Função para determinar a distância Xc
def X_c(dados):
    M_a = momento_em_A(dados) # M_a recebe o valor retornado pela função que calcula o momento resultante.
    R = forca_resultante(dados) # R recebe o valor retornado pela função que calcula a força resultante.
    xc = M_a/R # xc representa a distância em relação ao ponto de referência e é a divisão do momento pela força.

    print(f"A força resultante é: {R} N")
    print(f"x_c = {xc} m")
    print(f"x_c ~= {round(xc,3)} m") # xc aproximado com 3 casas decimais

    dados.clear()
    print()


dados = [] # Array vazio.

''' 
PROBLEMA RESOLVIDO 3.8 C)
Uma viga de 4,80 m de comprimento está submetida às forças mostradas. Reduza o dado
sistema de forças para (c) uma única força ou resultante.
 Observação . Como as reações nos apoios não estão incluídas no
dado sistema de forças, o sistema dado não manterá a viga em
equilíbrio.

Neste exercício adotamos o sentido das forças para baixo como negativo e para cima positivo.
'''
print("PROBLEMA RESOLVIDO 3.8 C)")

# Força 1
F1 = {
    "Valor": 150,
    "Distância em relação ao ponto A": 0
}
dados.append(list(F1.values())) # Adiciona o objeto com os parãmetros força e distância ao array de dados.

# Força 2
F2 = {
    "Valor": -600,
    "Distância em relação ao ponto A": 1.6
}
dados.append(list(F2.values())) # Adiciona o objeto com os parãmetros força e distância ao array de dados.

# Força 3
F3 = {
    "Valor": 100,
    "Distância em relação ao ponto A": 2.8
}
dados.append(list(F3.values())) # Adiciona o objeto com os parãmetros força e distância ao array de dados.

# Força 4
F4 = {
    "Valor": -250,
    "Distância em relação ao ponto A": 4.8
}
dados.append(list(F4.values())) # Adiciona o objeto com os parãmetros força e distância ao array de dados.

X_c(dados) # Chama a função que calcula a distãncia xc passando como parâmetro o array de dados.

"""
PROBLEMA 3.106 a)
Três refletores de palco são montados em um tubo, como mostra a figura. As luzes em A e B pesam 18 N cada uma,
enquanto a outra em C pesa 15 N. a) Se d = 0,60 m, determine a distância do ponto D até a linha de ação da resultante
dos pesos dos três refletores. b) Determine o valor de d de modo que a resultante dos pesos passe pelo ponto médio do tubo.
"""

print("PROBLEMA 3.106 a)")

# Força 1
F1 = {
    "Valor": -18,
    "Distância em relação ao ponto A": 0.25
}
dados.append(list(F1.values())) # Adiciona o objeto com os parãmetros força e distância ao array de dados.

# Força 2
F2 = {
    "Valor": -18,
    "Distância em relação ao ponto A": 1.11
}
dados.append(list(F2.values())) # Adiciona o objeto com os parãmetros força e distância ao array de dados.

# Força 3
F3 = {
    "Valor": -15,
    "Distância em relação ao ponto A": 1.71
}
dados.append(list(F3.values())) # Adiciona o objeto com os parãmetros força e distância ao array de dados.

X_c(dados) # Executa a função que calcula a distãncia xc passando como parâmetro o array de dados.

# PROBLEMA GENÉRICO
print("Problema genérico")
dnv = 0
while (not dnv):
    n = int(input("Há quantas forças no sistema: ")) # Número de forças
    for i in range(1, n+1):
        print(f"*FORÇA 0{i}*")
        val = float(input("Digite o valor da força: ")) # Valor da força
        d = float(input("Digite a distância dessa força em relação ao ponto A: ")) # Distância da força em relação ao ponto de origem.
        dados.append([val, d]) # Adiciona os parãmetros força e distância ao array de dados. 
        print()

    X_c(dados) # Executa a função que calcula a distãncia xc passando como parâmetro o array de dados.

    print("Deseja realizar outro problema genérico?")
    print("0- SIM")
    print("1- NÃO")
    dnv = int(input())
    print()
