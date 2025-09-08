import requests
from bs4 import BeautifulSoup
from plyer import notification
import pywhatkit
import datetime
import time
import random

def check_word_in_url(url, word, phone_number, message_text):
    try:
        # Headers to mimic a real browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }
        
        # Create session for better connection handling
        session = requests.Session()
        session.headers.update(headers)
        
        # Add random delay to avoid being flagged as bot
        time.sleep(random.uniform(1, 3))
        
        # Fetch webpage with longer timeout and retries
        response = session.get(url, timeout=30)
        response.raise_for_status()
        content = response.text

        # Parse HTML
        soup = BeautifulSoup(content, "html.parser")
        text = soup.get_text().lower()

        # Check if word exists
        if word.lower() in text:
            # Show system notification
            notification.notify(
                title="Word Found!",
                message=f'"{word}" was found on {url}',
                timeout=5
            )
            print(f'✅ Word "{word}" found on {url}')

            # Send WhatsApp message
            now = datetime.datetime.now()
            send_hour = now.hour
            send_minute = now.minute + 2  # pywhatkit requires future time

            # Handle minute overflow (e.g., 11:59 + 2 → 12:01)
            if send_minute >= 60:
                send_minute -= 60
                send_hour = (send_hour + 1) % 24

            pywhatkit.sendwhatmsg(
                phone_no=phone_number,
                message=message_text,
                time_hour=send_hour,
                time_minute=send_minute
            )
            print("📲 WhatsApp notification scheduled!")

            return True  # Found
        else:
            print(f'❌ Word "{word}" not found on {url}')
            return False

    except requests.exceptions.Timeout:
        print("⚠️ Timeout Error: Request took too long. example might be slow or blocking requests.")
        return False
    except requests.exceptions.ConnectionError:
        print("⚠️ Connection Error: Unable to connect to Myntra. Check your internet connection.")
        return False
    except requests.exceptions.HTTPError as e:
        print(f"⚠️ HTTP Error: {e}. Myntra might be blocking automated requests.")
        return False
    except Exception as e:
        print("⚠️ Unexpected Error:", e)
        return False


if __name__ == "__main__":
    url = "example.com"        # URL to scrape
    word = "test"                   # Word to search
    phone_number = "+911234567890"     # WhatsApp number with country code
    message_text = f"The word '{word}' was found on {url}!"
    check_interval = 10  # minutes between checks

    print(f"👀 Watching {url} for '{word}' every {check_interval} minutes...")

    while True:
        found = check_word_in_url(url, word, phone_number, message_text)
        if found:
            print("✅ Word found. Stopping watcher.")
            break  # Stop after finding once (optional)
        else:
            print(f"⏳ Waiting {check_interval} minutes before next check...")
            time.sleep(check_interval * 60)