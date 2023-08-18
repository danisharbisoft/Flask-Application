# Flask-Application
This is a simple CRUD TODO app.
You can use it to add some tasks which you have to do, moreover you can update and delete them too.

It has the following directories/files:


1. app.py

2. app_support
   -controllers
       .init.py
      .task_controllers.py
      .user_controllers.py
   -models
      .init.py
      .user.py
      .tasks.py
    .init.py
3.Static
  -css
    .style.css
  -js
    .script.js
    
4.Templates
   tasks:
     -base.html
     -index.html
     -error.html
     -update.html

   auth:
       -first.html
       -login.html
       -register.html


1.App.py:
        This initialises the Flask app and registers the blueprint

2.app_support:
         controllers:
                    init.py:
                                   This has the blueprint defined
                    task_controllers.py:
                                        This has the controllers for the Todo table
                     user_controllers.py:
                                        This has the controllers for the login/register
                     
          models:
               init.py:
                       This has the database initialised
              tasks.py:
                                        This has the models for the Todo table
               user.py:
                                        This has the models for the login/register
                     
               
               


3.Static:
        css:
          Contains some basic Css for styling the page
        js:
          Contains Javascript for toggling the submit button

4.Templates:
          tasks:
             error.html:
                        Contains the layout error page
             base.html:
                      Contains the layout for all html files.
             index.html:
                       Decides how the main homepage will look
             update.html:
                       Decides how the page for updating an entry will look
            auth:
                 first.html:
                            This is the first page the user sees when app loads.
                  login.html:
                            Layout for login page
                  register.html:
                               layout for register page

 
  SETUP Instructions:
  -Clone the repository to your system
  -Create and activate a virtual environment
  -Download SQLITE or any other SQL program which you wish to work with
  -Download Flask and flask_sqlalchemy using pip
  -Initialitise a database(For this navigate to the root directory. Switch to the python console. Import app from app and from app_support.models import db. Then run the following commands:
   with app.app_context():
      db.create_all
  -Make changes to the code and send a PR.
