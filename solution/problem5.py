def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    return pair(lambda a, b: a)  # Extracts the first element

def cdr(pair):
    return pair(lambda a, b: b)  # Extracts the second element

if __name__ =='__main__':
    p = cons(3, 4)
    print(car(p))  # Output: 3
    print(cdr(p))  # Output: 4