plaintext = input("Please enter a phase to be encrypted: ")

cyphertext = ""
while len(plaintext) > 0:
    char = plaintext[-1]
    cypherchar = chr(ord(char) + 1)
    cyphertext = cyphertext + cypherchar
    plaintext = plaintext[:-1]

print (cyphertext)

cyphertext = input("Please enter a phrase to be decrypted: ")

plaintext = ""
while len(cyphertext) > 0:
    cypherchar = cyphertext[-1]
    char = chr(ord(cypherchar) - 1)
    plaintext = plaintext + char
    cyphertext = cyphertext[:-1]

print (plaintext)
