import time
import subprocess

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# === Optional: Wait before starting (useful if scheduling startup scripts) ===
time.sleep(60)

# === Configuration ===
# Update the following variables with your actual paths and values

BRAVE_PATH = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"  # Path to Brave browser executable
USER_DATA_DIR = r"C:\Users\YourUsername\AppData\Local\BraveSoftware\Brave-Browser\User Data"  # Your browser user profile
CALL_URL = "https://www.instagram.com/call/?has_video=false&ig_thread_id=YOUR_THREAD_ID"  # Replace with the actual call URL
user_agent = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/137.0.0.0 Safari/537.36"
)  # Optional custom user-agent

# === Setup Selenium WebDriver with Brave ===
options = Options()
options.binary_location = BRAVE_PATH
options.add_argument(f"--user-data-dir={USER_DATA_DIR}")  # Use your logged-in profile
options.add_argument("--profile-directory=Default")
options.add_argument(f"--user-agent={user_agent}")
options.add_experimental_option("detach", True)  # Keeps the browser open after script ends
options.add_experimental_option("excludeSwitches", ["enable-automation"])  # Remove automation banner

# Launch browser with configured options
driver = webdriver.Chrome(options=options)
driver.get(CALL_URL)

try:
    # === Step 1: Click "Start call" button ===
    start_call_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[text()='Start call']/ancestor::div[@role='button']")
        )
    )
    start_call_button.click()
    print("[✓] Call started. Waiting for redirect...")

    # === Step 2: Wait for Instagram to redirect with call session data ===
    WebDriverWait(driver, 30).until(lambda d: "server_info_data=" in d.current_url)
    print(f"[✓] Redirected to call URL: {driver.current_url}")

    # === Step 3: Wait until the "+1" participant indicator appears ===
    print("[⏳] Waiting for receiver to join (detecting '+1')...")
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(text(), '+ 1 other')]")
        )
    )
    print("[✓] Receiver joined! Playing audio...")

    # === Step 4: Play audio via mpv when the receiver joins ===
    video_url = "https://www.youtube.com/watch?v=qgfQSSnzDLI"  # Replace with your preferred audio
    subprocess.Popen([
        r"C:\mpv\mpv.exe",     # Path to mpv executable
        "--no-video",          # Audio only
        "--quiet",             # No extra output
        "--no-terminal",       # No terminal control
        "--vo=null",           # Disable video output
        "--loop-file=no",      # Play once
        video_url              # YouTube audio URL
    ])

except Exception as e:
    print("[!] Error occurred:", e)
