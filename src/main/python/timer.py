​​import time
import random
 
our_list = list(range(10000000))
element = 7000000
 
start = time.time()
 
random_choice = random.choice(our_list)
while random_choice != element:
    random_choice = random.choice(our_list)
 
end = time.time()
 
print(end - start)

def countdown(seconds):
    time_left = seconds
    