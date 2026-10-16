# Faça uma função que receba uma cadeia de caracteres no formato “DD/MM/AAAA” e retorne o dia, mês e ano para 3 variáveis inteiras. Nessa função, verifique se as barras estão no lugar certo, e se DD, MM e AAAA são numéricos. Caso alguma verificação não seja válida, os retornos devem ser iguais a zero.

def funcao(x):
    dia = 0
    mes = 0
    ano = 0
    data = x.split("/")
    if len(x) == 10 and (x[2] == "/" and x[5] == "/") and (data[0].isdigit() and data[1].isdigit() and data[2].isdigit()):
        dia = int(data[0])
        mes = int(data[1])
        ano = int(data[2])
    return dia, mes, ano