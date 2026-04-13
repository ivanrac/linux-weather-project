# Release 2: Technical Implementation Steps

### Phase 1: Environment Setup
1. Verified Python3 installation on AlmaLinux VM
2. Installed python3-pip package
3. Installed Flask using pip3
4. Prepared environment for building a local web application

### Phase 2: Flask Core Development
5. Created the first Flask application in app.py
6. Added the root route "/" returning a simple text response
7. Started the local Flask application on port 5000
8. Ran the Flask application locally using python3 app.py
9. Application started on localhost:5000
10. Verified that the Flask app returns a response in the browser
11. Installed and used tmux for multi-terminal workflow
12. Ran Flask app and tested it using curl in parallel
13. Verified Flask application response using curl
14. Confirmed request handling and response flow in the Flask server

### Phase 3: UI & Data Integration
15. Documented working application with screenshots
16. Updated Flask app to read weather data from reports/weather.txt
17. Connected the original Bash project output with the Flask application
18. Displayed weather output in the browser/HTTP response using preformatted text
19. Updated Flask app to return a simple HTML page
20. Embedded weather data inside HTML structure
21. Verified HTML response using curl command
22. Created templates/index.html for HTML structure
23. Used Flask render_template to separate HTML from Python code
24. Successfully displayed weather data using template
25. Added basic CSS styling to improve UI appearance

### Phase 4: Professional API Migration (yr.no)
26. Observed dependency on external weather service (wttr.in)
27. Identified potential timeout issues with external data source
28. Verified correct rendering of weather data with sufficient terminal width
29. Observed formatting issues caused by narrow terminal view
30. Tested yr.no weather API successfully using curl
31. Retrieved JSON forecast data for Bratislava
32. Confirmed transition from wttr text output to structured API data
33. Created Python script to parse API JSON response
34. Extracted first timestamp and temperature from forecast data
35. Replaced complex one-liner with readable Python script
36. Created Python script (test_api.py) to process weather API data
37. Loaded JSON data from forecast.json using json.load()
38. Accessed first forecast entry from timeseries list
39. Extracted weather details (temperature, wind speed, humidity)
40. Used variable "details" to simplify access to nested JSON data
41. Successfully printed weather data (time, temperature, wind, humidity)
42. Connected Flask app directly to yr.no API
43. Added User-Agent header required by the API
44. Replaced wttr text source with structured JSON API data
45. Extracted and displayed temperature, wind speed, and humidity in the web app
46. Verified API-based HTML response through Flask using curl