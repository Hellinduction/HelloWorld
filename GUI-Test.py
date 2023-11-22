import time
from hashlib import sha256

import PySimpleGUI as gui

import Utils
import main


def login():
    print("Login")
    window = gui.Window(title="Login",
                        layout=[[gui.Text("Login")], [gui.Multiline(key="username")], [gui.Text("Password")],
                                [gui.Multiline(key="password")], [gui.Button("Login")], [gui.Text("", key="error")]],
                        margins=(100, 50), button_color="GREEN",
                        background_color="BLACK")

    while True:
        event, values = window.read()

        if event == "Login":
            if len(main.accounts) == 0:
                values["error"] = "No accounts exist"

            username = values["username"].lower()
            # print(username)
            # print(main.accounts)
            acc = main.accounts.get(username)

            if acc is None:
                window["error"].update("No account exists under that username.")
                continue

            now = int(time.time())
            last_locked = acc.last_locked
            diff = now - last_locked
            unlocked_in = main.LOCK_TIME - diff

            if diff <= main.LOCK_TIME:  # 5 minutes
                window["error"].update("You are currently locked out of your account for failing to "
                                       "enter the password "
                                       "correctly too many times. Your account will be unlocked in "
                                       f"{unlocked_in} seconds.")
                continue

            password = acc.hashed_password
            salt = acc.salt

            p = sha256((values["password"] + salt).encode('utf-8')).hexdigest()

            # print(p, password)
            if p == password:
                account = acc
                window["error"].update(f"Its a match! Welcome back {account.proper_username}!")
                continue

            window["error"].update("Incorrect password.")
            acc.increment_failed_attempts()
            continue

        if event == gui.WIN_CLOSED:
            break


def signup():
    print("Signup")

    window = gui.Window(title="Signup",
                        layout=[[gui.Text("Sign up")], [gui.Multiline(key="username")], [gui.Text("Password")],
                                [gui.Multiline(key="password")], [gui.Button("Signup")], [gui.Text("", key="error")]],
                        margins=(100, 50), button_color="GREEN",
                        background_color="BLACK")

    while True:
        event, values = window.read()

        if event == gui.WIN_CLOSED:
            break

        if event == "Signup":
            proper_username = values["username"]
            username = proper_username.lower()

            if len(username) < 3:
                window["error"].update("Username is not long enough!")
                continue

            salt = Utils.getRandomString(32)
            password = sha256((values["password"] + salt).encode('utf-8')).hexdigest()

            storedHashForUsername = main.accounts.get(username)
            if storedHashForUsername is not None:
                window["error"].update("That user already exists.")
                continue

            main.account = main.Account(username, proper_username, password, salt)
            main.accounts[username] = main.account
            window["error"].update("Signed up!")
            main.save()
            main.load()
            window.close()
            start()
            break


def start():
    main.load()

    print("Starting program...")
    window = gui.Window(title="Application",
                        layout=[[gui.Text("Welcome!")], [gui.Button("Login")], [gui.Button("Signup")]],
                        margins=(100, 50), button_color="GREEN",
                        background_color="BLACK")

    while True:
        event, values = window.read()

        if event == "Login":
            window.close()
            login()
            break

        if event == "Signup":
            window.close()
            signup()
            break

        if event == gui.WIN_CLOSED:
            break

    main.save()
    main.load()


if __name__ == "__main__":
    start()
