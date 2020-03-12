# Flask

* Flask is a micro-framework written in Python
* Makes the process of designing a request relatively easy
* Flask is designed in terms of routes - routes are the pages that are at the
end of the URL of a website
* When you set up a route in Flask, the function directly below the route
statement is the function that runs
* `export FLASK_APP=application.py` is a line that sets the FLASK_APP
environment variable for your application
47:15: routes0 - a Flask app with multiple routes
49:30: routes1 - Flask app that passes a variable through from the URL
53:55: templates - using HTML templates
* Flask only looks for templates in a folder called templates in the same
directory as the application
1:15:00: HTML Jinja template with link to another Flask route
1:18:15: HTML layout template
1:23:15: Flask form
* When you submit data via GET, it gets put in the URL - not a good idea if
you're submitting sensitive data
1:40:00: Flask app using session data
* Session variables allows you to store data that is specific to particular
users
