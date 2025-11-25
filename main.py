from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
import os

print("🚀 Memulai automasi...")

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--window-size=1920,1080')

# URL video
video_url = "https://videy.tv/s/6rZ0X5nr"

try:
    # Buat driver
    driver = webdriver.Chrome(options=chrome_options)
    
    print(f"📺 Membuka video: {video_url}")
    driver.get(video_url)
    
    print("⏳ Menunggu iklan load (15 detik)...")
    time.sleep(15)
    
    print("✅ Iklan ter-serve! Menunggu video selesai...")
    time.sleep(300)  # 5 menit
    
    print("🎉 Selesai!")
    driver.quit()
    
except Exception as e:
    print(f"❌ Error: {e}")
