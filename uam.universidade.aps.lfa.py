def juntatranqueiras(string):
    if identificador(string):
        return True
    elif numero(string):
        return True
    else:
        return False


def identificador(string):
    # Pega o primeiro caracter da tabela ASCII
    primeiro = ord(string[0])
    # Se não estiver entre [a-z] retorna False
    if not (97 <= primeiro <= 122):
        return False
    # percorre a string
    for caracter in string:
        decimal = ord(caracter)
        # Se não estiver em [a-z] ou [0-9] ou [_] retorna False
        if not ((97 <= decimal <= 122) or (48 <= decimal <= 57) or (decimal == 95)):
            return False
    print('[identificador] = "' + string + '"')
    return True


def op_atrib(string):
    # se não for '=' e o tamanho for 1, retorna False
    if string == '=':
        print('[op.atrib] = "' + string + '"')
        return True
    return False


def numero(string):
    # Se o primeiro carater for '.' ou o ultimo caracter for '.' ou a quantidade de '.' for maior que 1, retorna False
    if string[0] == '.' or string[-1] == '.' or string.count('.') > 1:
        return False

    for caracter in string:
        decimal = ord(caracter)
        # se o numero não for entre [0-9] retorna False
        if not 47 < decimal < 58 or decimal == 46:
            return False
    print('[numero] = "' + string + '"')
    return True


def pv(string):
    # Se o ultimo caracter não for ';' e o tamanho for 1, retorna False
    if string == ';':
        print('[pv] = "' + string + '"')
        return True
    return False


# ----------------------------------------------------------------------------------------------------------------------
def main(string):
    estado = 0
    cont = 0

    string = string.replace(" ", ",")
    string = string.replace(";", ",;")
    lista = string.split(",")

    print('\nEstado Inicial: [Q0]')
    print('Estado Lixo: [Q4]')
    print('Estado Final: [Q3]')

    lista = filter(None, lista)

    for tipo in lista:
        print('\nNo estado Q' + str(estado) + ':')

        if identificador(tipo) and cont == 0:
            if estado == 0:
                estado = 1
                cont += 1
            else:
                estado = 5

        elif op_atrib(tipo) and cont == 1:
            if estado == 1:
                estado = 2
                cont += 1
            else:
                estado = 5

        elif juntatranqueiras(tipo):
            if estado == 2:
                estado = 3
            else:
                estado = 5

        elif pv(tipo):
            if estado == 3:
                estado = 4
            else:
                estado = 5

        else:
            print('[Não-Identificado] = ' + tipo)
            estado = 5

        print('VAI PARA Q' + str(estado))

    if estado == 4:
        (print("\n\n--- A operação de atribuição foi aceita ---\n\n"))
    else:
        print("\n\n--- A operação de atribuição foi rejeitada ---\n\n")


while True:
    main(input(str('\nDigite uma palavra: ')))
