from cryptography.fernet import Fernet


'''def write_key():
    key = Fernet.generate_key()
    with open ("key.key", "wb") as key_file:
        key_file.write(key)'''

def load_key():
    file = open ("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key() 
fer = Fernet(key)



def view():
    with open('password.txt', 'r') as f:
        for line in f:
            data = line.rstrip("\n")

            if "|" not in data:
                continue

            user, passw = data.split("|", 1)

            try:
                decrypted = fer.decrypt(passw.encode()).decode()
                print("User:", user, "| Password:", decrypted)
            except Exception:
                print("Error: Is password ki key match nahi kar rahi:", user)

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('password.txt', 'a') as f:
        f.write(name + '|' + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit ? ").lower()
    if mode == "q":
        break
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue