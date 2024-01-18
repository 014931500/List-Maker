import random,string

letters = str(input("Press Enter Letters ? : "))
num = int(input("Press Enter Number :"))
domin = open("domains.txt",'r').read().splitlines()


for Enter_Email in domin:
    while 1:
        email= ''.join(random.choice(letters) for i in range(num))+ str(Enter_Email)
        if email[0] in string.digits:
            ''
        else:
            print(email+'\n')
            open('List-emails.txt','a').write(f'{email}\n')
