
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
ciphertext = "Teu cgeno jmsvr hlz dghqi kref xup oete ayo"

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