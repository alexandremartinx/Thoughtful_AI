#!/bin/bash
set -e

echo "===> Running tests..."
pytest test_package.py test_cases/ || echo "Some tests failed, but continuing..."

echo "===> Starting Flask app..."
python3 app/app.py &

sleep 5

echo "===> Opening browser..."
xdg-open app/index.html || echo "Please open the file manually: app/index.html"

# Keep the container running
tail -f /dev/null