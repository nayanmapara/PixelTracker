# SPY-Pixel Tracking Application

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

## Database Configuration

The application uses a MongoDB database to store tracking data. You can configure the MongoDB connection by setting the following environment variables:

- `MONGO_URI`: The URI for connecting to the MongoDB database.

## Pixel Tracking Endpoint

The tracking pixel is served at the `/pixel` endpoint. You can embed the pixel in an email by using the following HTML code:

```html
<img src="http://yourdomain.com/pixel" alt="" width="1" height="1">
```

When the pixel is loaded, it will log the user interaction and record the tracking data in the database.

You can also make it spcific to a user by adding a query parameter to the pixel URL:

```html
<img src="http://yourdomain.com/pixel?id={ANY_ID}" alt="" width="1" height="1">
```

## Running the Application

To run the application, you can use the following command:

- Install the required packages:

    ```bash
    python -m pip install -r requirements.txt
    ```

- Run the Flask application:
    
    ```bash
    python app.py
    ```