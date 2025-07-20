import pyautogui

def capture_screenshots():
  image = pyautogui.screenshot()
  image.save("logs/screenshot.png")