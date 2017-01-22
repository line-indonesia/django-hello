##django-hello
This repository demonstrates how to create a basic web application using Django Framework. Additionally, this sample also covers the topic of how to deploy a Django project into Heroku.

### How do I get set up?

- To run a Django application, you need to have Python, Django, and Pip installed in your machine.
- Run Server

    ```bash
    $ python manage.py runserver
    ```
- Use

    By default the server will serve at:
    > http://localhost:8000/
    
    You can make the server greets your name by calling:
    > http://localhost:8000/hello?name=<your_name>
    
### How to deploy to Heroku?

- Everytime you want to deploy a Django application to Heroku, you need to provide a `Procfile` file. Please see the sample in the project's root directory.
- When pushing a Django project to Heroku, Heroku downloads the dependency packages from ```requirements.txt```. Therefore, you need to provide this.
- Heroku also conducts ```collectstatic``` method from manage.py. Therefore you need to add the following lines in ```settings.py``` file:

    ```python
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)
```

    and ```django.contrib.staticfiles``` into the INSTALLED_APPS list.
    
- Last, you need to provide a directory named ```static``` in the same directory with ```settings.py```. As git disregards empty directory, you can add an empty ```.gitignore``` file into this directory.

### How do I contribute?
- Add your name and e-mail address into CONTRIBUTORS.txt