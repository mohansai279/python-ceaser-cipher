alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def encryption(plain_text,shift_key):#hello h=7 shiftjey=3
    cipher_text=""
    for char in plain_text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position=(position+shift_key)%26 
            cipher_text+=alphabet[new_position]
        else:
            cipher_text+=char
            
    print(f" here's is the text after encryption {cipher_text}")
    
def decryption(cipher_text,shift_key):#hello h=7 shiftkey=3
    plain_text=""
    for char in cipher_text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position=(position-shift_key)%26 
            plain_text+=alphabet[new_position]
        else:
            plain_text +=char
    print(f" here's is the text after decryption {plain_text}")
    
wanna_end=False              
while not wanna_end: 
    what_to_do=input("Type 'encrypt' for encryption, Type 'decrypt' for decrption:")
    text=input("Type your Message:")
    shift=int(input("Type the Key number:"))
    if what_to_do=="encrypt":
        encryption(plain_text=text,shift_key=shift)
    elif what_to_do=="decrypt":
        decryption(text,shift)
    play_again=input("Type 'Yes' if you  Want to again other wise Type 'No':")
    if play_again=='no':
       wanna_end=True
       print("have a nice day!bye..")
       
