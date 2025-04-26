from imports.__init__ import produtos


def formata_texto(lista, texto):
    texto_formatado = texto

    for dicionario in lista:
        texto_formatado += "".join(
            f"Produto: {dicionario['nome']} | Preço: {dicionario['preco']}\n"
        )
    
    return texto_formatado

def aumenta_preco_em_10_por_cento(lista):
    nova_lista = []

    # aumento 10% do preço de cada produto da lista
    for dicionario in lista:
        aumenta_10_por_cento = round(dicionario["preco"] * (1 + 0.10), 2)
        nova_lista.append({"nome": dicionario["nome"], "preco": aumenta_10_por_cento})

    return nova_lista
