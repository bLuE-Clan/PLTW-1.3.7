import random
import matplotlib.pyplot as plt

def dice(n):
    total = 0 
    for rolls in range(n):
        rolls = random.randint(1, 6)
        
        total += rolls
    print ('roll was %s' % (total))
    