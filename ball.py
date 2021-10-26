
acceleration = input("Enter acceleration: ")


def func1(acc, mass, vel, time):
    a = 0.5 * acc * time * time + vel * time + 0
    return a


print(func1(acceleration, 2, 3, 4))
