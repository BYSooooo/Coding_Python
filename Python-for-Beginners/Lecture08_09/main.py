## Keyword Arguments

# Positional Arguments
def plus (a,b):
    return a + b

plus(1,2)

# Keyword Argument
# Set a Argument with keyword
def plus_2(a,b,c,d,e):
    return a+b

plus_2(e = 1, c = 2, b = False, d = [1,2], a = "hello")

# mix positional and keyword
def plus_3(a,b,c,d,e):
    return a + b

# 1 = a
plus_3(1, c = 2, d = [1,2], b = False, e = "Hello")