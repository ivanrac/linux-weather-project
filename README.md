# 🌦️ Linux Weather Automation Project

A Linux-based automation and web application project that retrieves and displays weather data using Bash, Python, and a Flask web interface.

This project started as a simple Bash automation (Release 1) and was later extended into a web application with REST API integration (Release 2).

---

## 🚀 Project Overview

- Automated weather data collection using Bash and cron
- REST API integration (yr.no)
- Flask web application for displaying weather data
- Logging and reporting system
- Structured project organization using Git

---

## 🛠️ Technologies Used

- Linux (AlmaLinux)
- Bash
- Python 3
- Flask
- REST API (yr.no)
- cron
- systemd
- tmux
- curl
- Git

---

## 📂 Project Structure

app.py # Flask application
weather.sh # Bash automation script
templates/ # HTML templates
docs/ # Documentation and screenshots
tests/ # API test scripts
sample-data/ # Sample JSON data
archive/ # Old/experimental files
logs/ # Sample logs
reports/ # Sample outputs


---

## 🔄 Project Evolution

### 🔹 Release 1 – Bash Automation
- Fetch weather data using `curl` from wttr.in
- Save output to file
- Log execution with timestamps
- Automate execution using cron

📁 See: `docs/release-1/`

---

### 🔹 Release 2 – Flask Web Application
- Flask web server for displaying weather
- Integration with yr.no REST API
- JSON parsing and data extraction
- HTML rendering with templates
- Basic UI styling

📁 See: `docs/release-2/`

---

## 🌐 Features

- Web interface for weather display
- Live weather data from API
- JSON data processing
- HTML rendering using Flask
- Background automation via cron/systemd
- Logging and reporting

---

## 📸 Documentation

Detailed implementation steps and screenshots are available in:

- `docs/release-1/`
- `docs/release-2/`

---

## 📌 Future Improvements

- City selection support
- Enhanced UI
- Better error handling
- API response caching

---

## 📎 About

This project was created as part of hands-on learning in Linux, automation, backend development, and API integration.