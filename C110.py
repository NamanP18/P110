import time
seconds = input("Enter the number of seconds: ")
def count_down(seconds):
    while seconds>0:
        mins = int(seconds/60)
        sec = int(seconds%60)
        timer = f'{mins}:{sec}'
        #print(timer)
        print(timer,end="\r")
        time.sleep(1) 
        seconds=seconds-1
    print("Times Up!!!")

count_down(int(seconds))

