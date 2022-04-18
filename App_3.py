Progress_count=0
trailer_count=0
retriever_count=0
Exclude_count=0
def histogram():
    global Progress_count,trailer_count,retriever_count,Exclude_count
  
    print("\n\nProgress Trailer Retriever Exclude")
    while Progress_count+ trailer_count+ retriever_count + Exclude_count !=0:
        if Progress_count !=0:
            print("  * ",end="      ")
            Progress_count-=1
        else: 
            print("   ",end='       ')
        if trailer_count !=0:
            print(" * ",end='       ')
            trailer_count-=1
        else:
            print("   ",end='       ')
        if retriever_count !=0:
            print(" * ",end='       ')
            retriever_count-=1
        else:
            print("   ",end='       ')
        if Exclude_count!=0:
            print(" * ",end='       ')
            Exclude_count-=1
        else:
            print("   ",end='       ')

        print()

    print()





def range_integer_error(credit_name):
    while True:
        try:
            global credit
            global x
            credit_str=input(f"credit at each level {credit_name}:")
            credit=int(credit_str)
            if(credit%20 or credit>120):
                print('Range Error')
            else:
                x=None
                break
        except:
           
            
            if credit_str.lower()=="q":
                x="q"
                break
            else:
                print("interger requird")
                x=None
                continue

    
while True:
    range_integer_error("pass")
    if x:
        break
    pass1=credit
    range_integer_error("defer")
    if x:
        break
    defer=credit
    range_integer_error("fail")
    if x:
        break
    fail=credit

    if(pass1+defer+fail!=120):
        print("total incorrect")

            
    elif(pass1==120):
            print("Progress")
            Progress_count=Progress_count+1
    elif(pass1==100):
            print("Progress-module trailer")
            trailer_count=trailer_count+1
    elif(fail<=60):
            print("Do not Progress-module retriever")
            retriever_count=retriever_count+1
    elif(fail>=80):
            print("Exclude")
            Exclude_count=Exclude_count+1


histogram()
