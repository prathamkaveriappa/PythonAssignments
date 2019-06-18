Start = int(input("Enter Start: "))
End = int(input("Enter End: "))
for i in range(Start, End + 1): 
   if i > 1: 
       for n in range(2, i): 
           if (i % n) == 0: 
               break
       else: 
           print(i) 