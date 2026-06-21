import hashlib

password = "admin123"

def login(user,pwd):
    if pwd == password:
        print("Login Successful")
    else:
        print("Login Failed")

def find_largest(numbers):
    largest = 0
    for num in numbers:
        if num > largest:
            largest = num
    return largest

def save_data(name,data):
    file = open("users.txt","a")
    file.write(name + ":" + data + "\n")

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

nums = [-5, -10, -2]

login("admin", "admin123")
print(find_largest(nums))
save_data("john","developer")
print(hash_password("mypassword"))