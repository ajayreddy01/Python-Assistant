def whatsapp():
    import selenium
    from selenium import webdriver
    from  selenium.webdriver.common.keys import Keys
    import time
    from time import sleep
    user_name_list = []
    n = int(input('No.of user You want To Send Text  :'))
    Message = input('What You Want To Send  :')
    for i in range(0,n):
        username= str(input('Enter User Name :'))
        user_name_list.append(username)

    options = webdriver.ChromeOptions()
    options.add_argument('user-data-dir=C:\\Users\\AJAY REDDY\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
    options.add_argument('--profile-directory=Default')

    chromedriver_path ='C:/chromedriver.exe'
    webdriver = webdriver.Chrome(executable_path=chromedriver_path, options = options)

    webdriver.get('https://web.whatsapp.com')

    sleep(60)# to load website properly

    def new_chat(user_name):
        search_user =webdriver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
        search_user.send_keys(user_name)
        search_user.send_keys(u'\ue007')

        #user = webdriver.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
        #user.click()

    for user_name in user_name_list:
        new_chat(user_name)
        
        message_box = webdriver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        message_box.send_keys(Message)

        send_key = webdriver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
        send_key.click()
    sleep(10)
    webdriver.quit()    


    
