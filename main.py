def ordenar_lista():
    print("Digite uma lista de palavras separadas por vírgula (ex: maçã, banana, laranja):")
    entrada = input("Sua lista: ")
    
    # Divide a entrada em uma lista de palavras, removendo espaços extras
    lista = [palavra.strip() for palavra in entrada.split(",")]
    
    # Ordena a lista em ordem alfabética
    lista_ordenada = sorted(lista)
    
    print("\nLista em ordem alfabética:")
    print(lista_ordenada)

if __name__ == "__main__":
    ordenar_lista()