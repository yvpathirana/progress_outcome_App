
def range_integer_error(credit_name):
    while True:
        try:
            global credit
            credit=int(input(f"credit at each level {credit_name}:"))
            if(credit%20 or credit>120):
                print('Range Error')
            else:
                return credit
        except:
            print("interger requird")
            continue
while True:
    pass1=range_integer_error("pass")
    defer=range_integer_error("defer")
    fail=range_integer_error("fail")
    

    if(pass1+defer+fail!=120):
        print("total incorrect")

            
    elif(pass1==120):
        print("Progress")
        break
    elif(pass1==100):
        print("Progress-module trailer")
        break
    elif(fail<=60):
        print("Do not Progress-module retriever")
        break
    elif(fail>=80):
        print("Exclude")
        break
