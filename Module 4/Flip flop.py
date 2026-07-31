#Function to check whether palindrome or flip flop or not
def palind(r):
    end = len(r) - 1
    start = 0
    while (start<end):
        if (r[start] != r[end]):
            return False
        start += 1
        end -= 1
    return True
    # return r = [::-1]

r = (1,2,4,3,2,1)

if palind(r):
    print("The tuple is a flip flop!!")
else:
    print("The tuple is not a flip flop :(")
