import requests

# membaca daftar proxy dari "valid_proxies.txt" dan membaginya menjadi daftar proxies
with open("valid_proxies.txt", "r") as f:
    proxies = f.read().split("\n")

# Daftar situs web yang akan diakses menggunakan proxy
sites_to_check = ["https://books.toscrape.com/",
                  "https://books.toscrape.com/catalogue/category/books/fantasy_19/index.html",
                  "https://books.toscrape.com/catalogue/category/books/history_32/index.html"]

counter = 0

# loop digunakan untuk mengakses situs web dalam daftar sites_to_check. Di setiap iterasi, kode coba mengakses situs dengan
# proxy yang sesuai berdasarkan indeks counter. Jika berhasil, maka mencetak status kode 200 dan jika gagal berarti failed
for site in sites_to_check:
    try:
        print(f"using the proxy: {proxies[counter]}")
        res = requests.get(site, proxies={"http": proxies[counter], "https": proxies[counter]})
        print(res.status_code)
        # print(res.text)
    except:
        print("Failed")
    finally:
        counter += 1
        counter % len(proxies)