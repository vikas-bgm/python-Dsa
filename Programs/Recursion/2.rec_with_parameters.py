#recursion using parameters
#suppose I want to print x n number of times (x=15,n=4)

def func_name(x,n):
    if n== 0:
        return
    print(x)
    func_name(x,n-1)

func_name(15,4)