def inverte_string(string):
    # Aqui vou converter a string
    caracteres = list(string)
    
    # Para o primeiro caractere
    inicio = 0
    # Para o último caractere
    fim = len(caracteres) - 1
    
    # Se os indices não se cruzarem
    while inicio < fim:
        # Trocar a posição dos caracteres
        caracteres[inicio], caracteres[fim] = caracteres[fim], caracteres[inicio]
        # Mover os indices para o próximo caractere
        inicio += 1
        fim -= 1
    
    # Retornar a string invertida
    return ''.join(caracteres)

# Entrada de string
entrada = input("Digite uma string: ")

# Chamada de função para inverter a string
string_invertida = inverte_string(entrada)

# Exibir a string invertida
print("String invertida:", string_invertida)
