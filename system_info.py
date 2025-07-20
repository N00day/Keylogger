import socket, platform

def get_system_info():
  with open("logs/system.txt", "w") as f:
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    f.write(f"Hostname: {hostname}\n")
    f.write(f"IP Address: {IPAddr}\n")
    f.write(f"System: {platform.system()} {platform.version()}\n")
    f.write(f"Machine: {platform.machine()}\n")