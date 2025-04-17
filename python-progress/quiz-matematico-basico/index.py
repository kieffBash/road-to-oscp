"""
Sobre a "lista_respostas", é meio confuso ter que colocar o índice no 
lugar da resposta em si, mas foi como nosso professo pediu, acredito que
tenha sido para colocar uma dificuldade a mais no código
"""


perguntas = [
    {
        "Pergunta": "Quanto é 2+2?",
        "Opções": ["1", "3", "4", "5"],
        "Resposta": "4",
    },
    {
        "Pergunta": "Quanto é 5*5?",
        "Opções": ["25", "55", "10", "51"],
        "Resposta": "25",
    },
    {
        "Pergunta": "Quanto é 10/2?",
        "Opções": ["4", "5", "2", "1"],
        "Resposta": "5",
    }
]

# pega do usuário a resposta e retorna se esta correto
def quiz_matematico():
    contador = 0
    acertos = 0
    lista_respostas = ["3", "1", "2"]
 
    for i in lista_respostas:
        texto_pergunta = f"Pergunta: {perguntas[contador]['Pergunta']}\n\nOpções:\n"
        
        # gera índices para cada opção de resposta
        for indice, opcao in enumerate(perguntas[contador]["Opções"], 1):
            texto_pergunta += "".join(f"{indice}) {opcao}\n")
        
        texto_formatado = input(f"{texto_pergunta}\nDigite sua escolha: ")
        contador += 1
        
        # verifica se a resposta do usuário é igual a resposta da lista
        if texto_formatado == i:
            print("Resposta correta!")
            print()
            acertos += 1
            continue
        else:
            print("Resposta incorreta.")
            print()
            continue
 
            
    qtd_acertos = f"Você acertou {acertos} de 3 perguntas."
    print(qtd_acertos, end="\n\n")
 
quiz_matematico()
