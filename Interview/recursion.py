# write factorial function 3!
# iterative
def factorial_iterative(n):
    s = ''
    while n > 0:
        s += f'{n} x '
        n -= 1
    return s

def factorial_recursive(n):
    if n == 1:
        return '1'
    else:
        return f'{n} x ' + f'{factorial_recursive(n-1)}'

print(factorial_iterative(5)) 
print(factorial_recursive(5))