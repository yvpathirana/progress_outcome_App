Progress_count=0
trailer_count=0
retriever_count=0
Exclude_count=0
def result_maker():
    global Progress_count,trailer_count,retriever_count,Exclude_count
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
data=[
    {"pass1":120,"defer":0,"fail":0},
    {"pass1":100,"defer":20,"fail":0},
    {"pass1":100,"defer":0,"fail":20},
    {"pass1":80,"defer":20,"fail":20},
    {"pass1":60,"defer":40,"fail":20},
    {"pass1":40,"defer":40,"fail":40},
    {"pass1":20,"defer":40,"fail":60},
    {"pass1":20,"defer":20,"fail":80},
    {"pass1":20,"defer":0,"fail":100},
    {"pass1":0,"defer":0,"fail":120}
    ]
for i in data:
    pass1,defer,fail=i['pass1'],i['defer'],i['fail']
    result_maker()
    

print("Progress",Progress_count," :",end="")
for i in range(Progress_count):
    print('*',end="")

print("\n"+"trailer",trailer_count,"  :",end="")
for i in range(trailer_count):
    print('*',end="")
print("\n"+"retriever",retriever_count,":",end="")
for i in range(retriever_count):
    print('*',end="")
print("\n"+"Exclude",Exclude_count,"  :",end="")
for i in range(Exclude_count):
    print('*',end="")
