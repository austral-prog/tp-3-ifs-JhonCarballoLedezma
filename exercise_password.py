def password():
    """
    Ejercicio 10 - Validador de Contraseña

    Leer una contraseña mediante input(). Validar que cumpla con los siguientes requisitos:
    1. Debe tener al menos 8 caracteres de longitud
    2. Debe contener al menos un número (usar el operador in para verificar cada dígito del 0 al 9)

    Si cumple ambos requisitos, imprimir "Contraseña valida".
    Si no cumple, imprimir cuál requisito falta.

    Ejemplo:
        Para la entrada "abc12345", la salida esperada es:
        Contraseña valida

        Para la entrada "abc123", la salida esperada es:
        Contraseña muy corta

        Para la entrada "abcdefgh", la salida esperada es:
        Debe contener un numero

        Para la entrada "abc", la salida esperada es:
        Contraseña muy corta
        Debe contener un numero
    """
    
    pass
    #if contrasenia_count >= 8 and "0" in (contrasenia) or "1" in (contrasenia) or "2" in (contrasenia) or "3" in (contrasenia) or "4" in (contrasenia) or "5" in (contrasenia) or "6" in (contrasenia) or "7" in (contrasenia) or "8" in (contrasenia) or "9" in (contrasenia):
    '''
    if contrasenia_count >= 8:
        if "0" in (contrasenia):
            print("Contraseña valida")
        if "1" in (contrasenia):
            print("Contraseña valida")
        if "2" in (contrasenia):
            print("Contraseña valida")
        if "3" in (contrasenia):
            print("Contraseña valida")
        if "4" in (contrasenia):
            print("Contraseña valida")
        if "5" in (contrasenia):
            print("Contraseña valida")
        if "6" in (contrasenia):
            print("Contraseña valida")
        if "7" in (contrasenia):
            print("Contraseña valida")
        if "8" in (contrasenia):
            print("Contraseña valida")
        if "9" in (contrasenia):
            print("Contraseña valida")
    elif contrasenia_count < 8:
        print("Contraseña muy corta")
    '''
        #intento de forma larga
    contrasenia = input()
    contrasenia_count = len(contrasenia)
    if contrasenia_count >= 8:
        if "0" in (contrasenia) or "1" in (contrasenia) or "2" in (contrasenia) or "3" in (contrasenia) or "4" in (contrasenia) or "5" in (contrasenia) or "6" in (contrasenia) or "7" in (contrasenia) or "8" in (contrasenia) or "9" in (contrasenia):
            print("Contraseña valida")
        else:
            print("Debe contener un numero")
            
    elif "0" in (contrasenia) or "1" in (contrasenia) or "2" in (contrasenia) or "3" in (contrasenia) or "4" in (contrasenia) or "5" in (contrasenia) or "6" in (contrasenia) or "7" in (contrasenia) or "8" in (contrasenia) or "9" in (contrasenia):
        if contrasenia_count >= 8:
            print("Contraseña valida")
        else:
            print("Contraseña muy corta")
    else:
        print("Contraseña muy corta")
        print("Debe contener un numero")
    #Bloque innecesario
    '''
    if contrasenia_count >= 8 and "0" in (contrasenia) or "1" in (contrasenia) or "2" in (contrasenia) or "3" in (contrasenia) or "4" in (contrasenia) or "5" in (contrasenia) or "6" in (contrasenia) or "7" in (contrasenia) or "8" in (contrasenia) or "9" in (contrasenia):
        print("Contraseña valida")
    else:
        print("Contraseña muy corta")
        print("Debe contener un numero")
    '''
    
            
#password()