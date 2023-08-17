# Flask-Application
This is a simple CRUD TODO app.
You can use it to add some tasks which you have to do, moreover you can update and delete them too.

It has the following directories/files:


1. app.py

2. app_support
   -controllers
      .controllers.py
   -models
      .models.py
   
3.Static
  -css
    .style.css
  -js
    .script.js
    
4.Templates
  -base.html
  -index.html
  -update.html


1.App.py:
        This initialises the Flask app and registers the blueprint

2.app_support:
         controllers:
                    controllers.py:
                                   This handles application's logic and acts as intermediaries between the model (data) and the view (user interface).
          models:
                  models.py:
                            This file defines the database model.



3.Static:
        css:
          Contains some basic Css for styling the page
        js:
          Contains Javascript for toggling the submit button

4.Templates:
          base.html:
                   Contains the layout for all html files.
          index.html:
                    Decides how the main homepage will look
          update.html:
                    Decides how the page for updating an entry will look

 
  SETUP Instructions:
  -Clone the repository to your system
  -Create and activate a virtual environment
  -Download SQLITE or any other SQL program which you wish to work with
  -Download Flask and flask_sqlalchemy using pip
  -Initialitise a database(For this navigate to the root directory. Switch to the python console. Import app from app and from app_support.models import db. Then run the following commands:
   with app.app_context():
      db.create_all
  -Make changes to the code and send a PR.
