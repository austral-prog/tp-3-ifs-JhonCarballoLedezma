def age_check():
    """
    Ejercicio 3 - Verificar Mayoría de Edad

    Leer una edad y un límite de edad mediante input(). Verificar que ambos números sean
    válidos (positivos), y luego determinar si la persona es mayor de edad comparando
    con el límite ingresado.

    Si alguno de los números es negativo o cero, imprimir "Entrada invalida".

    Ejemplo:
        Para las entradas "20" y "18", la salida esperada es:
        Eres mayor de edad

        Para las entradas "16" y "18", la salida esperada es:
        Eres menor de edad

        Para las entradas "-5" y "18", la salida esperada es:
        Entrada invalida
    """
    pass
    '''
    edad = int(input())
    edad_limite= int(input())
    
    if edad and edad_limite > 0:
        if edad <= 18:
            print('Eres menor de edad')
        elif edad <= edad_limite:
            print('Entrada invalida')
    else:
        print('Entrada invalida')  
    '''
    '''
    edad = int(input())
    edad_limite= int(input())
    if edad and edad_limite > 0:
        if edad >= edad_limite:
            print("Eres mayor de edad")
        else:
            print("Eres menor de edad")
    else:
        print("Entrada invalida")
    '''  
    #problema es que entre en el apartado de  if, ya que -5 entre en que ambos sean > 0 cuando no lo son
    edad = int(input())
    edad_limite= int(input())
    
    if edad <= 0 or edad_limite <= 0:
        print("Entrada invalida")
    elif edad >= edad_limite:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")

#age_check()
