# COMP6015_project
SWAT testbed project 

# Run this command to run the backend code:
gunicorn --bind 0.0.0.0:8000 --timeout 300 wsgi:app