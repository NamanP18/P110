import random

responce='y'
while responce=='y':
    yes=random.randint(1,6)
    if yes==0:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")

    if yes==1:  
        print("[-----]")
        print("[     ]")
        print("[  1  ]")
        print("[     ]")
        print("[-----]")

    if yes==3:
        print("[-----]")
        print("[     ]")
        print("[  2  ]")
        print("[     ]")
        print("[-----]")

    if yes==4:
        print("[-----]")
        print("[     ]")
        print("[  3  ]")
        print("[     ]")
        print("[-----]")

    if yes==4:
        print("[-----]")
        print("[     ]")
        print("[  4  ]")
        print("[     ]")
        print("[-----]")
    
    if yes==5:
        print("[-----]")
        print("[     ]")
        print("[  5  ]")
        print("[     ]")
        print("[-----]")
    
    if yes==6:
        print("[-----]")
        print("[     ]")
        print("[  6  ]")
        print("[     ]")
        print("[-----]")

    YN=input('Press y to roll the dice and n to not: ')
    print('\n')


