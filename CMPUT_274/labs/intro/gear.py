import random

if __name__ == "__main__":
    t = random.randint(-45, 45)
    print("Temperature: {}".format(t))
    if t > -40 and t <= 0:
        print("Winter Coat")
    elif t > 0 and t <= 10:
        print("Light jacket")
    elif t > 10 and t <= 20:
        print("Sweater")
    elif t > 20 and t <= 40:
        print("Sunhat")
    else:
        print("Not going outside")
