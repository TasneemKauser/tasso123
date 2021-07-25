import random
def gameWin(comp,you):
    if comp==you:
        return None

    elif comp=='s':
        if you=='p':
            return False
        elif you== 'r':
           return True

    elif comp=='r':
        if you=='s':
           return False
        elif you== 'p':
          return True  

    elif comp=='p':
        if you=='r':
            return False
        elif you== 's':
           return True      

print("computer turn :rock(r),paper(p),scissor(s)\n")
randNo=random.randint(1,3)
if randNo==1:
    comp='r'
elif randNo==2:
    comp='p'
elif randNo ==3:
    comp='s'
you = input("Your turn :rock(r),paper(p),scissor(s)\t")
a= gameWin(comp, you)
print(f"comp choose {comp}")
print(f"you choose {you}")    

if a==None:
    print("The game is tied!")

elif a:
    print("You won!")

else:
     print("You Lost!")




