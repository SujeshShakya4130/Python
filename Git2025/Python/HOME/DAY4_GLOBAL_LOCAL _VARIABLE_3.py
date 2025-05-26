var1 = 50  # this is a global variable
var2 = 60  # this is a global variable


def myfunction():
    "Change values of global vatiacles"
    globals()['var1'] = globals()['var1']+10
    global var2
    var2 = var2 + 20


myfunction()
print("var1:", var1, "var2:", var2)  # shows global variables
