#!/usr/bin/env python
print("You Entered private room!")
user_input = raw_input("Enter Password: ")
 
if len(user_input) != 10:
    print "Try Again!"
    exit()
flag = [233, 129, 9, 5, 130, 194, 195, 39, 75, 229]
user_str = []
for char in user_input:
    user_str.append( (((ord(char) << 5) | (ord(char) >> 3)) ^ 111) & 255 )
 
if (user_str == flag):
    print "Well Done"
else:
    print "Try Again!"