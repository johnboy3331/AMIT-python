import calco as c
run=True
while(run):
    op=input("Enter an operation : add, sub, mult or div")
    num=input("Enter two numbers")
    n1,n2=num.split()
    if op=="add":
        res=c.add(n1,n2)
    elif op=="sub":
        res=c.sub(n1,n2)
    elif op=="div":
        res=c.div(n1,n2)
    elif op=="mult":
        res=c.mult(n1,n2)
    print(res)
    f= input("Would like to make another operation? yes or stop")
    if f=="stop":
        run=False