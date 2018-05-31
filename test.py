import sys


print ("Hello World from PYTHON"+sys.version)

def say_hello(hello_var):
    print(hello_var)

    def say_hi(hi_var):
        print(hello_var+" "+hi_var+" end")

    return say_hi

say_hello("Hello")("HI")
