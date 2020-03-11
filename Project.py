def display():
    'This  function will dislplay the table of mastermind game.'
    for i in range(10):
        print('___________________')
        print(breaker[i][0],breaker[i][1],breaker[i][2],breaker[i][3],('|'),hint[i][0],hint[i][1], hint[i][2],hint[i][3],'|')
    print('\nYou have',index+1,'Turns left!\n')
def check(a,b,c,d):
    'This function will check for double number enteries and range of numbers.'
    lis=[]
    lis.append(a)
    lis.append(b)
    lis.append(c)
    lis.append(d)
    for i in lis:
        a=lis.count(i)
        if(a>1):
            return True
        if(i>7 or i<=0):    
            return False

def append(a,b,c,d):
    'this function will fill the rows of the game. and will also give the hint'
    global index
    breaker[index][0]=a
    breaker[index][1]=b
    breaker[index][2]=c
    breaker[index][3]=d   
    for member in range(4):
        if(maker.get(member+1)==breaker[index][member]):
            hint[index][member]=9
        else:
            stor=member                 #this variable is used to store the itation of first for loop as it will be changing in the last for loop.
            for r in range(1,5):
                if(breaker[index][stor]==maker.get(r)):
                    hint[index][stor]=8
                    break
                member+=1 
            member=stor   
    index-=1

def Winner():
    'Checks the winning condition of the user whether the code is guessed right or not.'
    check=[9]*4
    if(hint[index+1]==check):
        return True

####        Main program starts from here..#######

import random,os,datetime,time
sample={1:1,2:2,3:3,4:4,5:5,6:6,7:7}                                               #This is the ditionary of the code maker.
breaker=[[' ']*4,[' ']*4,[' ']*4,[' ']*4,[' ']*4,[' ']*4,[' ']*4,[' ']*4,[' ']*4,[' ']*4]       #this is what the user will be going to enter.
hint=[[' ']*4,[' ']*4,[' ']*4,[' ']*4,[' ']*4,[' ']*4,[' ']*4,[' ']*4,[' ']*4,[' ']*4]      #This is hint  for given input and will be updated again and again.
maker={}
lis=list(sample.values())   #To shuffle the dictionary i will convert the dictionary values into the list,shuffle it and then again will make it dictionary.
random.shuffle(lis)
for i in range(1,5):
    maker.update({i:lis[i-1]})
index=9     

dateandtime=datetime.datetime.now()
name=input('Player please enter Your name! ')
file=open('F:\Record.txt','a')                          #player data appending in the file, score and other data will be appended later!
file.write('\n'+'*'*50)
file.write('\nstarting time:\t'+str(dateandtime)+'\nPLayer Name:\t'+name)
file.close()

## Welcoming to the game

print('Welcome',name,'!\nHere are some rules that you need to remember')
time.sleep(2)
print('Computer will generate the 4 digits code which you have to break out of 7 colours hint will also be given.\n\n Here "8" will stand for the right colour but in wrong position \nwhile the "9" stands for the right colour in right posiiton.')
time.sleep(4)
print('\nYour score will depend on how many turns you have taken\n\nComputer has generated the code  succesfuly.\nWe wish you best of luck!')
print()
print('Your starting date and time is',dateandtime)
while(index>-1):
    while True:
        try:
            a,b,c,d=eval(input('Please enter 4 numbers(1,2,3,4,5,6,7)not be repeatable: ')   )
            ch=check(a,b,c,d)
            if(ch==True):
                print()
                print('You have entered a number twice Please try again!')
                print()
                continue
            if(ch==False):
                print()
                print('You are required to enter the digits in between 1 and 7!')
                print()
                continue
            break
        except:
            print()
            print('Sorry! you have entered wrong values. try again!')
            print() 
    os.system('cls')
    append(a,b,c,d)
    display()
    print()
    win=Winner()
    if(win==True):
        score=(index+1)*10
        dateandtime=datetime.datetime.now()
        file=open('F:\Record.txt','a')
        file.write('\nResult:\t\t'+name+' Won!\nscore:\t\t'+str(score)+'\nTurns left:\t'+str(index)+'\nEnding time:\t'+str(dateandtime))
        file.close()
        print('Your Score is',score)
        print('Congratulations! You Won and have beaten the PC successfully!')
        exit()
    
print('\nGame Over!!\n\nBad_day Friend!\n\n You lost to Computer!')
dateandtime=datetime.datetime.now()
print('Your ending date and time is',dateandtime)
file=open('F:\Record.txt','a')
file.write('\nResult:\t\t'+name+' Lost!'+'\nScore\t\t0'+'\nEnding time:\t'+str(dateandtime))
file.close()