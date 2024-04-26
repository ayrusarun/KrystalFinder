#!/bin/bash

# Export the environment variables
export FLASK_APP=form.py
export FLASK_ENV=production  # or use 'development' if you are in a dev environment but ensure debug is off

# Start the Flask application in the background
nohup python3 form.py > flask_app.log 2>&1 &
