from cmath import sqrt


class Operacion():    
        
    def sumar(n1,n2):    
        return n1+n2
    
    def restar(n1,n2):
        return n1-n2
    
    def multiplicar(n1,n2):
        return n1*n2
    
    def dividir(n1,n2):
        return n1/n2    

    def potencia(n1,n2):
        return n1**n2
    
    def porcentaje(n1,n2):
        return n1*n2/100
    
    def raiz_cuadrada(n1):
        return sqrt(n1)
    
    def raiz(n1,n2):
        return n1**(1/n2)