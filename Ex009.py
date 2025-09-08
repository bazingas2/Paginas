import random
import string
def letra_aletorio():
    return random.choice(string.ascii_uppercase)
letra = letra_aletorio()
print(letra)