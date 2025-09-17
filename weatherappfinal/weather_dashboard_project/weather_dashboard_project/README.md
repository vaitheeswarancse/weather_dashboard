<<<<<<< HEAD
Weather Dashboard Django Project
--------------------------------

What's included:
- Django project 'weather_dashboard'
- App 'weather_app' with:
  - Search form for city name
  - Fetches current weather from OpenWeatherMap
  - Stores last 5 searches in SQLite (db.sqlite3)
  - Line chart for temperature trends (Chart.js)
  - Dark/Light theme toggle

Setup:
1. Install dependencies:
   pip install -r requirements.txt

2. Open 'weather_dashboard/settings.py' and set your OpenWeatherMap API key:
   OPENWEATHER_API_KEY = 'your_api_key_here'

3. Run migrations:
   python manage.py makemigrations
   python manage.py migrate

4. Start the server:
   python manage.py runserver

5. Visit: http://127.0.0.1:8000/

Notes:
- This is a minimal project scaffold meant for local development and learning.
- Replace SECRET_KEY in settings.py with a secure key for production.
=======
# weather_dashboard
Users can enter a city name. Fetch real-time weather data from a free public API (e.g., OpenWeatherMa . Display temperature, humidity, and condition. Store the last 5 searched cities in the database. Add chart (js based) for temperature trends. Add dark/light theme toggle.
>>>>>>> e2e266c92448178abe8ae3a818a60c8ae139f3f9
