# e.g. 1
def f1(a):
    a +=1
    def f2(a):
        a +=1
        print(a)
    f2(a)
    print(a)

a = 1
f1(a) 
a -= 1
print(a)

# e.g. 1
def scope_test():
    def do_local():
        spam = "local spam"
        pass

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
        pass

    def do_global():
        global spam
        spam = "global spam"
        pass

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)