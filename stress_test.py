import datetime

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~`!@#$%^&*()-_=+[{]}\\|;:'\",<.>/? "

def test (password: str) -> int:
    x = len(password) - 1
    strength = 0

    while x >= 0:
        diff = x - len(password)
        strength += chars.index(password[x]) * (10 ^ diff)
        x -= 1

    return strength * -1


if __name__ == "__main__":
    print("Password strength: " + str(test(input('Please give me a password to stress test:  '))))