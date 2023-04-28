name=input("Enter your name: ")
print(f"Hi {name}! Welcome to the New Adventure")

Path=input('''You have three Directions to go Left,Right and Straight ahead.
            so where you want to go? ''')
if Path=="left" :
    left=input('''Thre is a DownHill on this path,it might be dangerous
            to go there. If you want to go press "Yes": ''')
    if left=="yes":
        print("You fell from the hill, you are dead")
elif Path=="right":
    right=input('''The right side path might br good but there is
                    always a chance of Crocodiles b/c it is moving
                        by the river.If you still want to select it 
                            press "Yes": ''')
    if right=="yes":
        print("OH man: You have been eaten by a Crocodile.")
elif Path=="straight":
    straight=input('''Welcome to the World of mountains "HIMALIYAS". 
                    Left side "Lake" Right side "Mountain area": ''')
    if straight=="left":
        print("Enjoy the of Neelum Lake.It is Beautiful")
        s=input('''got tired,"Yes/No": ''')        
        if s=="yes":
            i=input('''Ok sir. Sould we take you back to your hotel
                OR you wanna go to the mountain area: ''')
            if i=="mountain":
                print("Now you are going to the Himalayas")
                print("Enjot the view and go for hiking")
            else:
                print("You are going back to your hotel.Take some Rest")
