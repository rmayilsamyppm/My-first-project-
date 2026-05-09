import random

heads = 0

for i in range(1000):
    toss = random.choice(["H", "T"])

    if toss == "H":
        heads += 1

probability = heads / 1000

print(probability)
