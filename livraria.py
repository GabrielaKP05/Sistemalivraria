from datetime import datetime

# Definição das classes
class Cliente:
    def __init__(self, codigo, endereco, telefone, identificador):
        self.codigo = codigo
        self.endereco = endereco
        self.telefone = telefone
        self.identificador = identificador
        self.compras = []

    def comprar_livro(self, livro):
        self.compras.append((datetime.now(), livro))
        livro.estoque -= 1

class Livro:
    def __init__(self, autor, assunto, editora, isbn, estoque):
        self.autor = autor
        self.assunto = assunto
        self.editora = editora
        self.isbn = isbn
        self.estoque = estoque

# Execução do programa
def main():
    # Criação de um cliente
    cliente1 = Cliente("001", "Rua das Flores, 123", "(11) 12345-6789", "123.456.789-00")

    # Criação de um livro
    livro1 = Livro("Autor Exemplo", "Assunto Exemplo", "Editora Exemplo", "123-4567890123", 10)

    # Cliente comprando um livro
    cliente1.comprar_livro(livro1)

    # Imprime as informações do cliente
    print(f"Cliente {cliente1.codigo} comprou o livro {livro1.isbn} em {cliente1.compras[0][0]}")

if __name__ == "__main__":
    main()
