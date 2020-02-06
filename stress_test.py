import datetime

cpass = open('cpass.txt',"r").readlines()
wrd_dict = open('dict.txt',"r").readlines()

chars = "abcdefghijklmnopqrstuvwxyz"
capt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

kbd = ["`1234567890-=","qwertyuiop[]\\","asdfghjkl;'","zxcvbnm,./"," "]
sft = ["~!@#$%^&*()_+","QWERTYUIOP{}|","ASDFGHJKL:\"","ZXCVBNM<>?"," "]

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

    x = 0

    while x < len(password):

        sft = None
        kbd_index = None
        row_index = None

        for row in kbd:
            for char in row:
                if l == password[x]:
                    kbd_index = kbd.index(i)
                    row_index = l.index(password[x])
                    sft = False

        if kbd_index == None:
            for i in sft:
                for l in i:
                    if l == password[x]

    return strength

if __name__ == "__main__":
    passcode = input('Please give me a passcode to stress-test:  ')
    pass_str = test(passcode)
    print("Your password has a strength of " + str(pass_str))