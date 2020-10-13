import sys, time, json, datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from json.decoder import JSONDecodeError

def init():
    f = open("./credentials.json", "r", encoding="utf8")
    try:
        data = json.load(f)
    except JSONDecodeError:
        print("[-] credentials.json 파일이 올바르지 않습니다.")
        sys.exit(0)

    if data["email"] == "" or data["pw"] == "" or data["std"] == "" or data["proj_folder"] == "" or data["chromedriver_path"] == "":
        print("[-] 비어있는 값이 있습니다.")
        sys.exit(0)

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    try:
        browser = webdriver.Chrome(data["chromedriver_path"], options=options)
    except WebDriverException:
        print("[-] 크롬 브라우저 버전이 올바르지 않습니다.")
        sys.exit(0)

    login(data, browser)

def login(data, browser):
    browser.get("https://jhserver.dimigo.biz/~jhlecture2019/xe/index.php?mid=board_LDnK32&act=dispMemberLoginForm")
    browser.find_elements_by_xpath("//*[@id=\"uid\"]")[0].send_keys(data["email"])
    browser.find_elements_by_xpath("//*[@id=\"upw\"]")[0].send_keys(data["pw"])
    browser.find_elements_by_xpath("//*[@id=\"fo_member_login\"]/fieldset/div[2]/input")[0].click()
    browser.get("https://jhserver.dimigo.biz/~jhlecture2019/xe/index.php?mid=board_LDnK32&act=dispBoardWrite")
    
    write(data, browser)

def write(data, browser):
    try:
        browser.find_elements_by_xpath("//*[@id=\"postTitle\"]")[0].send_keys(data["std"])
    except IndexError:
        print("[-] 아이디와 비밀번호를 확인해주세요.")
        sys.exit(0)
    print("[+] 로그인 완료!")
    print("[+] 게시물 작성 중...")
    actions = ActionChains(browser)
    (
    actions.send_keys(Keys.TAB * 2).send_keys('a').perform()
    )
    now = datetime.datetime.now()
    nowDate = now.strftime('%m%d')
    browser.find_element_by_css_selector("input[type=file]").send_keys(data["proj_folder"] + nowDate + ".py")
    time.sleep(4)
    browser.find_elements_by_xpath("//*[@id=\"bd\"]/form/div[5]/input[2]")[0].click()
    print("\n[+] " + nowDate + ".py" " 제출 완료!")

if __name__ == "__main__":
    print("[*] dimigo.biz 파이썬 코드 자동 제출")
    init()