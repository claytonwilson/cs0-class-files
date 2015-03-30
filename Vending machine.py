def vendingmachine(choice, money):
    change = 0
    money = int(money)
    watervartest = 'water'
    cokevartest = 'coke'
    spritevartest = 'sprite'
    options = ['coke', 'sprite', 'water'] 
    cost = [2, 3, 1]
    if choice not in options:
        print 'That is not an option. Please try again.'
    elif choice == cokevartest and money >= cost[0]: 
        change = money - 2
        print 'Here is your Coke' 
        print 'Your change is',change,'$'
    elif choice == spritevartest and money >= cost[1]: 
        change = money - 3
        print 'Here is your Sprite'
        print 'Your change is',change,'$'
    elif choice == watervartest and money >= cost[2]: 
        change = money - 1
        print 'Here is your Water'
        print 'Your change is',change,'$'
    elif choice == cokevartest and money < cost[0]:
        print 'Please enter more money'
    elif choice == spritevartest and money < cost[1]:
        print 'Please enter more money'
    elif choice == watervartest and money < cost[2]:
        print 'Please enter more money' 
    else:
        print 'You have broken something please try again'





        
        



