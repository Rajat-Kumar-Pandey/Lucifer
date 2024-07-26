from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from os import getcwd

# Configure Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--use-fake-ui-for-media-stream")
chrome_options.add_argument("--headless=new")  # Uncomment this line if you want headless mode

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Define paths
# website = f"file://{getcwd()}\\index.html"  # Use file:// for local files

website = f"file:///F:/LUCIFER/PACKAGE/index.html"
print(f"Opening URL: {website}")

rec_file = f"{getcwd()}\\input.txt"

# Open the website
driver.get(website)

def listen():
    try:
        # Wait for the start button to be clickable and click it
        start_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'startButton')))
        start_button.click()
        print("Listening...")

        output_text = ""
        is_second_click = False

        while True:
            # Wait for the output element to be present
            output_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'output')))
            current_text = output_element.text.strip()  # Get text from the output element

            # Check button text and manage output
            if "Start Listening" in start_button.text and is_second_click:
                if output_text:
                    is_second_click = False
            elif "Listening..." in start_button.text:
                is_second_click = True
                if current_text != output_text:
                    output_text = current_text
                    with open(rec_file, "w") as file:
                        file.write(output_text.lower())
                        print("USER: " + output_text)
            else:
                print("Waiting for the output...")
    except KeyboardInterrupt:
        print("Listening interrupted by user.")
    except Exception as e:
        print("Error:", e)
    finally:
        driver.quit()

listen()
