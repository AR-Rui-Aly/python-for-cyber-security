import hashlib


# getting the input from the user
     
def get_user_input():
     user_name = input("enter your user name: ")
     user_password = input("enter your user password: ")

     input_list = [user_name, user_password]
     return input_list


# encript the password o fthe user

def encrypt_pass(password):
     hashed_password = hashlib.sha256(password.encode()).hexdigest() 
     return hashed_password



#write on the file
def write_on_file(user_name, user_password):
     #freedie here is just a variable name I chose to hold the object.
     with open("data.txt", 'w') as freddie:
          freddie.write(f"user_name: {user_name}, user_password: {user_password}")



# join all the pieces together
          
def create_account():
     #acess the the second element of the list which will always be list in this context
     #also acess the user name to use later
     username, pas = get_user_input()
     
     #encrypt the retrived password from the list
     encrypted_pas = encrypt_pass(pas)


     #write pass the data into the file
     write_on_file(username, encrypted_pas)



#test our porcess_user_info funtion

create_account()
