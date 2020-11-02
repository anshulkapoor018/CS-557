from itertools import product
import random

vo = {"a","e","i","o","u","y"}

def get_inflations(wd):
   
    wd = list(wd)
    for idx, l in enumerate(wd):
        if random.random() * 100 > 60:
            wd[idx] = wd[idx]*int(random.random()*10)
    # ['h','i', 'i', 'i'] becomes ['h', ['i', 'ii', 'iii']]
    return wd

def get_vowelswaps(wd):
    
    wd = list(wd)
    for idx, l in enumerate(wd):
        if type(l) == list:
            pass
        elif l in vo:
            wd[idx] = list(vo)
        
    # ['h','i'] becomes ['h', ['a', 'e', 'i', 'o', 'u', 'y']]
    return wd

def flatten(options):
    # ['h',['i','ii','iii']] becomes 'hi','hii','hiii'
    a = set()
    for p in product(*options):
        a.add(''.join(p))
    return a

def misspell(wd):

    return random.choice(list(flatten(get_vowelswaps(wd)) | flatten(get_inflations(wd))))

if __name__ == "__main__":

    words = ["fishy", "monster", "apple", "saint", "potato", "moth"]
    for word in words:
        print(misspell(word))
