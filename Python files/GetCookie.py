from selenium import webdriver
import json,time

# def Registr(account,password):
#     driver = webdriver.Chrome()
#     driver.get('https://baidu.com/')
#     driver.find_element_by_xpath('//*[@id="u1"]/a[7]').click()
#     time.sleep(2)
#     driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__footerULoginBtn"]').click()
#     time.sleep(2)
#     driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__userName"]').send_keys(account)
#     driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__password"]').send_keys(password)
#     time.sleep(2)
#     driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__submit"]').click()
#     time.sleep(2)
#     # 发送验证码
#     try:
#        driver.find_element_by_xpath('//*[@id="TANGRAM__27__button_send_mobile"]').click()
#        code_photo = input('请输入验证码：')
#        driver.find_element_by_xpath('//*[@id="TANGRAM__27__input_label_vcode"]').send_keys(str(code_photo))
#        time.sleep(5)
#        driver.find_element_by_xpath('//*[@id="TANGRAM__27__button_submit"]').click()
#        time.sleep(10)
#     except: pass
#     cookies = driver.get_cookies()
#     f1 = open('cookie.txt','w')
#     f1.write(json.dumps(cookies))
#     f1.close()
#
# if __name__ == '__main__':
#     Registr('13572252156','xiangongye1234')


driver = webdriver.Chrome()
driver.get('https://baidu.com/')
driver.find_element_by_xpath('//*[@id="u1"]/a[7]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__footerULoginBtn"]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__userName"]').send_keys('13572252156')
driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__password"]').send_keys('xiangongye1234')
driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__submit"]').click()
time.sleep(30)


cookies = driver.get_cookies()
f1 = open('cookie.txt','w')
f1.write(json.dumps(cookies))
f1.close()