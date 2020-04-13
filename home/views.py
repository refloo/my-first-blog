from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
#from .models import Post
#from .forms import PostForm

from selenium import webdriver
import chromedriver_binary             # パスを通すためのコード
from time import sleep
import os
from selenium.common.exceptions import NoSuchElementException        #エラー無視


def index(request):
    return render(request, 'home/home.html', {})

def day(request):
    return render(request, 'home/testes.html', {})

def study(request):
    return render(request, 'home/study.html', {})

def magic(request):
    return render(request, 'home/magic.html', {})

def buy(request):
    return render(request, 'home/wish_list.html', {})

def update(request):
    """
    options = Options()

    # Headless Chromeを使うためのオプション
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
	
    # 設定したオプションを使ってwebdriverオブジェクトを作成
    driver = webdriver.Chrome(chrome_options=options)
    """
    driver = webdriver.Chrome()            # Chromeを準備

    sleep(2)

    #ワンパンマンHPへ
    top_url = 'https://tonarinoyj.jp/episode/13932016480028985383'
    driver.get(top_url)

    sleep(2)

    driver.execute_script("window.scrollTo(0, 500);")
    sleep(10)

    #最新話を取得
    last_day = driver.find_element_by_xpath("//*[@id='page-viewer']/section[3]/div[2]/div[2]/div[2]/ul/li[1]/a/div[2]/span").text
    last_episode = driver.find_element_by_xpath("//*[@id='page-viewer']/section[3]/div[2]/div[2]/div[2]/ul/li[1]/a/div[2]/h4").text
    comic = "<div class='comic'><a href=" + top_url + " target='_blank'>" + last_day + last_episode + "</a></div>\n"
    
    # Google Chrome Canaryを起動してRitsのトップページに接続
    base_url = 'https://ct.ritsumei.ac.jp/ct/home'
    driver.get(base_url)

    sleep(5)

    rits = "<div class='rits'><a href=" + base_url + " target='_blank'>manaba+R</a></div>\n"

    # あなたのユーザー名/メールアドレス
    username = 're0151rf'
    # あなたのパスワード
    password = 'Cdi9e3Bp'

    # ユーザー名の入力ボックスを探す
    username_box = driver.find_element_by_xpath("//*[@id='User_ID']")
    # パスワードの入力ボックスを探す
    password_box = driver.find_element_by_xpath("//*[@id='Password']")

    # ユーザ名とパスワードをインプットする
    username_box.send_keys(username)
    password_box.send_keys(password)

    # ログインボタンを探す
    login_button = driver.find_element_by_xpath("//*[@id='Submit']")
    #ログインボタンをクリック
    login_button.click()

    #5秒待つ
    sleep(5)

    #新着情報へ
    driver.get('https://ct.ritsumei.ac.jp/ct/home_whatsnew')

    sleep(1)

    #testesを更新
    n_path = "C:/Users/sprite564/djangogirls/home/templates/home/testes.html"

    with open(n_path, mode='w') as reset:
        default1 = "{% load static %}\n<!DOCTYPE html>\n<html>\n<head>\n<meta http-equiv='Content-Type' content='text/html; charset=UTF-8' />\n<meta name='author' content=''><meta name='description' content=''>\n"
        default2 = "<meta name='keywords' content=''>\n<title>Notitle</title>\n<a href=\"{% url 'update' %}\">UPDATE</a>\n</head>\n<body>\n<div class='Rits_info'>\n"
        wether = "<iframe src='https://www.jma.go.jp/jp/yoho/334.html' width='700px' height='565px'></iframe>\n<a class='home' href=\"{% url 'index' %}\">Home</a>\n"
        default = default1 + default2 + wether
        reset.write(default)

    with open(n_path, mode='a', encoding='UTF-8') as f:
        f.write(comic)
        f.write(rits)

        for i in range(1, 31):
            news = driver.find_element_by_xpath("//*[@id='container']/div[2]/div/div/div/table/tbody/tr[" + str(i) + "]/td[1]/div/a").text
            title = "<h3 class='info" + str(i) + "'>" + news + "</h3>\n"

            news_rink = driver.find_element_by_xpath("//*[@id='container']/div[2]/div/div/div/table/tbody/tr[" + str(i) + "]/td[1]/div/a")
            news_rink.click()
            sleep(0.1)

            try:
                detail = driver.find_element_by_xpath("//*[@id='container']/div[2]/div/div/div/div[2]/div[4]").text
                fine = "<p class='detail" + str(i) + "'>" + detail + "</p>\n"
                f.write(title)
                f.write(fine)
                driver.back()

            except NoSuchElementException:
                try:
                    detail = driver.find_element_by_xpath("//*[@id='container']/div[2]/div[3]/div/div/div[2]/div[1]").text
                    fine = "<p class='detail" + str(i) + "'>" + detail + "</p>\n"
                    f.write(title)
                    f.write(fine)
                    driver.back()

                except NoSuchElementException:
                    driver.back()

        end = "\n</div>\n</body>\n</html>"
        f.write(end)


    #付け足し終わり

    # ブラウザを閉じる
    driver.close()
    # Google Chrome Canaryを終了する
    driver.quit()

    return render(request, 'home/home.html', {})

def merukari(request):
    driver = webdriver.Chrome()            # Chromeを準備

    #メルカリへ
    keywords = ['inscrutable green', 'インスクリュータブル グリーン', "jermay's mind", 'ジャーメイズマインド', 'anti faro', 'アンチファロー', 'past midnight', 'パストミッドナイト', 'the cheat', 'ザ・チート', 'benjamin earl', 'ベンジャミンアール', 'emotional intelligence', 'エモーショナル・インテリジェンス']
    base_url = 'https://www.mercari.com/jp/search/?sort_order=&keyword='
    condition = '&category_root=5&category_child=74&brand_name=&brand_id=&size_group=&price_min=&price_max=&status_on_sale=1' #販売中、CD&DVDのみ

    wish_url = "C:/Users/sprite564/djangogirls/home/templates/home/wish_list.html"
    listup = []

    with open(wish_url, 'w', encoding='UTF-8') as f:
        base1_html = "{% load static %}\n<!DOCTYPE html>\n<html>\n<head>\n<meta http-equiv='Content-Type' content='text/html; charset=UTF-8' />\n<meta name='author' content=''><meta name='description' content=''>\n"
        base2_html = "<meta name='keywords' content=''>\n<link rel='stylesheet' href=\"{% static 'css/wish_list.css' %}\" type='text/css' />\n<title>Wish List</title>\n</head>\n<body>\n<a href=\"{% url 'merukari' %}\">list up</a>\n<a class='home' href=\"{% url 'index' %}\">Home</a>\n<div class='merukari'>\n"
        base_html = base1_html + base2_html

        f.write(base_html)

        for k in keywords:
            top_url = base_url + k + condition
            driver.get(top_url)
            sleep(2)

            for i in range(1, 50):
                try:
                    image_xpath = '/html/body/div[1]/main/div[1]/section/div[2]/section[' + str(i) + ']/a/figure/img'
                    item_xpath = '/html/body/div[1]/main/div[1]/section/div[2]/section[' + str(i) + ']/a/div/h3'
                    price_xpath = '/html/body/div[1]/main/div[1]/section/div[2]/section[' + str(i) + ']/a/div/div/div[1]'
                    image = driver.find_element_by_xpath(image_xpath)
                    item = driver.find_element_by_xpath(item_xpath)
                    price = driver.find_element_by_xpath(price_xpath)
                    write_goods = "<img src='" + image.get_attribute("src") + "'>\n<p>" + item.text + "</p>\n<p>" + price.text + "</p>\n"
                    listup.append(write_goods)

                except NoSuchElementException:
                    break

        listup = list(set(listup))
        for j in listup:
            f.write(j)

        end_html = "</div>\n</body>\n</html>"
        f.write(end_html)


    # ブラウザを閉じる
    driver.close()
    # Google Chrome Canaryを終了する
    driver.quit()

    return render(request, 'home/home.html', {})