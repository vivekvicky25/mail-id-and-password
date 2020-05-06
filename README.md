# Create a password

def create_password():
    mail_id = input("Enter your Email I'd :")
    password = input('Enter your Password :')
    confirm_password = input('Confirm your Password :')
    
    while password != confirm_password:
        print("Your Password does not match")
        confirm_password = input('Re-Enter your confirmation Password :')
    else:
        print('You have sucessfully created your account')
        
        
create_password()
