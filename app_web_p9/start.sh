#/bin/sh
gunicorn app_web_p9.wsgi:application --bind 0.0.0.0:$PORT
