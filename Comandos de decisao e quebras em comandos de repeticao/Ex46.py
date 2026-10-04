'''Faça um programa que, dada uma string, diga se ela é um palíndromo ou não. Lembrando que um palíndromo é uma palavra que tenha a propriedade de poder ser lida tanto da direita para a esquerda como da esquerda para a direita. Exemplos:
           ovo
           arara
           Socorram-me, subi no onibus em Marrocos.
           Anotaram a data da maratona
Não é permitido usar a função replace(), nem funções que alterem a caixa de caracteres (como lower(), upper() ou capitalize(), por exemplo). Também não é permitido comparar strings, mas é permitido comparar caracteres individuais. Apesar de aparecerem apenas poucos símbolos nos exemplos dados, o programa deve ser genérico o suficiente para ignorar todos os símbolos.'''

string = input()
palin = True
ctrlEsq = 0
ctrlDir = len(string)-1
while palin == True:
    if ctrlDir > ctrlEsq:
        caracEsq = string[ctrlEsq]
        caracDir = string[ctrlDir]
        ordEsq = ord(caracEsq)
        ordDir = ord(caracDir)
        letraEsq = ordEsq
        letraDir = ordDir
        if ordEsq < 65:
            while ordEsq < 65:
                if ctrlEsq < len(string)-1:
                    if ctrlEsq < ctrlDir:
                        ctrlEsq = ctrlEsq + 1
                        caracEsq = string[ctrlEsq]
                        ordEsq = ord(caracEsq)
                    else:
                        break
                else:
                    break
            letraEsq = ordEsq
        elif ordEsq < 97:
            while ordEsq > 90: 
                if ctrlEsq < len(string)-1:
                    if ctrlEsq < ctrlDir:
                        ctrlEsq = ctrlEsq + 1
                        caracEsq = string[ctrlEsq]
                        ordEsq = ord(caracEsq)
                    else:
                        break
                else:
                    break
            letraEsq = ordEsq
        if ctrlEsq == ctrlDir:
            break
        elif ctrlEsq > ctrlDir:
            break
        else:
            if ordDir < 65:
                while ordDir < 65:
                    if ctrlDir >= 0:
                        if ctrlEsq < ctrlDir:
                            ctrlDir = ctrlDir - 1
                            caracDir = string[ctrlDir]
                            ordDir = ord(caracDir)
                        else:
                            break
                    else:
                        break
                letraDir = ordDir
            if ordDir <= 90:
                letraDir = ordDir
            elif ordDir < 97:
                while ordDir > 90: 
                    if ctrlDir >= 0:
                        if ctrlEsq < ctrlDir:
                            ctrlDir = ctrlDir - 1
                            caracDir = string[ctrlDir]
                            ordDir = ord(caracDir)
                        else:
                            break
                    else:
                        break
                letraDir = ordDir
            elif ordDir <= 122:
                letraDir = ordDir
            else:
                while ordDir > 122:
                    if ctrlDir >= 0:
                        if ctrlEsq < ctrlDir:
                            ctrlDir = ctrlDir - 1
                            caracDir = string[ctrlDir]
                            ordDir = ord(caracDir)
                        else:
                            break
                    else:
                        break
                letraDir = ordDir
        if ctrlEsq == ctrlDir:
            break
        if ctrlEsq > ctrlDir:
            break
        if letraEsq >= 97:
            if letraEsq <= 122:
                letraEsq = letraEsq - 32
        if letraDir >= 97:
            if letraDir <= 122:
                letraDir = letraDir - 32
        if letraEsq != letraDir:
            palin = False
        ctrlEsq = ctrlEsq + 1
        ctrlDir = ctrlDir - 1
    else:
        break
print(palin)