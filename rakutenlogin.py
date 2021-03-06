import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rakucoin.appspot.com/rakuten/kuji/")
time.sleep(5)

#aタグを全て取得
urls = driver.find_elements_by_xpath ("//table/tbody/tr/td/a")
url_txts = [url.get_attribute("href") for url in urls]

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

for url_txt in url_txts:

#URLにリダイレクトを含む時、上手くくじを引けないので、まず除外します
    if 'redirect' in url_txt:
        print(f'{url_txt}はリダイレクトを含むのでスキップします')
        continue
    try:
        driver.get(url_txt)
        time.sleep(5)
    except:
        print(f'{url_txt}に遷移出来ませんでした。')
        continue
    
    print(f"Accessing:{url_txt}")
    #もしくじを引くボタン（entry）が存在したら

    #entryボタンの有無を、配列の長さから判定します
    if(len(driver.find_elements(By.ID, "entry"))>0):
        print("くじを引きます")
        time.sleep(2)
        try:
            start_button = driver.find_element(By.ID, "entry")
            start_button.click()
            #webdriverwaitを使用して、くじを引いているURLから別のURLに変化するまで待ちます
            WebDriverWait(driver,60).until(EC.url_changes(url_txt))

        except:
            print('くじを引くボタンはありましたが、押せませんでした')
    #くじを引くボタンがなかった時
    else:
        try:
            print("くじを引くボタンがありませんでした")
            time.sleep(1)
        except Exception as e:
            print('不明なエラーが発生しました')
            print(f'エラー内容{e.message}')
            time.sleep(1)
driver.close()

print('完了しました。')

driver.quit()


exit()

# ラッキーくじURLへアクセス
# driver.get('https://kuji.rakuten.co.jp/46211bf9dd')
# time.sleep(5)

# くじ開始ボタンの要素を取得し、クリック
# element = driver.find_element_by_xpath("//*[@id='entry']")
# element.click()
# time.sleep(15)

# 終了処理
# driver.quit()

# print('完了しました')
