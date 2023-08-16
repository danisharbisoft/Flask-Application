# Flask-Application
This is a simple CRUD TODO app.
You can use it to add some tasks which you have to do, moreover you can update and delete them too.

It has the following directories/files:

1.Instance
  -test.db
2.Static
  -css
    .style.css
  -js
    .script.js
3.Templates
  -base.html
  -index.html
  -update.html
4. app.py



1.Intsance:
          This directory contains test.db which is the database file containing the table for your tasks. It has been created by integrating it with SQLite. I chose this because I
          I had worked with SQLite before as well and find it conveneient to integrate it within my web apps.

2.Static:
        css:
          Contains some basic Css for styling the page
        js:
          Contains Javascript for toggling the submit button

3.Templates:
          base.html:
                   Contains the layout for all html files.
          index.html:
                    Decides how the main homepage will look
          update.html:
                    Decides how the page for updating an entry will look

4.App.py:
        This contains the main code for the app including the model and different routes.

  The application uses SQLAlchemy as an ORM library to use SQLite databases using python models.

  SETUP Instructions:
  -Clone the repository to your system
  -Create and activate a virtual environment
  -Download SQLITE or any other SQL program which you wish to work with
  -Download Flask and flask_sqlalchemy using pip
  -Initialitise a database
  -Make changes to the code and send a PR.
