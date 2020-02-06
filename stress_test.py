from math import floor

cpass = open('cpass.txt',"r").readlines()
wrd_dict = open('dict.txt',"r").readlines()

chars = "abcdefghijklmnopqrstuvwxyz"
capt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

num = "1234567890"
sym = "`~!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?"

kbd = ["`1234567890-=","qwertyuiop[]\\","asdfghjkl;'","zxcvbnm,./"," "]
sft = ["~!@#$%^&*()_+","QWERTYUIOP{}|",'ASDFGHJKL:"',"ZXCVBNM<>?"," "]

def test(password: str) -> int:

    # Check if password is a common password
    for i in cpass:
        if password == i.strip():
            return 0

    # Check if password is a single word in the dictionary
    for i in wrd_dict:
        if password == i.strip():
            return 0

    # Password's strength is defined
    strength = len(password) * 2
    x = 0
    y = 0

    for i in password:
        if i in num:
            x += 1
        elif i in sym:
            y += 1

    if x >= floor(len(password) / 4):
        strength += len(password)
    
    if y >= floor(len(password) / 4):
        strength += len(password)

    x = 0

    while x < len(password) - 1:
        if password[x] == password[x + 1]:
            strength -= 2

        x += 1

    x = 0

    while x < len(password) - 1:

        captial = None

        if password[x] in chars:

            char = chars.index(password[x])
            capital = False
        
        elif password[x] in capt:

            char = chars.index(password[x])
            capital = True

        if captial:
            
            if char < len(capt) - 1:

                if password[x + 1] == capt[char + 1]:
                    strength -= 1

                elif password[x + 1] == capt[char + 1]:
                    strength -= 1

                elif password[x + 1] == chars[char]:
                    strength -= 1

        elif not capital:

            if char < len(capt) - 1:

                if password[x + 1] == chars[char + 1]:
                    strength -= 1

                elif password[x + 1] == chars[char + 1]:
                    strength -= 1

                elif password[x + 1] == capt[char]:
                    strength -= 1

        x += 1

    return strength

if __name__ == "__main__":
    passcode = input('Please give me a passcode to stress-test:  ')
    pass_str = test(passcode)
    print("Your password has a strength of " + str(pass_str))