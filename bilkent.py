

from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from colorama import init
from termcolor import colored
import json
import os
import threading
import sys
import itertools


init()

main_url = "https://stars.bilkent.edu.tr/"
tab_url = "https://webmail.bilkent.edu.tr/"
version = 2.0
done = False


mode = sys.argv[1]


driver = webdriver.Chrome(
    executable_path=f'{os.getcwd()}/chromedriver')
options = Options()

preferences = {"profile.default_content_setting_values.notifications": 2}
options.add_experimental_option("prefs", preferences)
options.page_load_strategy = 'eager'


def getCode(mb, pb):
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(tab_url)

    driver.find_element_by_xpath(
        '/html/body/div[1]/div/form/table/tbody/tr[1]/td[2]/input').send_keys(mb)
    time.sleep(0.2)
    driver.find_element_by_xpath(
        '/html/body/div[1]/div/form/table/tbody/tr[2]/td[2]/input').send_keys(pb)
    time.sleep(0.1)
    driver.find_element_by_xpath('/html/body/div[1]/div/form/p/button').click()
    time.sleep(1)
    driver.find_elements_by_class_name('message')[0].click()
    frame = driver.find_element_by_tag_name("iframe")
    driver.switch_to.default_content()
    driver.switch_to.frame(frame)
    time.sleep(1)
    text = driver.find_element_by_xpath(
        '/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div').text
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element_by_id(
        'rcmbtn123').click()
    code = text.split()[2]
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    return code

def join():

    with open("credentials.json") as cred:
        data = json.load(cred)
        uid = data["bilkent_id"]
        upw = data["stars_password"]
        mb = data["bilkent_mail"]
        pb = data["mail_password"]

    driver.get(main_url)
    driver.find_element_by_xpath('//*[@id="services"]/li[3]/a').click()
    driver.find_element_by_xpath(
        '//*[@id="LoginForm_username"]').send_keys(uid)
    driver.find_element_by_xpath(
        '/html/body/div/div[1]/div[2]/div[1]/div/section/form/fieldset/div/div[1]/div[2]/div/div/input').send_keys(upw)
    driver.find_element_by_xpath(
        '/html/body/div/div[1]/div[2]/div[1]/div/section/form/fieldset/div/div[1]/div[3]/button').click()
    time.sleep(0.5)

    time.sleep(0.5)
    driver.find_element_by_xpath(
        '/html/body/div/div[1]/div[2]/div[1]/div/section/form/fieldset/div/div[1]/div[1]/div/div/input').send_keys(getCode(mb, pb))
    driver.find_element_by_xpath(
        '/html/body/div/div[1]/div[2]/div[1]/div/section/form/fieldset/div/div[1]/div[2]/button').click()
    time.sleep(1)
    try:
        driver.execute_script("closeMessage();")
    except:
        pass

    if (mode == "zoom"):
        global done
        done = True
        time.sleep(1.2)
        driver.find_element_by_xpath(
            '/html/body/div[13]/div[2]/div/div[7]/div[2]/div[2]/a[1]').click()
        for i in range(10, 0, -1):
            # print(colored("\r>>", "cyan", "on_grey", ["bold"]),
            #     colored(f"Windows will be closed in {i}", "white"))
            sys.stdout.write(f"\rWindows will be closed in {i}  ")
            time.sleep(1)
        sys.stdout.write("\r                                ")
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        driver.close()

def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rRunning ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r                        ')



if __name__ == "__main__":
    print(colored(">>", "cyan", "on_grey", ["bold"]),
        colored(f"berkegokmen bilkent script version {version}", "white"))
    
    print(colored(">>", "cyan", "on_grey", ["bold"]),
        colored(f"Target: {mode}", "white"))

    t = threading.Thread(target=animate)
    t.start()
    join()
    done = True
    sys.stdout.write("\r")
    sys.stdout.flush()
    print(colored(">>", "cyan", "on_grey", ["bold"]),
        colored(f"Done.         \n", "white"))
