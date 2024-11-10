import sys
sys.path.append("C:/Users/atuls/OneDrive/Desktop/project.p1.py")
from p1 import*
print(responses[0])
print(responses[1])

while True:
   text=input("Please Ask:")
   for w in text.split():
       if w.upper() in operations.keys():
         try:
           l=extract_num(text)
           r=operations[w.upper()](l[0],l[1])
           print(r)
           break

         except:
             print("Please ask correct Questions")
             break

       elif w.upper()in commands.keys():
            commands[w.upper()]()
            break


       else:
        print(responses[5])
        print(responses[4])
