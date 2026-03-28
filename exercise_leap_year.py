def leap_year():
    """
    Ejercicio 11 (Desafío) - Año Bisiesto

    Leer un año mediante input(). Determinar si es un año bisiesto e imprimir el resultado.
    Un año es bisiesto si:
    - Es divisible por 4, Y
    - NO es divisible por 100, O es divisible por 400

    Ejemplo:
        Para la entrada "2000", la salida esperada es:
        El año 2000 es bisiesto

        Para la entrada "2001", la salida esperada es:
        El año 2001 no es bisiesto

        Para la entrada "1700", la salida esperada es:
        El año 1700 no es bisiesto
    """
    pass
    
    '''
    anio = int(input())
    bisiesto4 = anio % 4
    bisiesto100 = anio % 100
    bisiesto400 = anio % 400
    if bisiesto4 == 0:
        if bisiesto400 == 0:
            
            print(f"El año {anio} es bisiesto")
            
    if bisiesto4 != 0:
        print(f"El año {anio} no es bisiesto")
    '''
    '''
    anio = int(input())
    bisiesto4 = anio % 4
    bisiesto100 = anio % 100
    bisiesto400 = anio % 400
    
    if bisiesto400 == 0:
        if (bisiesto100 < 100 and bisiesto100 > 0) or (bisiesto100 > -100 and bisiesto100 < 0):
            if bisiesto4 == 0:
                print(f"El año {anio} es bisiesto")
                
                
    elif bisiesto4 == 0 and bisiesto100 == 0 and bisiesto400 == 0:
        print(f"El año {anio} es bisiesto")
    '''    
    '''
    anio = int(input())
    bisiesto4 = anio % 4
    bisiesto100 = anio % 100
    bisiesto400 = anio % 400
        
    if bisiesto4 == 0:
        if bisiesto100 == 0 and bisiesto400 == 0:
            print(f"El año {anio} es bisiesto")
        else:
            print(f"El año {anio} no es bisiesto")
    else:
        print(f"El año {anio} no es bisiesto")
    '''
    anio = int(input())
    bisiesto4 = anio % 4
    bisiesto100 = anio % 100
    bisiesto400 = anio % 400
        
 
    if (bisiesto4 == 0 and bisiesto100 != 0) or bisiesto400 == 0:
        print(f"El año {anio} es bisiesto")
    else:
        print(f"El año {anio} no es bisiesto")

#leap_year()