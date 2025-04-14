"""
Lista de Compras Simples
"""


# lista a ser trabalhada
lista_compras = []

# loop para exibir opções ao usuário
while True:
    print("Selecione uma opção")
    opcao_usuario = input("[i]nserir [a]pagar [l]istar [s]air: ")
    
    
    if opcao_usuario == "i":
        # adiciona um item na lista
        usuario_adiciona = input("\nItem: ").lower()
        
        # verifica se é um texto vazio, se não for, adiciona o item
        if usuario_adiciona == "":
            print("Por favor, digite algo.")
            continue
        else:
            lista_compras.append(usuario_adiciona)
            print("Item adicionado com sucesso!\n\n")
    elif opcao_usuario == "a":
        # apaga o elemento no índice informado
        indice_exclusao = input("\nDigite o índice: ")

        # tratamento de erros caso o usuário não digite um índice
        try:
            indice_exclusao = int(indice_exclusao)
            lista_compras.pop(indice_exclusao)
            print("Item excluído com sucesso.\n\n")
        except ValueError:
            print("Por favor, utilize apenas índices numéricos.\n\n")
            continue
        except TypeError:
            print("Por favor, utilize apenas índices numéricos.\n\n")
            continue
        except IndexError:
            print("Por favor, utilize apenas índices numéricos.\n\n")
            continue

        continue
    elif opcao_usuario == "l":
        # exibe os itens da lista  
        enumera_itens = enumerate(lista_compras)

        # loop para exibir os nomes com índices
        print(end="\n\n")
        for indice, nome in enumera_itens:
            nome_maiusculo = str(nome).capitalize()
            print(f"{indice} - {nome_maiusculo}")
        print(end="\n\n")
        continue
    elif opcao_usuario == "s":
        # sai do loop de opções do usuário
        print("Saindo...")
        break
    else:
        # garante que o usuário digite uma opção válida
        print("Digite uma opção válida!\n\n")

