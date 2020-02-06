import datetime

cpass = open('cpass.txt',"r").readlines()
wrd_dict = open('dict.txt',"r").readlines()

def test(password: str) -> int:
    for i in cpass:
        if password == i.strip():
            return 0
    
    for i in wrd_dict:
        if password == i.strip():
            return 0

    strength = len(password)
    x = 0

    while x < len(password) - 1:
        if password[x] == password[x + 1]:
            strength -= 1

        x += 1

    return strength

if __name__ == "__main__":
    passcode = input('Please give me a passcode to stress-test:  ')
    pass_str = test(passcode)
    print("Your password has a strength of " + str(pass_str))