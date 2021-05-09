from claseConjunto import Conjunto
def test ():
    unConjunto=Conjunto()
    otroConjunto=Conjunto()
    unConjunto.AgregarEle()
    otroConjunto.AgregarEle()
    print("SE MOSTRARA EL PRIMER CONJUNTO")
    unConjunto.mostrar()
    print("SE MOSTRARA EL SEGUNDO CONJUNTO")
    otroConjunto.mostrar()
    nuevoConjunto= unConjunto+otroConjunto
    print("SE MOSTRARA EL CONJUNTO CREADO A PARTIR DE LA UNION DE LOS DOS CONJUNTOS ANTERIORES")
    print(nuevoConjunto)
    nueco=unConjunto-otroConjunto
    print("SE MOSTRARA EL CONJUNTO CREADO APARTIR DE LA RESTA DE LOS DOS CONJUNTOS")
    print(nueco)
    print("SE MOSTRARA SI LOS CONJUNTOS SON IGUALES O NO")
    n=unConjunto==otroConjunto
    if n==False:
        print("Los dos conjuntos no son iguales")
    else:
        print("Los dos conjuntos son iguales")
if __name__=="__main__":
    test()