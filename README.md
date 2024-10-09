## Marketplace Discord Bot

This is a Discord bot that allows users to search Facebook Marketplace for items based on specified criteria. The bot uses Selenium and BeautifulSoup to scrape listings and return the results directly in Discord.

![image](https://github.com/user-attachments/assets/31ab1676-7d1b-40e0-9c90-a6a4b7147042)


Features
Interactive Search: Collects search criteria from the user and returns matching listings.

Marketplace Search Command: Uses parameters like city, product, price range, and days listed to filter items.

Pre-configured Test Command: For quick testing without entering search parameters.

Requirements
Python 3.7+
Discord.py
Selenium
BeautifulSoup
ChromeDriver
dotenv
webdriver-manager

## Installation

# Clone the repository:
```bash
Copy code
git clone https://github.com/yourusername/marketplace-discord-bot.git
cd marketplace-discord-bot
```
# Install the required Python packages:
```bash
pip install -r requirements.txt
Set up your environment variables:
```

# Create a .env file in the project directory.
Add your Discord bot token to the .env file:

```plaintext
DISCORD_TOKEN=your_discord_bot_token
```
## Usage
Run the bot:

```bash
python bot.py
In Discord, use the following commands:
```
!marketplace: Initiates a series of prompts for entering search criteria.
you will be prompted for:
```plaintext
City: The location for the search.
Product: The item you want to search for.
Minimum Price: The minimum price in USD.
Maximum Price: The maximum price in USD.
Days Listed: The number of days since the listing was posted.
```

!marketplacetest: Runs a pre-configured test search with set parameters.


```plaintext
City: Houston
Product: RSX
Minimum Price: $0
Maximum Price: $8000
Days Listed: 7
```
