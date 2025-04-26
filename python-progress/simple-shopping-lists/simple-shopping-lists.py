"""
Lista de Compras Simples
"""


shopping_list = []

# loop para exibir opções ao usuário
while True:
    print("Selecione uma opção")
    user_option = input("[i]nserir [a]pagar [l]istar [s]air: ")
    
    
    if user_option == "i":
        # adiciona um item na lista
        add_item = input("\nItem: ").lower()
        
        # verifica se é um texto vazio, se não for, adiciona o item
        if add_item == "":
            print("Por favor, digite algo.")
            continue
        else:
            shopping_list.append(add_item)
            print("Item adicionado com sucesso!\n\n")
    elif user_option == "a":
        # apaga o elemento no índice informado
        deletion_index = input("\nDigite o índice: ")

        # tratamento de erros caso o usuário não digite um índice
        try:
            deletion_index = int(deletion_index)
            shopping_list.pop(deletion_index)
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
    elif user_option == "l":
        # exibe os itens da lista  
        enumerate_itens = enumerate(shopping_list)

        # loop para exibir os nomes com índices
        print(end="\n\n")
        for index, name in enumerate_itens:
            uppercase_name = str(name).capitalize()
            print(f"{index} - {uppercase_name}")
        print(end="\n\n")
        continue
    elif user_option == "s":
        # sai do loop de opções do usuário
        print("Saindo...")
        break
    else:
        # garante que o usuário digite uma opção válida
        print("Digite uma opção válida!\n\n")

