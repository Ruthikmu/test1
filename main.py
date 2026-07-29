import hashlib
import os

PASSWORD = "admin123"
users = {}

def login(username, password):
    if password == PASSWORD:
        print("Login successful")
        return True
    return False

def register(username, password):
    users[username] = password

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def read_file(filename):
    f = open(filename)
    data = f.read()
    return data

def save_file(filename, data):
    f = open(filename, "w")
    f.write(data)

def find_user(username):
    for key in users.keys():
        if key == username:
            return users[key]
    return None

def search_items(items, target):
    result = []
    for i in items:
        for j in items:
            if i == target:
                result.append(i)
    return result

class Database:
    def connect(self):
        print("Connected")

class UserService:
    def __init__(self):
        self.db = Database()

    def create(self, username, password):
        self.db.connect()
        register(username, password)

def calculate_average(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)

def delete_user(username):
    del users[username]

def execute(command):
    os.system(command)

service = UserService()
service.create("alice", "password123")

print(login("alice", "admin123"))
print(hash_password("password123"))
print(read_file("config.txt"))
print(search_items([1, 2, 3, 4], 3))
print(calculate_average([]))
execute(input("Command: "))
