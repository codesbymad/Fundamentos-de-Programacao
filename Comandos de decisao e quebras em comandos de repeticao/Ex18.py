# Faça um função que receba a data atual (cadeia de caracteres no formato “DD/MM/AAAA”) e retorne uma string com a data onde o mês está no formato textual por extenso. Considere que a data é válida. Exemplo: Data: 01/01/2000, retornar: 1 de janeiro de 2000.

def funcao(data):
    sep = data.split("/")
    dia = int(sep[0])
    ano = sep[2]
    if sep[1] == "01":
        mes = " de janeiro de "
    elif sep[1] == "02":
        mes = " de fevereiro de "
    elif sep[1] == "03":
        mes = " de marco de "
    elif sep[1] == "04":
        mes = " de abril de "
    elif sep[1] == "05":
        mes = " de maio de "
    elif sep[1] == "06":
        mes = " de junho de "
    elif sep[1] == "07":
        mes = " de julho de "
    elif sep[1] == "08":
        mes = " de agosto de "
    elif sep[1] == "09":
        mes = " de setembro de "
    elif sep[1] == "10":
        mes = " de outubro de "
    elif sep[1] == "11":
        mes = " de novembro de "
    elif sep[1] == "12":
        mes = " de dezembro de "
    dataExt = str(dia) + mes + ano
    return dataExt

x = input("")
y = funcao(x)
print(f"{y}")