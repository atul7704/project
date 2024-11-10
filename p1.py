responses=["Hello,my name is robot","What may i help you?","Thank you","Bye-Bye","Sorry,I don't know","But next time surely I will do for you"]
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

def end():
    print(responses[2])
    print(responses[3])

def extract_num(text):
    l1=[]
    for w in text.split():
        try:
            l1.append(float(w))

        except:
            pass
    return l1

def ajay():
    print("Ajay is a student of RAJKIYA ENGINEERING COLLEGE SONBHADRA,he is in 4th year of Engineering")

operations={"ADDITION":add,"SUM":add,"PLUS":add,"SUB":sub,"MINUS":sub}
commands={"AJAY":ajay,"BYE BYE":end,"EXIT":end}
