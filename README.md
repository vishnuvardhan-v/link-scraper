# Link Scraper Script

A Python web scraper that monitors websites for specific keywords and sends notifications when found. The script continuously checks a target URL at specified intervals and alerts you via desktop notifications and WhatsApp messages when your keyword appears.

## Features

- 🔍 **Keyword Monitoring**: Continuously monitors websites for specific words/phrases
- 🔔 **Desktop Notifications**: Shows system notifications when keywords are found
- 📱 **WhatsApp Integration**: Automatically sends WhatsApp messages via pywhatkit
- 🤖 **Bot Detection Avoidance**: Uses realistic browser headers and random delays
- ⚡ **Robust Error Handling**: Handles timeouts, connection errors, and HTTP errors gracefully
- 🔄 **Continuous Monitoring**: Runs indefinitely with configurable check intervals
- 📊 **Real-time Status**: Provides colored console output for easy monitoring

## Requirements

- Python 3.7+
- Internet connection
- WhatsApp Web (for WhatsApp notifications)

## Installation

1. Clone or download this repository:

```bash
git clone <repository-url>
cd link-scraper-script
```

2. Install required dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Before running the script, update the configuration variables in `scrape.py`:

```python
url = "https://example.com"    # Target URL to monitor
word = "test"                             # Keyword to search for
phone_number = "+91123456789"                 # WhatsApp number (with country code)
check_interval = 10                            # Minutes between checks
```

### Configuration Parameters

- **`url`**: The website URL you want to monitor
- **`word`**: The keyword or phrase to search for (case-insensitive)
- **`phone_number`**: Your WhatsApp number in international format (e.g., +1234567890)
- **`check_interval`**: Time in minutes between each check
- **`message_text`**: Custom WhatsApp message (automatically generated)

## Usage

1. **Configure the script** with your target URL, keyword, and phone number
2. **Run the script**:

```bash
python scrape.py
```

3. **First-time WhatsApp setup**:
   - The script will open WhatsApp Web in your browser
   - Scan the QR code with your phone to link WhatsApp Web
   - Keep the browser tab open while the script runs

## How It Works

1. **Web Scraping**: The script fetches the target webpage using requests with realistic browser headers
2. **Content Parsing**: BeautifulSoup extracts and parses the HTML content
3. **Keyword Search**: Searches for the specified keyword in the webpage text (case-insensitive)
4. **Notifications**: When keyword is found:
   - Shows desktop notification
   - Sends WhatsApp message
   - Stops monitoring (optional - can be modified to continue)
5. **Retry Logic**: Waits for the specified interval before checking again

## Output Examples

```
👀 Watching example.com for 'test' every 10 minutes...
❌ Word "test" not found on https://example.com
⏳ Waiting 10 minutes before next check...
✅ Word "test" found on https://example.com
📲 WhatsApp notification scheduled!
✅ Word found. Stopping watcher.
```

## Dependencies

- **requests**: HTTP library for web scraping
- **beautifulsoup4**: HTML parsing and content extraction
- **plyer**: Cross-platform desktop notifications
- **pywhatkit**: WhatsApp automation

## Error Handling

The script handles various error scenarios:

- **Timeout Errors**: When the website takes too long to respond
- **Connection Errors**: Network connectivity issues
- **HTTP Errors**: Server errors (404, 403, etc.)
- **General Exceptions**: Unexpected errors with detailed logging

## Customization

### Modify Check Behavior

To continue monitoring after finding the keyword, comment out the `break` statement:

```python
if found:
    print("✅ Word found. Stopping watcher.")
    # break  # Comment this line to continue monitoring
```

### Change Notification Settings

Modify the notification parameters:

```python
notification.notify(
    title="Custom Title",
    message="Custom message",
    timeout=10  # Notification duration in seconds
)
```

### Adjust Request Headers

Modify browser headers in the `headers` dictionary to mimic different browsers or add additional headers.

## Use Cases

- **E-commerce Monitoring**: Track product availability, price drops, or sale announcements
- **Content Monitoring**: Monitor blogs, news sites, or forums for specific topics
- **Stock Alerts**: Watch for product restocks or availability changes
- **Price Tracking**: Monitor for discount keywords like "sale", "offer", etc.

## Important Notes

- **Rate Limiting**: The script includes random delays to avoid being flagged as a bot
- **WhatsApp Web**: Keep WhatsApp Web open in your browser for notifications to work
- **Ethical Usage**: Respect website terms of service and don't overload servers with requests
- **Network Dependency**: Script requires stable internet connection

## Troubleshooting

### WhatsApp Issues

- Ensure WhatsApp Web is logged in and browser tab remains open
- Check phone number format (include country code with +)
- Verify time settings on your system

### Connection Issues

- Check internet connectivity
- Try increasing timeout values
- Some websites may block automated requests

### Permission Issues

- On some systems, desktop notifications may require permission
- Run with appropriate privileges if needed

## License

This project is open source. Feel free to modify and distribute according to your needs.

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.
