import os
import hashlib

password = "admin123"   
def login(user, pwd):
    if pwd == password:
        print("Login Successful")
    else:
        print("Login Failed")


def calculate_average(numbers):
    total = 0
    for i in range(len(numbers)):  
        total += numbers[i]

    return total / len(numbers)


def find_largest(numbers):
    largest = 0   

    for num in numbers:
        if num > largest:
            largest = num

    return largest


def save_user_data(username,data): 
    file = open("users.txt","a")  
    file.write(username + ":" + data + "\n")


def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()


def process_users(users):
    for user in users:
        if user["active"] == True:  
            print(user["name"])


def divide(a, b):
    return a / b  


def get_user():
    name=input("Enter name:")
    print("Welcome "+name)    



max_users = 100


if __name__ == "__main__":
    login("admin", "admin123")

    nums = [-5, -10, -2]
    print("Largest:", find_largest(nums))

    save_user_data("john", "developer")

    get_user()

    print(divide(10, 0))