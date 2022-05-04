import time
initial = time.time()
print(initial)



# initial1 = time.time()
# a = 0
# while a<40:
#     print('This is Shrey Thakkar')
#     a = a+1
# print(f'While loop took {time.time() - initial1} seconds')

# initial2 = time.time()
# for b in range(40):
#     print('This is Shrey Thakkar')
# print(f'for loop took {time.time() - initial2} seconds')




'''Print current time, day and date'''
# import time 
# localtime = time.asctime(time.localtime(time.time()))
# print(localtime)



'''time.sleep()'''

# time.sleep(2) 
import time
initial2 = time.time()
for b in range(40):
    print('This is Shrey Thakkar')
    time.sleep(2)  # --> it will print the command after every 2 second
    