from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common import by
PATH = "C:/Program Files (x86)/chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://teamseas.org/")

def donate():

    inp = input("Amount: ")

    inp_field = driver.find_element(by=by.By.NAME, value="other_amount")

    inp_field.send_keys(inp)

    next_btn = driver.find_element(by=by.By.ID, value="donateBtnStep1")

    next_btn.click()

    time.sleep(4)

    d_name = input("Display Name: ")

    d_email = input("Email Address: ")

    d_msg = input("Message: ")

    inp_name = driver.find_element(by=by.By.ID, value="inputName")
    inp_name.send_keys(d_name)

    time.sleep(2)

    inp_name = driver.find_element(by=by.By.ID, value="inputEmail")
    inp_name.send_keys(d_email)

    time.sleep(2)

    inp_name = driver.find_element(by=by.By.ID, value="inputMessage")
    inp_name.send_keys(d_msg)

    time.sleep(2)

    btn_2 = driver.find_element(by=by.By.ID, value="donateBtnStep2")

    btn_2.click()


cmd = input('What would you like to do, know the amount of trashed removed (USE the "a" command) or Donate (USE THE "d" COMMAND) ')

if cmd.upper() == "A":

    search = driver.find_element(by=by.By.ID, value="liveCounter")

    print(search.text)

elif cmd.upper() == "D":
    donate()