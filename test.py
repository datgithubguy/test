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

def callback_l(lst):
    if lst == "+":
        lst= 1.
    else:
        lst= -1.
    return lst
    
def callback_r(lst):
    if lst == "+":
        lst= -1.
    else:
        lst= 1.
    return lst

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
    p = re.compile("((([-+] )?[0-9]+(\.[0-9]*)? \* X\^([-+] )?[0-9]+(\.[0-9]*)? )+\=( ([-+] )?[0-9]+(\.[0-9]*)? \* X\^([-+] )?[0-9]+(\.[0-9]*)?)+)")
    #sanity_check = re.match("(([-+] )?[0-9]+(\.[0-9]+)* \* X\^([-+] )?[0-9]+(\.[0-9]+)*)+", str)
    p.match(str)
    print(p.search(str).group(0))
    #p.findall(str)
    #print(p.findall(str))
    #if sanity_check == str:
    if p.search(str).group(0) != str:
        print("syntax error \n")
    #print(sanity_check)
    tokens = re.split(r"=", str)
    print(tokens)
    left = re.split(r"[+-] ", tokens[0])
    right = re.split(r"^[+-] ", tokens[1])
    print(left)
    print(right)
    p = re.compile("[-+]")
    signs_left = p.findall(tokens[0])
    signs_right = p.findall(tokens[1])
    print(signs_left )
    print(signs_right )
    print("num_field - num_signs == ")
    diff = len(left) - len(signs_left)
    print(diff)
    if diff > 0:
        signs_left.insert(0, "+")
    print(signs_left)
    diff = len(right) - len(signs_right)
    print(diff)
    if diff > 0:
        signs_right.insert(0, "+")
    signs_right = map(callback_r, signs_right)
    print(signs_right)
    signs_left = map(callback_l, signs_left)
    print(signs_left)
    p = re.compile("(^([-+] )?[0-9]+(\.[0-9]*)?)")
    exponents_left = [p.findall(x) for x in left ]
    print(exponents_left)
    # separer : exponent et power
    # multiplier exponent par sign_tabs
    # trier par exponent
    # reduire
    # gestion d'erreur
    # resolution
    
example = "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"

entry_point(example)

print()