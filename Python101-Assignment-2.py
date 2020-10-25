Database={
    'eddygrant':{
        'name': 'Sachin',
        'age':22,
        'email':'eddyXXXXgmail.com',
        'password':'red@123',
        'amount':20000
    },
    'sachin':{
        'name':'Tanuj',
        'age':25,
        'email':'tanuj@gmail.com',
        'password':'red@123',
        'amount':10000
    }
}
while(Database!=''):
    x=int(input("Enter your Choice: \n 1.Sign in \n 2.Sign Up \n 3.Exit: "))
    if(x==1):
        username=input("Enter user name: ")
        if((username in Database)==True):
            password=input("Enter password: ")
            if((password in Database[username]['password'])==True):
                print("Welcome",Database[username]['name'])
                while(Database!=''):
                    x=int(input('''Enter your Choice:
                    1. Check Balance
                    2. Deposit Balance
                    3. Withdrawl
                    4. Change Password
                    5. Log out    '''))
                    if(x==1):
                        print('Current Balance:',Database[username]['amount'])
                    elif(x==2):
                        depositamt=int(input("Enter amount: "))
                        Database[username]['amount']=Database[username]['amount']+depositamt
                    elif(x==3):
                        withdrawlamt=int(input("Enter amount: "))
                        print("Collect your Cash ",withdrawlamt)
                        Database[username]['amount']=Database[username]['amount']-withdrawlamt
                    elif(x==4):
                        while(Database!=''):
                            password=input("Enter old password:")
                            if(password==Database[username]['password']):
                                temp_pswd=eval(input("Enter new password:"))
                                Conf_pswd=eval(input("Enter confirm new password:"))
                                if(temp_pswd==Conf_pswd):
                                    Database[username]['password']=temp_pswd
                                    print("Password successfully changed")
                                    break
                                else:
                                    print("Password not matched")
                            else:
                                print("Enter password correctly")
                    elif(x==5):
                        break
            elif((password in Database[username]['password'])==False) :
                print('Forgot password')
                email=input( 'Enter the email:')
                if((email in Database[username]['email'])==True):
                    Database[username]['password']=input('New password:')
                    print("Password successfully changed")		    
        else:
            print("Username is Not Found")
    elif(x==2):
        username=eval(input("Enter your username: "))
        name=eval(input("Enter your name: "))
        age=eval(input("Enter your age: "))
        email=eval(input("Enter your email: "))
        password=eval(input("Enter your password: "))
        amount=eval(input("Enter your amount: "))
        Database[username]={'name':name,'age':age,'email':email,'password':password,'amount':amount}
        print("Username successfully created")
    elif(x==3):
        break
