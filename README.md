# Flask-Application

This is a simple CRUD TODO app. You can use it to add some tasks which you have to do, and you can also update and delete them.
It will ask you to register and log in and will remember your tasks.

## Directory Structure

The application has the following directories/files:

1. **app.py**: This initializes the Flask app and registers the blueprints along with other registrations.

2. **controllers**:
    - **task_controllers.py**: This file contains the controllers for the Todo table.
    - **user_controllers.py**: This file contains the controllers for the login/register.

3. **models**:
    - **user.py**: This file contains the models for the login/register page.
    - **tasks.py**: This file contains the models for the Todo table.

4. **Static**:
    - **css**: Contains basic CSS for styling the page.
    - **js**: Contains JavaScript for toggling the submit button.

5. **Templates**:
    - **tasks**:
        - **error.html**: Contains the layout for the error page.
        - **base.html**: Contains the layout for all HTML files.
        - **index.html**: Defines how the main homepage will look.
        - **update.html**: Defines how the page for updating an entry will look.
    - **auth**:
        - **first.html**: This is the first page the user sees when the app loads.
        - **login.html**: Layout for the login page.
        - **register.html**: Layout for the register page.

## Setup Instructions:

- Clone the repository to your system.
- Create and activate a virtual environment.
- Download SQLite or any other SQL program you wish to work with.
- Download Flask and flask_sqlalchemy using pip.
- To Initialize a database follow the following steps:
  - Navigate to the root directory.
  - Switch to the Python console.
  - Import `app` from `app`.
  - Import `db` from `models`
  - Run the following commands:
    ```python
    with app.app_context():
        db.create_all()
    ```
- Run your server
- Test the app with your TODOs.
- Run Migrations if you make changes to models.
- Make changes to the code and send a pull request.

