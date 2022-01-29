# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 08:33:06 2021

@author: THILAK
"""

import time
def countdown(t):
    while t > 0:
        print(t)
        t -= 1
        time.sleep(1)
    print("BLAST OFF!")

print("How many seconds to count down? Enter an integer:")
print("T-minus")
seconds = input()
while not seconds.isdigit():
    print("That wasn't an integer! Enter an integer:")
    seconds = input()
seconds = int(seconds)
countdown(seconds)