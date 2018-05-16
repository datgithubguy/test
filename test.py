import re
import sys

def my_square_root(num):
    if num == 0. or num == 1.:
        return num
    i = 1.
    result = 1.
    while result <= num:
        i = i + .0000001
        result = i*i
    return float(i)
    
    
#print(my_square_root(20.5))
r = lambda x: x**(.5)
print(r(20.5))

def entry_point(str):
    #if len(sys.argv) != 2:
    #    print("incorrect user input") 
    #    exit
    #else:
    #    print(sys.argv[1])
    #print(sys.argv)
    #
    # if more than 2 equals syntax error
    i = 1
    p = re.compile("((([-+] )?[0-9]+(\.[0-9]+)* \* X\^([-+] )?[0-9]+(\.[0-9]+)* )+\=( ([-+] )?[0-9]+(\.[0-9]+)* \* X\^([-+] )?[0-9]+(\.[0-9]+)*)+)")
    #sanity_check = re.match("(([-+] )?[0-9]+(\.[0-9]+)* \* X\^([-+] )?[0-9]+(\.[0-9]+)*)+", str)
    p.match(str)
    print(p.search(str).group(0))
    #p.findall(str)
    #print(p.findall(str))
    #if sanity_check == str:
    if p.search(str).group(0) != str:
        print("syntax error \n")
    #print(sanity_check)
    right = re.match(r" ", str)


example = "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"

entry_point(example)

print()