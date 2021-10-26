def func1(acc, mass, vel, time):
    a = 1/2 * acc * time * time + vel * time + 0
    if a < 0:
        return 0
    else:
        return a

acceleration = input("Enter acceleration: ")
try:
    int(acceleration)
    print('noice')
except ValueError:
    print('the fuck u doin')
    acceleration = 0
masse = input("Enter the mass: ")
try:
    int(masse)
    print('noice')
except ValueError:
    print('the fuck u doin')
    masse = 1
velocity = input("Enter the velocity: ")
try:
    int(velocity)
    print('noice')
except ValueError:
    print('the fuck u doin')
    velocity = 0
tid = input("Enter the time: ")
try:
    int(tid)
    print('noice')
except ValueError:
    print('the fuck u doin')
    tid = 1

print(func1(int(acceleration), int(masse), int(velocity), int(tid)))