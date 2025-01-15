import random 
import time

def traga():
    frutas = ['🍒', '🍋', '🍊', '🍉', '🍇', '🍓']
    print('\nPresiona Enter para jugar')
    resultado = []
    for n in range(3):
        fruta = random.choice(frutas)
        print(fruta, end=' ', flush=True)
        resultado.append(fruta)
        time.sleep(1)
        
    if resultado[0] == resultado[1] == resultado[2]:
        print('\n¡Felicidades, ganaste!')

while True:   
    
    traga()
    