#print 1 to N with Recursion

def func(i,n):
    if i > n:
        return
    print(i)
    func(i+1,n)         # Tail recursion
func(1,10)

#suppsoe if we want to print the reverse use head recursion,

'''Head Recursion
def func(i,n):
    if i > n:
        return
    func(i+1,n)
    print(i)
def(1,10)
O/P-- > 10 9 8 7 6 5 4 3 2 1
'''