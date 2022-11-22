import random


correct_char=[]
false_char=[]
mistake=0

words_bank=["hello","fish","clear","laptop","open","bike","flower","red","green"]

#x=random.randint(0,len(words_bank)-1)
words=random.choice(words_bank)

#words=random.choice(words_bank)

while(mistake<6):
    flag=1
    for i in range(len(words)):
        if words[i] in correct_char:
            print(words[i],end=" ")

        else :
            flag=0
            print('-',end=' ')

    if flag==1 :
        print()
        print("bravo! you win 🎉🎈👑")
        break

    print()

    user_char=input("enter your guess: ").lower()

    if len(user_char) == 1:
        if user_char in words:
            print("✅")
            correct_char.append(user_char)

        else:
            false_char.append(user_char)
            print("❌")
            mistake+=1

    else:
        print("enter one charecter!😐 ")

if mistake==6:
    print('"game over 💀"')
