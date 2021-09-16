def fun(**kwargs):
    print(type(kwargs))
    print(kwargs)


def fun2(*args, **kwargs):
    pass


fun(a=10, b=20, c="Abc")
fun(x=10, y=20)

fun2(10, 20, name='abc')
