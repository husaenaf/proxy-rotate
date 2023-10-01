import requests

# Membaca daftar proxy dari "valid_proxies.txt" dan membaginya menjadi daftar proxies dengan memisahkan barisnya
# dengan karakter baris baru ("\n")
with open("valid_proxies.txt", "r") as f:
    proxies = f.read().split("\n")

# Daftar situs web yang akan diakses menggunakan proxy
sites_to_check = ["https://top-1000-sekolah.ltmpt.ac.id/?page=1&per-page=100",
                  "https://top-1000-sekolah.ltmpt.ac.id/?page=2&per-page=100",
                  "https://top-1000-sekolah.ltmpt.ac.id/?page=3&per-page=100"]

for site in sites_to_check:
    proxy_succeed = False  # untuk menandai apakah proxy berhasil mengakses situs saat ini atau tidak
    for proxy in proxies:
        # Menguji proxy, jika berhasil (kode 200) maka pesan akan dicetak dan proxy_succeed bernilai True
        # namun jika proxy tidak berfungsi, atau dicek lebih dari 3 detik, maka akan memakai proxy lain
        try:
            res = requests.get(site, proxies={"http": proxy, "https": proxy}, timeout=5)
            if res.status_code == 200:
                # Memisahkan alamat IP dan port dari proxy
                ip_address, port = proxy.split(":")
                print(f"Proxy {ip_address}:{port} berhasil mengakses {site}")
                proxy_succeed = True
                break
        except:
            continue

    if not proxy_succeed:
        print(f"Semua proxy gagal mengakses {site}")
