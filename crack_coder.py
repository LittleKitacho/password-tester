# this is just used to encode and decode the passwords stored in output.txt
# for example, hdkbheehdkvoldkanbldkvnzo$B would be hello when decoded.

from random import choice

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~`!@#$%^&*()-_=+[{]}\\|;:'\",<.>/? "
length_id = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"

# encode function
def encode (decoded_str, length):
    if length > 52:
        #print("Set the length to 52")
        length = 52

    #print("Set encoded_str and i")
    encoded_str = ""
    i = 0

    while i <= len(decoded_str) - 1:
        encoded_str += decoded_str[i]
        print('encoding')

        if i == len(decoded_str) - 1:
            x = 0
            print('gibberish')

            while x < length:
                encoded_str += choice(chars)
                print('g')
                x += 1
        
        i += 1

    #print("Finished encoding")
    return encoded_str + length_id[length - 1]

def decode(encoded_str):

    length = length_id.index(encoded_str[-1]) + 1
    decoded_str = ""
    i = 0
    
    while i < len(encoded_str) - 1:
        decoded_str += encoded_str[i]
        #print(str(i))
        #print(encoded_str[i - 1])
        #print(encoded_str[i])
        #print(encoded_str[i + 1])
        #print('\n')
        i += length + 1

    return decoded_str