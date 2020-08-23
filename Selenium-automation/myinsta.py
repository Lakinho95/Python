from urllib.parse import urlparse
import os
import time
from webdriver_manager.chrome import ChromeDriverManager
import requests
from selenium import webdriver

browser = webdriver.Chrome(ChromeDriverManager().install())

url = "https://www.instagram.com"
browser.get(url)

time.sleep(2)
username_el = browser.find_element_by_name("username")
username_el.send_keys('***********@gmail.com')

password_el = browser.find_element_by_name("password")
password_el.send_keys('***********')

time.sleep(1.5)
submit_btn_el = browser.find_element_by_css_selector("button[type='submit']")
submit_btn_el.click()

time.sleep(2)
notnow = browser.find_element_by_xpath("//button[contains(text(), 'Not Now')]")
notnow.click()
time.sleep(2)
notnow = browser.find_element_by_xpath("//button[contains(text(), 'Not Now')]")
notnow.click()

def liking_post(iteration_number):
      if iteration_number > 0:
            like_heart_svg_xpath = "//*[contains(@aria-label, 'Like')]"
            all_like_hearts_elements = browser.find_elements_by_xpath(like_heart_svg_xpath)
            h = []
            for heart_el in all_like_hearts_elements:
                  h.append(heart_el.get_attribute("height"))
                  heart_height = set(h)
            photo_heart = max(heart_height)
            for like_button in all_like_hearts_elements:
                  h = like_button.get_attribute("height")
                  if h == photo_heart or h == f"{photo_heart}":
                        print(like_button)
                        parent_button = like_button.find_element_by_xpath('..')
                        time.sleep(2)
                        try:
                              parent_button.click()
                        except:
                              pass
                        liking_post(iteration_number-1)

video_els = browser.find_elements_by_xpath("//video")
images_els = browser.find_elements_by_xpath("//img[contains(@class, 'FFVAD')]")
base_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(base_dir, "data")
os.makedirs(data_dir, exist_ok=True)

def name_func():
      ime = browser.find_elements_by_xpath("//a[contains(@tabindex, '0')][contains(@class, 'sqdOP')]")
      current_name = []
      for im in ime:
            yield(im.text + '.jpg')
generator = name_func()

number_of_likes = browser.find_elements_by_xpath("//button[contains(@class, 'sqdOP yWX7d     _8A5w5')]")
lajkovi1 = []
for likes in number_of_likes:
      likes1 = likes.text.split(' ')
      if len(likes1[0])>1:  #isinstance(, int)
            lajkovi1.append(likes1[0])

def likes():
      for lajks in lajkovi1:
            yield(lajks + '-likes-')
generator_likes = likes()

                  
def scrape_and_save():
      for el in images_els:
            # print(img.get_attribute('src'))
            url = el.get_attribute('src')
            base_url = urlparse(url).path
            filename = os.path.basename(next(generator_likes) + next(generator))
            filepath = os.path.join(data_dir, filename)
            if os.path.exists(filepath):
                  continue
            with requests.get(url, stream=True) as r:
                  try:
                        r.raise_for_status()
                  except:
                        continue
                  with open(filepath, 'wb') as f:
                        for chunk in r.iter_content(chunk_size=8192):
                              if chunk:
                                    f.write(chunk)

scrape_and_save()
