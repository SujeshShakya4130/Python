name = 'TutorialsPoint'
marks = 50
result = True


def myfunction():
    a = 10
    b = 20
    c = a+b
    print("globals():", globals())
    print("locals():", locals())
    return c


myfunction()
