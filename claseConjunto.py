class Conjunto:
    __lista=[]
    
    def __init__ (self):
        self.__lista=[]
        
    def agregar (self,unElemento):
        self.__lista.append(unElemento)
    
    def getElemento (self,i):
        print(i)
        return self.__lista[i]
        
    def getConjunto (self):
        cont=[]
        for elemento in self.__lista:
            cont.append(elemento)
        return cont
    def getLongitud (self):
        long=len(self.__lista)
        return long
    def __add__  (self,otroConjunto):
        nuevoCon=[]
        nuevoCon.extend(self.__lista)
        nuevoCon.extend(otroConjunto.getConjunto())
        nuevoCon=set(nuevoCon)
        return nuevoCon
    
    def AgregarEle (self):
        print ("Se comenzaran a agregar los elementos al conjunto")
        i=1
        while(int(i)==1):
            print("Ingrese elemento: ")
            ele=int(input())
            if type(ele)==int:
                self.agregar(ele)
            else:
                print("El elemento que ingreso es incorrecto")
            print("Ingrese 1 para contunuar agregando elementos \n Ingrese 2 si no va a continuar agregando elementos  ")
            i=input()
                
        
            
    
    def __sub__ (self,otroConjunto):
        nuevocon=[]
        nuevocon.extend(self.__lista)
        conjunto=otroConjunto.getConjunto()
        for elemento in conjunto:
            if elemento in nuevocon:
                nuevocon.remove(elemento)
                
                
        return nuevocon
        
        
        
    def __eq__(self, otroConjunto):
        nuevocon=[]
        nuevocon.extend(self.__lista)
        conjunto=otroConjunto.getConjunto()
        band=True
        if len(conjunto)==len(nuevocon):
            for elemento in conjunto:
                if elemento in nuevocon:
                    band=True
                else:
                    return False
        else:
            return False
        return band
        
                
                
        
                
    def mostrar (self):
        for elemento in self.__lista:
            print(elemento)
            
