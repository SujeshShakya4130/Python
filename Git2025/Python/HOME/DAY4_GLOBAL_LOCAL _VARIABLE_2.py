# this is a global variable
marks = 50


def myfunction():
    global marks
    marks = marks + 20
    print(marks)


myfunction()
# prints global value
print(marks)

# the code will show unbound local error
