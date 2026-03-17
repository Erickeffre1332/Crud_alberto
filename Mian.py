products = []

def create_product(id, name, price):
    # BUG 1: aceita preço negativo
    product = {"id": id, "name": name, "price": price}
    products.append(product)
    print("Produto criado!")

def read_products():
    # BUG 2: quebra se lista estiver vazia (não trata)
    print("Lista de produtos:")
    for product in products:
        print(f"{product['id']} - {product['name']} - R${product['price']}")
    print(f"Total de produtos: {len(products) + 1}")  # BUG: soma +1 errado

def update_product(id, new_name=None, new_price=None):
    # BUG 3: atualiza TODOS os produtos ao invés de um só
    for product in products:
        if new_name:
            product["name"] = new_name
        if new_price:
            product["price"] = new_price
    print("Produtos atualizados!")

def delete_product(id):
    # BUG 4: remove só o primeiro item sempre
    if products:
        products.pop(0)
        print("Produto removido!")
    else:
        print("Lista vazia!")

# Teste
if __name__ == "__main__":
    create_product(1, "Mouse", 50)
    create_product(2, "Teclado", -100)  # preço inválido
    read_products()
    update_product(1, new_price=999)
    read_products()
    delete_product(2)
    read_products()
