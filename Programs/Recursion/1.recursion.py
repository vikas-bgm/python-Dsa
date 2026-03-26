# print the name n number of times

count = 0

def func_name():
    global count
    if count == 6:
        return
    count+= 1
    func_name()
    print("Hello world")
    
func_name()
    