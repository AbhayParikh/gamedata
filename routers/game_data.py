from fastapi import APIRouter,HTTPException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service



router = APIRouter(tags=['GameData'])

@router.get("/game_data/{app_id}")
def game_data(app_id : str):
    try:
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # Run Chrome in headless mode
        chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration
        service = Service(executable_path='chromedriver.exe')
        driver = webdriver.Chrome(options=chrome_options,service=service)
        driver.get(f'https://play.google.com/store/apps/details?id={app_id}')
        # time.sleep(10)
        # Find an element by its ID and interact with it
        about_click = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@aria-label='See more information on About this game']"))
        )
        # about_click.click()
        driver.execute_script("arguments[0].click();", about_click)

        tabel_data = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '''//div[@role='dialog']//div[@class="G1zzid"]'''))
        )
        # tabel_data.text
        scrape_data = tabel_data.text.split('\n')
        print(scrape_data)
        d1={}
        l1=[]
        l2=[]
        for i in range(len(scrape_data)):
            if i%2==0:
                l1.append(scrape_data[i])
            else:
                l2.append(scrape_data[i])
        
        new_data = [dict(zip(l1,l2))]
        return new_data
    except:
        raise HTTPException(status_code=404, detail="Data not found!!!!")