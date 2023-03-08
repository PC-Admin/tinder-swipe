
import pytest
import time
import json
import random
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

############################## Hard Coded Variables ##################################
telegram_client= 'https://tinder.com/en-AU'
############################## Hard Coded Variables ##################################

def sleep(duration, max_offset):
  duration_offset = round(random.uniform(-max_offset, max_offset), 4)
  duration += duration_offset
  print("Sleeping for " + str(round(duration, 4)) + "seconds...")
  time.sleep(duration)

def coordinate_varied(coordinate, max_offset):
  # Generate random offsets between -max_offset and max_offset
  coordinate_offset = random.randint(-max_offset, max_offset)
  # Add the offsets to the initial coordinates
  coordinate += coordinate_offset
  print("Coordinate generated: " + str(coordinate))
  return(coordinate)

class tinder_swiper():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()

  def login(self):
    # Logs the current browser window into your seek.com.au account
    print("Performing initial login to telegram...")
    self.driver.get(telegram_client)
    self.driver.set_window_size(1280, 960)
    #self.driver.find_element(By.LINK_TEXT, "Sign in").click()
    sleep(5,0)
    input("After logging into Tinder, press enter to continue...")

  def auto_swipe(self):
    #self.driver.get(telegram_client)
    self.driver.set_window_size(1280, 960)

    # Get the X and Y coordinates of the heart button
    x_coord = coordinate_varied(880, 8)
    y_coord = coordinate_varied(686, 8)

    # Use ActionChains to move the mouse to the specified coordinates and click
    action = ActionChains(self.driver)
    print("Action: Moving mouse to like button...")
    action.move_by_offset(x_coord, y_coord).perform()
    print("Action: Clicking the like button...")
    action.click().perform()
    sleep(1,0.5)
    #move mouse back to origin
    print("Action: Moving mouse back to origin...")
    action.move_by_offset(-x_coord, -y_coord).perform()

target_room = "Target Room Name"
target_time = datetime.time(hour=20)  # set the target time to 8PM

# start!
tinder = tinder_swiper()
tinder.setup_method('Firefox')

# First login to Tinder
tinder.login()

swipes = 0

while True:
    swipes += 1
    tinder.auto_swipe()
    print("Swiped " + str(swipes) + " girls so far!")
