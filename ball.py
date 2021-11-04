def func1(vel, time):
    a = 1/2 * (-9.82) * time * time + vel * time
    if a < 0:
        return 0
    else:
        return a


def getVariables():
    velocity = input("Enter velocity: ")
    try:
        int(velocity)
        print('noice')
    except ValueError:
        print('the fuck u doin')
        velocity = 0
    masse = input("Enter the mass: ")
    try:
        int(masse)
        print('noice')
    except ValueError:
        print('the fuck u doin')
        masse = 1
    tid = input("Enter the time: ")
    try:
        int(tid)
        print('noice')
    except ValueError:
        print('the fuck u doin')
        tid = 1

    print(func1(int(velocity), int(tid)))


getVariables()
