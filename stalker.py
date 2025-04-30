import platform
import psutil
import socket
import requests

def get_info():
    battery = psutil.sensors_battery()
    info = {
        "device": platform.node(),
        "os": platform.system(),
        "version": platform.version(),
        "battery": battery.percent if battery else 'N/A',
        "charging": battery.power_plugged if battery else 'N/A',
        "ip": socket.gethostbyname(socket.gethostname())
    }
    return info

def send_to_admin(info):
    # Ganti URL ini dengan webhook bot lo nanti
    requests.post("https://your-webhook-here.com", json=info)

if __name__ == "__main__":
    data = get_info()
    print(data)
    send_to_admin(data)