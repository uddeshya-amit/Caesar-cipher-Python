
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar_func():
    choice = input("Enter your choice Encrypt or Decrypt ? ").lower()
    plain_text = input("Enter your message : ")
    shift = int(input("Enter the shift amount : "))
    modified_text = ""
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift) % len(alphabet) if choice == 'encrypt' else (position - shift) % len(alphabet)
            new_text = alphabet[new_position]
            modified_text += new_text
        else:
            modified_text += char
    print(f"Your encrypted text is : {modified_text}")
    
caesar_func()

while True:
    cmd = input("Type 'yes' if you want to encrypt/decrypt again, otherwise type 'no'. ")
    if cmd == "yes":
        caesar_func()
    else:
        print("Goodbye!")
        break



   
