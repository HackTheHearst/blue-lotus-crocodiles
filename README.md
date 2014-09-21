Time Capsule: The Stela of Prince Wepemnofret
==========
![Time Capsule screenshot](https://raw.githubusercontent.com/angelausy/blue-lotus-crocodiles/master/static/screenshot.png)
[View the demo version of this application](http://crocodiles.herokuapp.com)

## The project
Time Capsule is an educational tool with two components: a matching game intended to encourage student learning, and a teacher-guided activity to make sense of Ancient Egyptian life. The application is built with Flask, a Python web framework, and uses jQuery and d3.js for the interactive features.

## Installation (Mac OSX)
To run the application with your computer as a server, you'll need Python installed. First, open the Terminal clone this repository:

    git clone https://github.com/angelausy/blue-lotus-crocodiles.git

Next, create a virtual environment for the application and its dependencies:

    virtualenv env
    source env/bin/activate
    pip install flask
    pip install -r requirements.txt

You should then be able to launch the app with your computer as the server. When you type:

    python app.py

You should see:

    * Running on http://127.0.0.1:5000/
    * Restarting with reloader

## The team
Time Capsule was created for UC Berkeley's 2014 [Hack the Hearst](http://hackthehearst.berkeley.edu/) event.
* [Angela Lau](https://twitter.com/a2lau)
* [Casondra Sobieralski](http://dancing-octopus-health-media.com/)
* [Michael Katz](https://www.linkedin.com/pub/michael-katz/6/215/408)
* [Maggie Shine](http://twitter.com/magksh)
