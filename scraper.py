#Import Dependencies
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os
import time
from bs4 import BeautifulSoup


def Marketplace(city, product, minimum, maximum,listed):
    city = city
    product = product
    min_price = minimum
    max_price = maximum
    days_listed = listed


    #Configure Chromedriver

    chrome_install = ChromeDriverManager().install()

    folder = os.path.dirname(chrome_install)
    chromedriver_path = os.path.join(folder, "chromedriver.exe")


    # Initialize Chrome WebDriver
    browser = webdriver.Chrome(
        service = Service(chromedriver_path),
    )


    # Set up base URL
    url = f'https://www.facebook.com/marketplace/{city}/search?query={product}&minPrice={min_price}&maxPrice={max_price}&daysSinceListed={days_listed}&exact=false'

    # Visit the website
    browser.get(url)


    # Locate the button with aria-label="Decline optional cookies" (Europe)
    try:
        decline_button = browser.find_element(By.XPATH, '//div[@aria-label="Close" and @role="button"]')
        decline_button.click()
        print("Decline optional cookies button clicked!")
        
    except:
        print("Could not find or click the optional cookies button!")
        pass


    # Locate the button for the login pop-up with aria-label="Close"
    try:
        close_button = browser.find_element(By.XPATH, '//div[@aria-label="Close" and @role="button"]')
        close_button.click()
        print("Close button clicked!")
        
    except:
        print("Could not find or click the close button!")
        pass



    def closePopUp():
        try:
            close_button = browser.find_element(By.XPATH, '//div[@aria-label="Close" and @role="button"]')
            close_button.click()
            print("Close button clicked!")
            return True
        
        except:
            print("Could not find or click the close button!")
            return False


    #Scroll down to load all results
    end_time = time.time() + 10 # Set the end time to 60 seconds from now
    try:
        # Get the initial scroll position
        last_height = browser.execute_script("return document.body.scrollHeight")
        
        while time.time() < end_time:
            while True:  # Infinite loop
                if closePopUp():  # Check the condition
                    time.sleep(1)  # Wait for 1 second
                    continue  # Restart the loop if the condition is True
                
                # Additional logic here, executed only if closePopUp() is False
                print("Popup closed or no popup to close.")
                break  # Exit the loop when desired
            
            
    except Exception as e:
        print(f"An error occurred: {e}")


    closePopUp()
    # Retrieve the HTML
    html = browser.page_source

    # Use BeautifulSoup to parse the HTML
    soup = BeautifulSoup(html, 'html.parser')

    #Close the browser
    browser.close()


    print(soup)


    # Find all link elements
    links = soup.find_all('a')

    # Only keep items where the text matches your search terms and desired location
    rsx_links = [link['href'] for link in links if product.lower() in link.text.lower() and city.lower() in link.text.lower()]


    rsx_data = []
    start_printing = False
    i = 0
    for link in links:
        baselink = "https://www.facebook.com"
        extension = link.get('href')
        
        if(start_printing == True):
            if(link.text.lower()=="log in"):
                break
            if(True):
                #print(link.text.lower())
                #print(baselink+extension)
                url = baselink+extension
                text = link.text.lower()
                rsx_data.append({'text':text,'url':url})
                #print(i)
                i+=1
        if(baselink+extension == "https://www.facebook.com/marketplace/categories/"):
            start_printing = True
        
    
    return rsx_data