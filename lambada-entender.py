
v1 = [1, 1, 1]
v2 = [2, 2, 2]
v3 = [3, 3, 3]

p = lambda p1, p2, p3: p1+p2+p3

# pp = [1, 1, 1, 2, 2, 2, 3, 3, 3]

"""
def p(a, b, c):
    return a+b+c
"""
# soma =  list(map(p, v1, v2, v3))

string = list(map(p, v1, v2, v3))

print(string)
