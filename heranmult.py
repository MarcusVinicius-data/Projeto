class A:
    pass

    def quem_sou(self):
        print('A')
  
        
class B(A):
    pass
   
    
class C(A):
    pass

    def quem_sou(self):
        print('C')
      
        
class D(B,C):
    pass 

    def quem_sou(self):
        print('D')
        
        
        
var = D()
var.quem_sou()
print(D.mro())                            