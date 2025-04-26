from copy import deepcopy
from imports.imports import formata_texto, aumenta_preco_em_10_por_cento, produtos


def ordena_produtos_por_nome_decrescente():
    preco_aumentado = deepcopy(aumenta_preco_em_10_por_cento(produtos))
    texto_formatado = f"Ordenando por Nome (decrescente)\n----------------------------------\n"

    # ordena com base do nome do produto, de forma decrescente
    ordena = sorted(preco_aumentado, key=lambda x: x["nome"], reverse=True)    

    # formatando o texto a ser exibido
    texto_formatado = formata_texto(ordena, texto_formatado)
    
    return texto_formatado


def ordena_produtos_por_preco_crescente():
    preco_aumentado = deepcopy(aumenta_preco_em_10_por_cento(produtos))
    texto_formatado = f"Ordenado por Preço (crescente)\n----------------------------------\n"

    # ordena por preço, de forma crescente
    ordena = sorted(preco_aumentado, key=lambda x: x["preco"])        

    # formatando o texto a ser exibido
    texto_formatado = formata_texto(ordena, texto_formatado)

    return texto_formatado


print(ordena_produtos_por_nome_decrescente())
print("__" * 17, end="\n\n\n")
print(ordena_produtos_por_preco_crescente())
