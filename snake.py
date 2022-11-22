number=int(input("enter a number: "))
snake=[]

for i in range(1,number+1):

    if i%2==0:

        snake.append(str('#'))
        
    else:
        snake.append(str('*'))
    
print(''.join(snake[: :]))