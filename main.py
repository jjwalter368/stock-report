password = "79332021"
openPhrase = """
Welcome to Stock-Report v1.0.0
Made by Joshua Walter

Password: """


def run():
    if input(openPhrase) == password:
        print("You're in")
        # put the function that will ask for your stocks of the day to check

if __name__ == '__main__':
    run()