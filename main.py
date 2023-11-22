import json
import os.path
import random
import time
from hashlib import sha256

import Utils

LOCK_TIME = 300  # Time an account is locked when password is failed after so many times

# Account
# passwords = []
accounts = {}
account = None

# Files
path = "accounts.json"


def toAccount(acc):
    if isinstance(acc, Account):
        return acc

    return Account(**acc)


class Account:
    def __init__(self, username, proper_username, hashed_password, salt, last_locked=0, failed_attempts=0):
        self.username = username
        self.proper_username = proper_username
        self.hashed_password = hashed_password
        self.salt = salt
        self.last_locked = last_locked
        self.failed_attempts = failed_attempts

    def lock(self):  # Locks the account for 5 minutes
        self.last_locked = int(time.time())
        self.failed_attempts = 0

    def increment_failed_attempts(self):
        self.failed_attempts = self.failed_attempts + 1

        if self.failed_attempts > 3:
            self.lock()

    def to_dict(self):
        return {
            'username': self.username,
            'proper_username': self.proper_username,
            'hashed_password': self.hashed_password,
            'salt': self.salt,
            'last_locked': self.last_locked,
            'failed_attempts': self.failed_attempts
        }


def save():
    global path
    global accounts

    file = None

    if os.path.isfile(path):
        file = open(path, 'w')
    else:
        file = open(path, 'x')
        file.close()
        file = open(path, 'w')

    accs = {}

    for username in accounts.keys():
        obj = accounts[username]

        if isinstance(obj, dict):
            accs[username] = obj
        else:
            accs[username] = accounts[username].to_dict()

    json.dump(accs, file, indent=4)
    file.close()


def load():
    global path
    global accounts

    if os.path.isfile(path):
        file = open(path, 'r')
        accs = dict(json.load(file))

        for username in accs.keys():
            accounts[username] = toAccount(accs[username])

        file.close()


def fun():
    pos = 0

    while True:
        spaces = ""

        for i in range(pos):
            spaces += " "

        print(f"{spaces}{Utils.getRandomColor()}.")

        rand = random.randint(-1, 1)
        if pos < 1:
            rand = 1

        pos += rand
        time.sleep(1)


def flow1():
    print(Utils.formatColor("Welcome to %s where it asks you overly personal questions %s!", "Epic Gamer Program", "G"))
    name = input("Name? ")
    age = int(input("How old are you? "))

    confirm = Utils.toBool(input("What you like to provide additional info? "))

    town = None
    favColor = None
    lastName = None

    if confirm:
        town = input("What town do you reside in? ")
        favColor = input("What is your favourite color? ")
        lastName = input("What is your last name? ")

    print(Utils.formatColor("Your name is %s!\nYou are %s years old!", name, age), sep="")

    if confirm:
        print(Utils.formatColor("You are from %s!", town))
        print(Utils.formatColor("Your favourite color is %s!", favColor))
        print(Utils.formatColor("Your last name is %s!", lastName))

    animation = Utils.toBool(input("Do you hate yourself? "))
    if animation:
        fun()


def flow2():
    load()
    add = Utils.toBool(input(Utils.formatColor("Would you like to login? ")))

    if add:
        login()
    else:
        signup()

    save()
    load()
    exit()


def login():
    global accounts
    global account

    if len(accounts) == 0:
        print("No accounts exist!")
        exit()

    username = input(Utils.formatColor("Enter your username: ")).lower()

    acc = accounts.get(username)
    if acc is None:
        print(Utils.formatColor("No account exists under that username."))
        exit()

    now = int(time.time())
    last_locked = acc.last_locked
    diff = now - last_locked
    unlocked_in = LOCK_TIME - diff

    if diff <= LOCK_TIME:  # 5 minutes
        print(Utils.formatColor("You are currently locked out of your account for failing to enter the password "
                                "correctly too many times. Your account will be unlocked in %s seconds.", unlocked_in))
        exit()

    password = acc.hashed_password
    salt = acc.salt

    p = sha256((input(Utils.formatColor("Enter your password: ")) + salt).encode('utf-8')).hexdigest()

    if p == password:
        account = acc
        print(Utils.formatColor("Its a match! Welcome back %s!", account.proper_username))
        return

    print(Utils.formatColor("Passwords do not match! Fix it RIGHT NOW!11"))
    acc.increment_failed_attempts()


def signup():
    global accounts
    global account

    proper_username = input(Utils.formatColor("Enter a username: "))
    username = proper_username.lower()

    salt = Utils.getRandomString(32)
    password = sha256((input(
        Utils.formatColor("Set your password: ")) + salt).encode(
        'utf-8')).hexdigest()  # Probably shouldn't hash actual passwords like this but good enough for this :)

    storedHashForUsername = accounts.get(username)
    if storedHashForUsername is not None:
        print(Utils.formatColor("That user already exists."))
        exit()

    account = Account(username, proper_username, password, salt)
    accounts[username] = account
    print(Utils.formatColor("Thank you for signing up with username %s and hashed password %s.", proper_username, password))


if __name__ == "__main__":
    flow2()
