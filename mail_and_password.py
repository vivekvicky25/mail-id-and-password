
mail= "vivek@gmail.com"
pwd  = "vivek"

# User id and password , correct 
# User id correct , password 
# User id wrong
# User id correct , in 2nd attempt , 3rd attemp 


for no_of_attempts in range(3):
    email = input("Enter email id ? ")
    if email == mail:
        for no_of_pass in range(3):
            password = input("Enter password ?")
            if password == pwd:
                print("You have logged in succesfully !")
                exit()
            else:
                print("Incorrect password")
        print("Exceeded to many tries!")
        exit()
