import argparse

def decrypt_string(string, length):
    counter = 0 #local_4h
    local_18 = 0
    local_1c = 0
    new_string = ''
    while counter < length:
        if not local_18 == 1:
            letter = string[counter]
            if not letter == ' ':
                new_string += chr(ord(letter)+1)
        else:
            letter = string[counter]
            if not letter == ' ':
                new_string += chr(ord(letter)-1)
        counter += 1
        local_18 += 1
        if local_18 > 2:
            local_18 = 0

    return new_string

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('string', help='String we want to decrypt')
    args = parser.parse_args()
    decrypt_string(args.string, len(args.string))
