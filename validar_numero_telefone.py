def validar_numero_telefone(numero):
    # Verificar o comprimento do número
    if len(numero) != 9:
        return False
    
    # Verificar se o primeiro número é 9
    if numero[0] != '9':
        return False
    
    # Verificar prefixos inválidos
    prefixos_invalidos = ['+244', '999', '900', '909']
    for prefixo in prefixos_invalidos:
        if numero.startswith(prefixo):
            return False
    
    # Verificar prefixos válidos
    prefixos_validos = ['92', '93', '94', '91', '95', '99']
    if not any(numero.startswith(prefixo) for prefixo in prefixos_validos):
        return False
    
    return True

# Solicitar a entrada do usuário
numero = input("Insira o Nº de telefone: ")
print(f"{numero}: {'Válido' if validar_numero_telefone(numero) else 'Inválido'}")
