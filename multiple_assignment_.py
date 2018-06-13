def multiple_return():
    a =15
    b=90
    return a,b


if __name__== "__main__":
    #this is a demonstration of chained assignment
    a = 5
    a, b = a+1, a
    c=1000
    a, b = multiple_return()
    print(a)
    print(b)
    #print(eval(input()))
    print(range(49))