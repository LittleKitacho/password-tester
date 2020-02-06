import datetime

cpass = open('cpass.txt',"r").readlines()
wrd_dict = open('dict.txt',"r").readlines()

chars = "abcdefghijklmnopqrstuvwxyz"
capt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

kbd = ["`1234567890-=","qwertyuiop[]\\","asdfghjkl;'","zxcvbnm,./"," "]
sft = ["~!@#$%^&*()_+","QWERTYUIOP{}|","ASDFGHJKL:\"","ZXCVBNM<>?"," "]

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
    strength = len(password)
    x = 0

    while x < len(password) - 1:
        if password[x] == password[x + 1]:
            strength -= 1

        x += 1

    x = 0

    while x < len(password):

        is_sft = None
        kbd_index = None
        row_index = None

        for row in kbd:
            for char in row:
                if char == password[x]:
                    kbd_index = kbd.index(row)
                    row_index = row.index(password[x])
                    is_sft = False

        if is_sft == None:
            for row in sft:
                for char in row:
                    if char == password[x]:
                        kbd_index = sft.index(row)
                        row_index = row.index(password[x])
                        is_sft = True

        if is_sft:

            if password[x] == sft[kbd_index + 1][row_index]:
                strength -= 1

            elif password[x] == sft[kbd_index - 1][row_index]:
                strength -= 1

            elif password[x] == sft[kbd_index][row_index + 1]:
                strength -= 1

            elif password[x] == sft[kbd_index][row_index - 1]:
                strength -= 1

        else:

            if password[x] == kbd[kbd_index + 1][row_index]:
                strength -= 1

            elif password[x] == kbd[kbd_index - 1][row_index]:
                strength -= 1

            elif password[x] == kbd[kbd_index][row_index + 1]:
                strength -= 1

            elif password[x] == kbd[kbd_index][row_index - 1]:
                strength -= 1
        
        x += 1

    return strength

if __name__ == "__main__":
    passcode = input('Please give me a passcode to stress-test:  ')
    pass_str = test(passcode)
    print("Your password has a strength of " + str(pass_str))