msg = input("Enter a message to encrypt: ")
encmsg = ""
for ch in msg:
    asc = ord(ch) + 3
    ench = chr(asc)
    encmsg += ench
    encmsg = encmsg[::-1] #for string reversal
print("Encrypted message: " + encmsg)
