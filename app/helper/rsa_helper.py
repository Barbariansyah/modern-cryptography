import random
from app.util.util import gcd
'''
choose e:
1. greater than 2
2. less than toitent
3. coprime with toitent
'''
def choose_e(toitent):
    random.seed(0)
    e = random.rand(2, toitent)
    
    while  gcd(e, toitent) != 1:
        e = random.rand(2, toitent)
    
    return e