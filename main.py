import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

video_url = input("Shorts/Video Linki: ")
izleme_suresi = int(input("Kaç saniye izlensin? (15-30 önerilir): "))

def bot_baslat():
    # --- TERMUX ÖZEL AYARLARI ---
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # Termux'taki Chromium'un yeri
    chrome_options.binary_location = "/usr/bin/chromium-browser" 
    
    # Termux'taki Chromedriver'ın yolu
    # (Eğer hata alırsan bu yolu "/data/data/com.termux/files/usr/bin/chromedriver" olarak dene)
    service = Service("/usr/bin/chromedriver") 

    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        print(f"[*] İzleyici gönderiliyor... {video_url}")
        driver.get(video_url)
        time.sleep(5) 
        bekle = izleme_suresi + random.randint(1, 5)
        print(f"[+] Video oynatılıyor. {bekle} sn beklenecek...")
        time.sleep(bekle)
    except Exception as e:
        print(f"[-] Hata: {e}")
    finally:
        driver.quit()

while True:
    bot_baslat()
    time.sleep(random.randint(5, 10))
