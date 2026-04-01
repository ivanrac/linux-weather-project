# 🌦️ Linux Weather Automation Project

## 📌 Overview
This project demonstrates a simple Linux-based automation solution that retrieves weather data from the internet and processes it using a Bash script.

The script fetches weather information for Bratislava using `curl` and automatically saves the output into a file while logging execution details.

---

## ⚙️ Technologies Used
- Linux (AlmaLinux)
- Bash scripting
- curl (HTTP requests)
- cron (task scheduling)

---

## 🚀 Features
- Fetch weather data from the internet (wttr.in)
- Store weather output into a file
- Log script execution with timestamps
- Automatically run script using cron (every minute)

---

## 📂 Project Structure

linux-pocasie-projekt/
├── weather.sh
├── README.md
├── logs/
├── reports/
└── docs/
    ├── postup.txt
    └── screenshots/

---
## ▶️ How to Run

### Run manually:
```bash
./weather.sh

Check weather output:
   cat reports/weather.txt
   
Check logs:
   cat reports/weather.txt
   
⏱️ Automation (cron)

The script is scheduled using cron:
    * * * * * /home/ivan/linux-pocasie-projekt/weather.sh
	
This runs the script every minute.

🔄 Future Improvements (Version 2)

    Use a real weather API (e.g. yr.no)
    Add support for dynamic city input
    Improve script output formatting
    Build a simple web interface
	
📸 Screenshots

(Screenshots will be added in the docs/screenshots folder)	
 
## Documentation

Detailed implementation steps are available in:

- docs/postup.txt

Project screenshots can be found in:

- docs/screenshots/ 