# Discord Stage Tracker Bot

## Overview
This is a Discord Bot designed to track member activities on Discord stage channels and log the data in a Google Sheet.

## Features
- Track Stage Channel Activity: Logs when users join or leave stage channels in a Google Sheet.
- Commands:
    - `/get_bot_email`: Retrieves the bot's email address.
    - `/get_sheet`: Gets the URL of the connected Google Sheet.
    - `/update_sheet <url>`: Updates the Google Sheet URL.
    - `/share_sheet <email>`: Shares the Google Sheet with the specified email address.

## Installation
### Prerequisites
- Python 3.9+
- Discord account and a Discord bot token
- Google Cloud account with a Service Account for Google Sheets API access

### Setup
**1. Create a Discord Bot**
- Follow this guide: https://www.ionos.com/digitalguide/server/know-how/creating-discord-bot/
- Ensure your bot has access for `Message Content Intent`
- After created, invite bot into your server with `Read Messages/View Channels` permission. 


**2. Set Up Google Credentials**
- Follow this guide: https://docs.gspread.org/en/v6.0.0/oauth2.html#for-bots-using-service-account
- This repository use `Service Account` as authorize method.


**3. Install dependencies and setup environment variables**
- Install dependencies
    ```sh
    pip install -r requirements.txt
    ```
- Setup environment variables

    Create a copy of `.env.example` , with name `.env` file in the root directory and paste your variables.
    ```env
    BOT_TOKEN=your_discord_bot_token
    ...
    ```


**4. Running the Bot**
```sh
python main.py
```

## Hosting your bot 

This guide helps you host your bot 24/7 on [Render.com](https://render.com/) for free.
1. Deploy your bot on Render using Web Service. Follow: https://docs.render.com/web-services

2. Go to `Settings` -> `Health Checks`, update health check path at `/`. This will ensure that the server isn't detected as idle by the Render and consequently isn't suspended.

## License
Distributed under the MIT License. See LICENSE for more information.


