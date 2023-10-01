import threading
import queue
import requests

q = queue.Queue()   # menyimpan daftar proxy
valid_proxies = []

with open("proxy_list.txt", "r") as f:
    proxies = f.read().split("\n")
    for p in proxies:
        q.put(p)

# mengambil proxy dari antrian q, mencoba melakukan permintaan HTTP ke "http://ipinfo.io/json" menggunakan proxy itu,
# Jika permintaan berhasil (status kode 200), maka proxy tersebut dianggap valid dan dicetak ke layar.
def check_proxies():
    global q
    while not q.empty():
        proxy = q.get()
        try:
            res = requests.get("http://ipinfo.io/json", proxies={"http":proxy, "https:": proxy})
        except:
            continue
        if res.status_code == 200:
            print(proxy)

# Iterasi untuk mempersingkat durasi pemeriksaan proxy secara paralel/asyncronus, lebih cepat dan efisien
for _ in range(10):
    threading.Thread(target=check_proxies).start()