echo "sleep of 80 seconds"
sleep 80

flask db init
flask db migrate -m "initial migration"
flask db upgrade
gunicorn app:app --bind 0.0.0.0:5000