import random
import matplotlib.pyplot as plt


# 10a
def roll_hundred_pair():
    final = []
    
    for rolls in range(100):
        roll = random.randint(2, 13)
        final += [roll]
        
    plt.hist(final)
    plt.show()
    
# 10b
def dice(n):
    
    total = 0
    
    for rolls in range(n):
        d = random.randint(1, 7)
        total += d
        
    return total
    
# 11b
def matches(ticket, winners):
    total = 0
    for item in ticket:
        if item in winners:
            total += 1
    return total
   
# 11c 
def report(guesses, secret):
    number_right_place = 0
    number_wrong_place = 0
    n = -1
    
    for item in guesses:
        n += 1
        if item in secret:
            if guesses[n] == secret[n]:
                number_right_place += 1
            else:
                number_wrong_place += 1
                
    return [number_right_place, number_wrong_place]
    
# 11a
def hangman_display(guessed, secret):
    
    letters = ''
    
    for item in secret:
        if item in guessed:
            letters += item
        elif item == ' ':
            letters += ' '
        else:
            letters += '-'
    print(letters)
    
        
        