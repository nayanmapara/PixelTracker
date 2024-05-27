# Pixel Tracking Application

This is a Flask application that uses a "pixel" to track and log user interactions with emails. The application records various details such as IP address, user agent, referrer, and more whenever the tracking pixel is loaded.

## Features

- Track and log user interactions with a spy pixel embedded in emails.
- Record IP address, user agent, referrer, and other HTTP headers.
- Perform GeoIP lookups to get geographic location information based on IP address.
- Store tracking data in a MongoDB database.

## Requirements

- Python 3.x
- Flask
- Flask-PyMongo
- requests
- MongoDB