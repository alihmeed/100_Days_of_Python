print("++++++++++++")
print("LOGIN SYSTEM")
print("++++++++++++")
print()

username = input("Username: ")
password = input("Password: ")

if username == "Ali" and password == "12345":
    print("\033[32m"
          "Welcome,", username + "!"
          "\033[0m")

elif username == "Mark" and password == "password":
    print("\033[32m"
          "Welcome,", username + "!"
          "\033[0m")

elif username == "Sara" and password == "abc123":
    print("\033[32m"
          "Welcome,", username + "!"
          "\033[0m")

else:
    print("\033[31m"
          "Unauthorized Access.."
          "\033[0m")
