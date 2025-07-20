import pyperclip

def get_clipboard():
  try:
    with open("logs/clipboard.txt", "w") as f:
      f.write(f"Clipboard Data:\n{pyperclip.paste()}")
  except:
    pass