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
## 🌐 How to Run & Access the Application

To run the Flask application in a virtualized environment (like VirtualBox) and access it from your host machine (Windows/Mac), follow these steps:

### 1. Host-to-VM Networking (VirtualBox Settings)
Before starting, ensure your Virtual Machine is visible to your host computer:
* Go to **Settings** -> **Network** -> **Adapter 1**.
* Attached to: **Bridged Adapter** 
* This gives your VM its own IP address in your local network (e.g., `192.168.31.22`).

### 2. Configure AlmaLinux Firewall
AlmaLinux blocks incoming traffic by default. You must open port `8080` to allow your host browser to connect:
```bash
sudo firewall-cmd --add-port=8080/tcp --permanent
sudo firewall-cmd --reload

3. Launch the Application
Run the following commands in your project folder. We use --host=0.0.0.0 to tell Flask to listen on all network interfaces (not just internal localhost).

Bash
# Optional: Clear the port if it's already in use
sudo fuser -k 8080/tcp 2>/dev/null

# Start the Flask app
flask run --host=0.0.0.0 --port=8080
4. Access via Browser
Once the server is running, find your VM's IP address (ip addr show enp0s3) and open it in your host machine's browser:

URL: http://<YOUR_VM_IP>:8080 (e.g., http://192.168.31.22:8080)

🛠️ Quick Fixes
Port already in use: Use sudo fuser -k 8080/tcp to kill the ghost process.

Connection Refused: Ensure you used --host=0.0.0.0 and that your Firewall is configured to allow port 8080.

Host cannot ping VM: Double-check that your Network Adapter is set to Bridged and not NAT.

## 📎 About

This project was created as part of hands-on learning in Linux, automation, backend development, and API integration.