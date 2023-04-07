FROM python:3.9.12
# Environment variable set for production.
ENV ENV PRODUCTION
# Setting work directory.
WORKDIR /app
COPY . /app
RUN chmod +x start.sh
# Installing dependencies.
RUN pip install -r requirements.txt
# Collecting static files.
RUN python manage.py collectstatic --noinput
# Running gunicorn.
CMD ["./start.sh"]
