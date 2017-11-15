import random
import matplotlib.pyplot as plt

plt.ion()

def roll_hundred_pair():
    
    for dice in range(100):
        final = random.randint(1, 100)
        
        plt.hist(final)
        plt.show()

def dice(n):
    
    total = 0
    
    for dice in range(n):
        rolls = random.randint(1, 6)
    
        total += rolls
    print ('Roll was %s' % (total))
    
def matches(ticket, winners):
    
    total = 0
    
    for ticket in winners:
        total += 1
        
    return total
    