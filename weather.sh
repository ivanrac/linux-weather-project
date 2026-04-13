
#!/bin/bash

echo "===== $(date) =====" >>/home/ivan/linux-pocasie-projekt/logs/weather.log
curl https://wttr.in/bratislava > /home/ivan/linux-pocasie-projekt/reports/weather.txt
echo "Weather report for Bratislava saved to reports/weather.txt" >> /home/ivan/linux-pocasie-projekt/logs/weather.log
