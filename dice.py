import random
import matplotlib.pyplot as plt


def roll_dice(sides):
    return random.randint(1, sides)


counter = {
    "d4Counter": 0,
    "d6Counter": 0,
    "d8Counter": 0,
    "d10Counter": 0,
    "d12Counter": 0,
    "d20Counter": 0,
}

while True:
    counter["d4Counter"] += 1
    d4 = roll_dice(4)
    if d4 == 4:
        d6 = roll_dice(6)
        counter["d6Counter"] += 1
        if d6 == 6:
            d8 = roll_dice(8)
            counter["d8Counter"] += 1
            if d8 == 8:
                d10 = roll_dice(10)
                counter["d10Counter"] += 1
                if d10 == 10:
                    d12 = roll_dice(12)
                    counter["d12Counter"] += 1
                    if d12 == 12:
                        d20 = roll_dice(20)
                        counter["d20Counter"] += 1
                        if d20 == 20:
                            break


for key, value in counter.items():
    formatted_value = f"{value:,}"
    print(f"{key}: {formatted_value}")
plt.bar(list(counter.keys()), counter.values(), color="g")
plt.show()
