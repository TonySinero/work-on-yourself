s = ['hello','python','this','code','here',]
lis = [print(f'{x} - {y}') for x,y in enumerate(s)]


waf = ((lambda **kwargs: {k*2: v for k, v in kwargs.items()})(abc=5, de=1))
print(dict(waf))

def my_decorator(func):
    def wrapper(*arg):
        new_arg = [a for a in arg if a % 2 == 0]
        return func(new_arg)

    return wrapper


@my_decorator
def real_func(x):
    print(x)


real_func([1, 2, 3, 4, 5, 6, 7, 8, ])


def my_decorator(func):
    def wrapper(*arg):
        new_arg = [a for a in reversed(arg)]
        return func(new_arg)

    return wrapper


@my_decorator
def real_func(x):
    print(x)


real_func([1, 2, 3, 4, 5, 6, 7, 8, ])