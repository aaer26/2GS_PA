def hanoi(discos, inicio, intermedio, fin):


    #caso base
    if discos == 1:
        print(inicio, "→", fin)

    else:
        #1. Mover todos menos el ultimo (n-1) al intermedio
        hanoi(discos-1,inicio, fin , intermedio ) #me hace los print 

        #2. Mover el grande a final
        print(inicio, "→", fin)

        #3. Mover los n-1 (todos menos el grande) del intermedio al final
        hanoi(discos-1, intermedio  ,  inicio  , fin)