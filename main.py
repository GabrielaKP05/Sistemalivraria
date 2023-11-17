from livraria import Cliente, Livro

def main():
    # Solicita informações do cliente ao usuário
    codigo = input("Digite o código do cliente: ")
    endereco = input("Digite o endereço do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    identificador = input("Digite o CPF ou CNPJ do cliente: ")

    # Criação de um cliente
    cliente1 = Cliente(codigo, endereco, telefone, identificador)

    # Solicita informações do livro ao usuário
    autor = input("Digite o autor do livro: ")
    assunto = input("Digite o assunto do livro: ")
    editora = input("Digite a editora do livro: ")
    isbn = input("Digite o ISBN do livro: ")
    estoque = int(input("Digite a quantidade em estoque do livro: "))

    # Criação de um livro
    livro1 = Livro(autor, assunto, editora, isbn, estoque)

    # Cliente comprando um livro
    cliente1.comprar_livro(livro1)

    # Imprime as informações do cliente
    print(f"Cliente {cliente1.codigo} comprou o livro {livro1.isbn} em {cliente1.compras[0][0]}")

if __name__ == "__main__":
    main()
