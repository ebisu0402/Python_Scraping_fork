from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary
import time
from selenium.webdriver.common.by import By

option = Options()
option.add_argument("--headless")

driver = webdriver.Chrome(options=option)
driver.get("https://www.google.co.jp/")

# 検索フィールドの取得
query = driver.find_element(by=By.NAME, value="q")

# 検索文字列を入力
query.send_keys("96猫")

# 3秒待つ
time.sleep(3)

# 検索ボタンをクリック
button = driver.find_element(by=By.NAME, value="btnK")
button.click()

# 3秒待つ
time.sleep(3)

# ページのソースコードを取得してBeautifulSoupで解析
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

# 最初の検索結果のリンクを取得
first_link_element = soup.find("div", class_="g").find("a", href=True)
first_link_url = first_link_element["href"] if first_link_element else None

# 取得したリンクにアクセスする
if first_link_url:
    driver.get(first_link_url)

time.sleep(3)

# ページのソースコードを取得してBeautifulSoupで解析
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

# ページのテキストを取得
page_text = soup.get_text()

# 特定の文字列が出現する回数を調べる
target_string = "96猫"
count = page_text.count(target_string)

# 結果を出力
print(f"ページ内で '{target_string}' が {count} 回見つかりました。")
