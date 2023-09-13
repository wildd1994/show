
def decorator(func):
    cache = {}

    def inner(*args, **kwargs):
        print('Считаем кэш')
        res = func(*args, **kwargs)
        return res
    return inner


@decorator
def fn():
    i = 0
    while True:
        i += 1
        yield




fn([123, 123, 123])
fn([123, 123, 123])
fn(5)
fn(15)
fn(20)

