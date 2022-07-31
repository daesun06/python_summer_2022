message = input("Enter a message to encode or decode: ")
message = message.upper()
key = eval(input("How many letters are we going to shift (1-26): "))
output = ""
for letter in message:
    if letter.isupper():
        value = ord(letter) + key
        letter = chr(value)
        if not letter.isupper():
            value -= 26 
            letter = chr(value)
    output += letter
print("Output message: ", output)

# To decode substract your custom key from 26 (26 - key)