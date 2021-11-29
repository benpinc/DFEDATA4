yellow = int(input("Enter the number of yellow balls: "))
blue = int(input("Enter the number of blue balls: "))
red = int(input("Enter the number of red balls: "))
green = int(input("Enter the number of green balls: "))

def choose_balls(yellow,blue,red,green):
    balls = yellow + blue + red + green
    return balls

def probability_yellow():
    balls = yellow + blue + red + green
    probability = yellow/balls
    return probability

def probability_blue():
    balls = yellow + blue + red + green
    probability = blue/balls
    return probability

def probability_red():
    balls = yellow + blue + red + green
    probability = red/balls
    return probability

def probability_green():
    balls = yellow + blue + red + green
    probability = green/balls
    return probability

print("probability of blue is ", probability_blue())
print("probability of yellow is ", probability_yellow())
print("probability of red is ", probability_red())
print("probability of green is ", probability_green())