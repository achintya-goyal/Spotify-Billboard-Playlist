# 🎶 Spotify Billboard Playlist Maker

Ever wondered how those **“Top 20 Daily”** playlists on Spotify keep updating?
This project shows you how to build your own automatically generated playlists by **scraping trending songs** from a website and adding them into Spotify via the Spotify Web API.

---

## 🚀 Features

* Scrapes trending songs for a given **year** from Popnable.
* Searches the scraped songs on Spotify.
* Creates a **private playlist** in your Spotify account.
* Saves your authentication token locally (`token.txt`) so you don’t need to log in every time.

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Spotify-Billboard-Playlist.git
cd Spotify-Billboard-Playlist
```

### 2. Install Dependencies

Make sure you have Python 3.7+ installed, then run:

```bash
pip install requests beautifulsoup4 spotipy
```

### 3. Configure Spotify API

1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard).
2. Create a new app → get your **Client ID** and **Client Secret**.
3. Set your **Redirect URI** (must match the one in your code). Example:

   ```
   https://www.google.com/
   ```
4. Replace the placeholders in the code with your `client_id`, `client_secret`, and `redirect_uri`.

---

## 🌐 Configure Headers for Web Scraping

To set the **header** variable in the code:

1. Visit [What Is My Browser](https://www.whatismybrowser.com/detect/what-http-headers-is-my-browser-sending/).
2. Copy your `User-Agent` value.
3. Paste it into the `header` dictionary in the code.

---

## ▶️ Usage

Run the script:

```bash
python main.py
```

1. Enter the year you want songs from (e.g., `2015`).
2. The script will scrape trending songs from Popnable.
3. It will search those songs on Spotify and add them to a **new private playlist** in your account.

---

## 📌 Notes

* On first run, Spotify will ask for authorization and redirect you to your chosen URL.
* Copy-paste the redirected link into your terminal to complete verification.
* A `token.txt` file will be created for future runs (no need to re-authenticate).

---

## ⚠️ Disclaimer

This project is for **educational purposes only**.
Web scraping may break if the source website changes its structure.

---

## 💡 Future Improvements

* Automatically handle missing or misspelled songs.
* Add support for **daily / weekly chart scraping**.
* Option to make playlists **public** instead of private.

---
