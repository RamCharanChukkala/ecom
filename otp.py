import random
def genotp():
    ul=[chr(i) for i in range(ord('A'),ord('Z')+1)]
    sl=[chr(i) for i in range(ord('a'),ord('z')+1)]
    otp=''
    for i in range(2):
        otp=otp+random.choice(ul)
        otp=otp+str(random.randint(0,9))
        otp=otp+random.choice(sl)
    return otp