class A(object):
    atributo_a = 'Valor A'
    
    def __init__(self, atributo):
      self.atributo = atributo
      
    def metodo(self):
        print('A')
        
class B(A):
    atributo_b = 'Valor B'
    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa
        
    def metodo(self):
        print('B')
    
class C(B):
    atributo_c = 'Valor C'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
def metodo(self):
    A.metodo(self)
    B.metodo(self)
    print('C')
    
c = C('Atributo', 'Qualquer')
c.metodo()                            
    
        