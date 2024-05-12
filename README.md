# Project Name

Welcome to the Learning Log!

## Installation

1. Clone the repository:
   ```bash
   git clone git@github.com:bnjtgly/learning_log.git
   ```

2. Navigate into the project directory:
   ```bash
   cd learning_log
   ```

3. (Optional) Create a virtual environment:
   ```bash
   python3 -m venv env
   ```

4. Activate the virtual environment (skip this step if not using a virtual environment):
   ```bash
   source env/bin/activate
   ```

5. Install dependencies:
   ```bash
   pip install django
   ```

## How to Run

1. Ensure you're in the project directory.

2. Apply migrations:
   ```bash
   python manage.py migrate
   ```

3. (Optional) Create a superuser for accessing the Django admin interface:
   ```bash
   python manage.py createsuperuser
   ```

4. Start the development server:
   ```bash
   python manage.py runserver
   ```

5. Open your web browser and go to `http://127.0.0.1:8000/` to view the project.
   Once the server is running, you can access the Django admin interface by navigating to http://127.0.0.1:8000/admin in your web browser.

## Additional Information

- For production deployment, make sure to set `DEBUG = False` in `settings.py` and configure your server accordingly.
- For more detailed instructions and documentation, refer to the [Django Documentation](https://docs.djangoproject.com/en/stable/).
