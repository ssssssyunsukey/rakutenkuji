import automate
# 要素がない場合のエラーハンドリング
from selenium.common.exceptions import NoSuchElementException

# くじURLリスト
# kujiUrlList = [
#     'https://kuji.rakuten.co.jp/4351057845',
#     'https://kuji.rakuten.co.jp/8c538152dd',
# ]

# ユーザーID
userId = 'ssssssyunsukey@gmail.com'
# パスワード
password = 'Sanosyunsuke2'

# 指定URLのくじを引く関数
def openKujiBrowser(selenium, url):
    # 処理中にエラーが発生して、後続処理に対し動作停止になるのを防ぐためtryしている。
    try:
        # 指定URLへアクセス
        selenium.access(url)

        # ページ読み込みのために遅延させる。
        selenium.stop(5)

        # くじ開始ボタンの要素をセット
        selenium.find_element_xpath("//*[@id='entry']")
        # くじ開始ボタンクリック
        selenium.click()

        # くじの実行時間のために遅延させる。
        selenium.stop(20)

    # 要素がない場合のエラーハンドリング
    except NoSuchElementException:
        selenium.stop(1)

# seleniumに関するinstance生成を行う。
selenium = automate.Selenium()

#ラッキーくじ一覧サイトへアクセス
selenium.access("https://rakucoin.appspot.com/rakuten/kuji/")
selenium.stop(5)
urls = selenium.find_element_xpath ("//table/tbody/tr/td/a")
kujiUrlList = [url_list.get_attribute("href") for url_list in urls]


# 楽天ログインページに移動
selenium.access('https://grp01.id.rakuten.co.jp/rms/nid/vc?__event=login&service_id=top')
# ページ読み込みのために遅延させる。
selenium.stop(5)

# 楽天にログイン

# userIdの要素をセット
selenium.find_element_by_id('loginInner_u')
# userIdに値を格納
selenium.set_value(userId)
# passwordの要素をセット
selenium.find_element_by_id('loginInner_p')
# passwordに値を格納
selenium.set_value(password)

# 「ログイン」ボタンの要素をセット
selenium.find_element_css_name('input[type="submit"]')
# ログインボタンをクリック
selenium.click()

# ページ読み込みのために遅延させる。
selenium.stop(10)

# くじのURLリストを開く
for url in kujiUrlList:
    openKujiBrowser(selenium, url)

# 処理終了
selenium.quit()
