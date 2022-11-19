import random

class Coin:
    direction = 0
    def __init__(self,direction):
        pass

    def flip():
        options = (1,-1)
        self.direction = random.choice(options)

class Dice:
    distance = 0
    def __init__(self):
        pass

    def roll():
        #Dice.distance = 0
        Dice.distance = (random.randrange(1, 6))

class Player:
    update_postition = 0
    position = 0
    def __init__(self):
        pass
    def take_turn():
        Coin.flip()
        Dice.roll()
        Player.update_position = (Coin.direction * Dice.distance)

class Game:
    turn = 0
    end_position = 0
    def __init__(self):
        pass
    def play():
        while Game.turn < 20:
            Player.take_turn()
            Game.end_position = Player.position
            Game.turn = (Game.turn + 1)