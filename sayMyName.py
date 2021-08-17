#Enter your SID number
ntime = input('Enter your Studnet ID.')
#Enter your name to be printed
name = input('Please type in your name.')
#initialize i
i = 0
#create a range for the amount of times your name will be printed
times = int(ntime[0:2])
#using a while loop print your name for the amount of times set in range
while i < times:
    print(name)
    #increment i after every time the name is printed
    i += 1
