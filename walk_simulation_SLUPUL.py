import random_walk_SLUPUL

results = []

a = random_walk_SLUPUL.Coin
b = random_walk_SLUPUL.Dice
c = random_walk_SLUPUL.Player
d = random_walk_SLUPUL.Game

def start_simulation(*numbers):
        instances = 0
        while instances < 100:
            d.play()
            results.append(random_walk_SLUPUL.Game.end_position)
            instances = (instances + 1)

start_simulation(random_walk_SLUPUL)
#float_results = list(map(float, results))
average_position = (sum(results[0:100])/100)
print("Average position after 100 games (20 moves per game) is ", average_position)
print(random_walk_SLUPUL.Game.end_position)
print(len(results))

