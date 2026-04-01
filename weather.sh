#!/bin/bash

echo "===== $(date) =====" >> logs/weather.log
curl https://wttr.in/bratislava > reports/weather.txt
echo "Weather report for Bratislava saved to reports/weather.txt" >> logs/weather.log