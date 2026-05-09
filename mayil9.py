
def derivative(f, x, h=0.0001):
    return (f(x+h) - f(x)) / h

f = lambda x: x**2

result = derivative(f, 5)

print(result)
