# Logica: Reto 2
# Escribe una función que reciba dos palabras (String) y retorne
# verdadero o falso (Bool) según sean o no anagramas.
# - Un Anagrama consiste en formar una palabra reordenando TODAS
#   las letras de otra palabra inicial.
# - NO hace falta comprobar que ambas palabras existan.
# - Dos palabras exactamente iguales no son anagrama.

import sys

def Anagrama(Word_1, Word_2):
    if (Word_1.lower() == Word_2.lower()):
        print(False)
    else:
        print(''.join(sorted(Word_1.lower())) == ''.join(sorted(Word_2.lower())))

if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2], sys.argv[3])
