import random
import string

from palabras import palabras
from ahorcado_diagramas import vidas_diccionario_visual

def obtener_palabra_valida(palabras):
    #Seleccionar una palabra al azar de la lista
    # de palabras validas
    palabra = random.choice(palabras)

    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)

    return palabra.upper()

def ahorcado():
    print('===========================================')
    print('   ¡Bienvenido(a) al Juego del Ahorcado!   ')
    print('===========================================')
    
    palabra = obtener_palabra_valida(palabras)

    letras_por_adivinar = set(palabra)#conjunto
    letras_adivinadas = set()
    abecedario = set(string.ascii_uppercase)

    vidas = 9

    while len(letras_por_adivinar) > 0 and vidas > 0:
        print(f'Te quedan {vidas} vidas y has usado estas letras: {" ".join(letras_adivinadas)}')

        #Mostrar el estado actual de la palabra
        palabra_lista = [letra if letra in letras_adivinadas else '_' for letra in palabra]

        #Mostrar estado del ahorcado
        print(vidas_diccionario_visual[vidas])

        #Mostrar letras adivinadas en la palabra seleccionada separadas por un espacio
        print(f'Palabra: {" ".join(palabra_lista)}')

        letra_usuario = input('Escoge una letra: ').upper()
        
        #Si la letra escogida por el usuario esta en el
        #abecedario y no esta en el conjunto de letras
        #que ya se ha ingresado, se añade la letra al conjunto
        #de letras ingresadas.
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)

            #Si la letra esta en la palabra,
            #quitar la letra del conjunto de letras
            #pendientes por adivinar.
            #Si no esta en la palabra, quitar una vida
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
            else:
                vidas -= 1
                print(f'\n Tu letra, {letra_usuario} no esta en la palabra')
        #Si la letra escogida por el usuario ya fue ingresada
        elif letra_usuario in letras_adivinadas:
            print('\nYa escogiste esa letra. Por favor escoge una letra nueva')
        else:
            print('\nEsta letra no es valida')
            
    #El jugador llega a esta linea cuando se adivinan todas las
    #letras de la palabra o cuando se agontan las vidas del
    #jugador
    if vidas == 0:
        print(vidas_diccionario_visual)
        print(f'¡Ahorcado! Perdiste. Lo lamento mucho. La palabra era: {palabra}')
    else:
        print(f'¡Excelente! ¡Adivinaste la palabra {palabra}!')


ahorcado()