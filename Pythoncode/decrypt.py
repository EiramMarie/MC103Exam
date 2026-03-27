
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
ciphertext = "ZA z9 TcVmVi A5 3zE kyz4x9 r SzA sF vE6r4uz4x R26yrsvA r4u ruuz4x 4B3sv89"

for shift in range(62):
    result = ""
    for char in ciphertext:
        if char in alphabet:
            index = alphabet.index(char)
            new_index = index + shift

            if new_index >= len(alphabet):
                new_index = new_index - len(alphabet)

            result = result + alphabet[new_index]
        else:
            result = result + char
    print("Shift", shift, ":", result)