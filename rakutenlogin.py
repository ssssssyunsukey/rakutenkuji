import time
from selenium import webdriver

driver = webdriver.Chrome()

# 楽天ログインページに移動
driver.get('https://grp01.id.rakuten.co.jp/rms/nid/vc?__event=login&service_id=top')
time.sleep(5)

#elementで位置を取得し、send_keysで楽天ユーザー名を入力
element = driver.find_element_by_id('loginInner_u')
element.send_keys('ssssssyunsukey@gmail.com')

#elementで位置を取得し、send_keysでパスワードを入力
element = driver.find_element_by_id('loginInner_p')
element.send_keys('Sanosyunsuke2')
time.sleep(5)

#elementで位置を取得し、click()でログインボタンをクリックする
element = driver.find_element_by_css_selector('input[type="submit"]')
element.click()
time.sleep(10)

#ラッキーくじURLへアクセス
driver.get('https://kuji.rakuten.co.jp/46211bf9dd')
time.sleep(5)

#くじ開始ボタンの要素を取得し、クリック
element = driver.find_element_by_xpath("//*[@id='entry']")
element.click()
time.sleep(30)

#終了処理
driver.quit()

print('完了しました')