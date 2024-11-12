import subprocess
import re

def scane_wifi():
    result = subprocess.run(["sudo", "iwlist","wlan0", "scan"], capture_output=True,text=True)
    internet = re.findall(r'ESSID:"(.*?)"', result.stdout)
    for one in internet:
        print(one)

scane_wifi()


def connetc_wifi(ssid, password):

    # Desconectarse 
    subprocess.run(["nmcli","d", "disconnect", "wlan0"])

    #Conectarse a red
    result = subprocess.run(
        ["nmcli", "d","wifi","connect", ssid, "password", password ],
        capture_output=True,
        text=True
    )

    # Verificar si la conexión fue exitosa
    if result.returncode == 0:
        print(f"Conectado a {ssid} exitosamente.")
    else:
        print(f"No se pudo conectar a {ssid}: {result.stderr}")


# Ejemplo de uso
ssid = input("Introduce el SSID de la red: ")
password = input("Introduce la contraseña de la red: ")
connetc_wifi(ssid, password)