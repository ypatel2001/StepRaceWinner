#Yash's Code for Step Race Game Between Nicky and Byron, 2 fictional characters who are racing
#The problem was to code for a situation that intakes the number of steps the user gives for each
#character. It the ntakes the number of steps to end the race at and computes who wins. 

print("All inputed values must be between 1 and 10,000")
a= int(input("Please input number of steps Nicky takes forward: "))
b= int(input("Please input number of steps Nicky takes backward: "))
totalstepsN= 0
loopcountN= 0
nickypsn= 0
c= int(input("Please input number of steps Byron takes forward: "))
d= int(input("Please input number of steps Byron takes backward: ")) 
totalstepsB= 0
loopcountB= 0
byronpsn= 0
print("The value for s must be between 1 and 100,000")
s= int(input("Please input the total number of steps you want the game to end at: "))


while totalstepsN<s:
    loopcountN += 1
    totalstepsN+= a
    if totalstepsN<s:
        loopcountN += 1
        totalstepsN+=b
    if totalstepsN>s:
            x=totalstepsN-s
            totalstepsN-=x
            nickypsn-=x
print("Nicky's total steps: %d" %totalstepsN)
print("Nicky loops: %d" %loopcountN)
            

while totalstepsB<s:
    loopcountB += 1
    totalstepsB+= c
    if totalstepsB<s:
        loopcountB += 1
        totalstepsB+=d
    if totalstepsB>s:
            y=totalstepsB-s
            totalstepsB-=y
            byronpsn-=y
print("Byrons's total steps: %d" %totalstepsB)
print("Byron loops: %d" %loopcountB)

if loopcountN%2 == 0:
    for psn in range (int(loopcountN/2)):
        nickypsn+= a-b
    print("Nicky's position is: %d" %nickypsn)
else:
        nickypsn+=a
        for psn2 in range (int((loopcountN-1)/2)):
            nickypsn+= a-b
print("Nicky's position is: %d" %nickypsn)
    


if loopcountB%2 == 0:
    for psn3 in range (int(loopcountB/2)):
        byronpsn+= c-d
    print("Byron's position is: %d" %byronpsn)
else:
        byronpsn+=c
        for psn4 in range (int((loopcountB-1)/2)):
            byronpsn+= c-d
print("Byron's position is: %d" %byronpsn)

if nickypsn>byronpsn:
    print ("Nicky wins the game!")
if byronpsn>nickypsn:
    print ("Byron wins the game!")

if byronpsn==nickypsn:
    print("It is a tie!")
