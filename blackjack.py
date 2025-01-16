import random
import time
cards ={
        'A': 11,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 10,
        'Q': 10,
        'K': 10
    }



    
def calculate_hand(hand):
    total = 0
    ass = 0
    for card in hand:
        if card =='A':
            ass += 1
        total += cards[card]
    
    while total > 21 and ass >0:
        total -= 10
        ass -= 1
    
    return total
def blackjack():   
    print('\n¡Bienvenido a Blackjack!')
    player= []
    house = []
    mazo_completo = [carta for carta in cards.keys() for _ in range(4)]
    player.append(random.choice(mazo_completo))
    mazo_completo.remove(player[-1])   
    player.append(random.choice(mazo_completo))
    mazo_completo.remove(player[-1])
    
    house.append(random.choice(list(mazo_completo)))
    mazo_completo.remove(house[-1])
    house.append(random.choice(list(mazo_completo)))
    mazo_completo.remove(house[-1])
    print('*Tus cartas son:', player)
    print('*Las cartas de la casa son:', house)
    option = input('\n->Quieres Pedir (P) o Plantarse (S)?\n')
    while 'P' in option:
        player.append(random.choice(list(mazo_completo)))
        mazo_completo.remove(player[-1])
        house.append(random.choice(list(mazo_completo)))
        mazo_completo.remove(house[-1])
        print('*Tus cartas son:', player)
        print('*Las cartas de la casa son:', house)
        option = input('Quieres Pedir (P) o Plantarse (S)?')
    
    if 'S' in option:
        total_player = calculate_hand(player)
        total_house = calculate_hand(house)
        while total_house <16:
            house.append(random.choice(list(cards.keys())))
            mazo_completo.remove(house[-1])
            total_house = calculate_hand(house)
        if total_player >  total_house and total_player <= 21 or total_house > 21 and total_player <= 21:
            print('\n¡Ganaste!')
        else:
            print('\n¡Perdiste!')
        print('\nMaso completo:', mazo_completo)
        
        
    
blackjack()

