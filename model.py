x = 0
y = 0

def init(a, b):
    global x
    global y
    x = a
    y = b

def do_it(action): 
    if action == "+": return x + y
    if action == "-": return x - y
    if action == "/": return x / y
    if action == "*": return x * y