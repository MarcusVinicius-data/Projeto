'''aqui foi usado o agregação para usar com seria um
exemplo de uma compra de planos de servidor'''

class Server:
    def __init__(self) -> None:
        self._product = [] #um dicionario que não poderár modificar

  
#   metodo para a listagem de compras do servidor usando 'for e in'
#   com _product.         
    def  total(self):
        return sum([p.price for p in self._product])
    
#   metodo de inserir produtos usando for e in com o metodo append,para adicionar itens em uma lista    
    def insert_products(self, *product):
        for product in product:
            self._product.append(product)
 #listando produtos usando o mesmo metodo for e in com o nome e preço.
    
    def listProduct(self):
        print()
        for product in self._product:
            print(product.name, product.price)
        print()
'''classe criada a baixo que recebe o metodo de iniciação 
com nome e preço do plano do servidor 
'''       
class Product:
    def __init__(self, name, price) -> None: #metodo de iniciação com nome e preco
        self.name = name  #nome
        self.price = price #preço
        
add_to_cart = Server() #variavel criada que recebe a clase Server com todos o parametros criados
server1 , server2 = Product('common server', 59.90), Product('advanced server', 99.90) #variaveis criadas com o nome do plano e preço recebendo a clase product e seus parametros
add_to_cart.insert_products(server1, server2) #adicionando no carrinho de compras no planos selecionados
add_to_cart.listProduct() #listando produtos
print(add_to_cart.total()) #somando o total                           
                
