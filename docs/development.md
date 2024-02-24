## How to API clientdb, 
### ClientDB
curl https://schools:sQuola@clientdb-staging.heanet.ie:8443/api/clients/get_by_ip/193.1.1.1
https://wiki.heanet.ie/ClientDB_Developer_Docs#ClientDB_API
schools:sQuola

### Junos Space/CSD
Space -> Role Based Access Control -> User Accounts -> set up new user
https://wiki.heanet.ie/Space/CSD_API
* example:
https://193.1.255.5/api/space/managed-domain/managed-elements
in conductor.heanet.ie: walter-app:H0BmIkxSs

### RT
https://rt4-staging.heanet.ie:8443/ -> API walter:FriDay13th
walter:FriDay13th
* RT REST API documentation: https://rt-wiki.bestpractical.com/wiki/REST. Note that it also has recomendations for clients; e.g. Python client 


### Django REST Swagger
* https://github.com/m-haziq/django-rest-swagger-docs
* https://django-rest-swagger.readthedocs.io/en/latest/

### How to string in API URL
* https://stackoverflow.com/questions/11894916/django-url-pattern-string-parameter
* If the function you are calling has an input of 'hostname', then the URL pattern, the regex, has to have the keyword <hostname>

### How to log
* in each file
`
import logging
logger = logging.getLogger(__name__)

class PintView(TemplateView):
    
    def get_context_data(self, *args, **kwargs):
        logger.debug('Only %d pints of ice cream left.' % pints_remaining)

`

* in settings.py (or way better in settings_development.py)
`
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        # Your logging configuration only captures logs within the django namespace.
        # https://stackoverflow.com/questions/36571284/why-django-logging-is-not-working
        #'django': {
        #    'handlers': ['console'],
        #    'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        #},
        # So that we capture ANY namespace
        '': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
    },
}
`
* Reference: https://stackoverflow.com/questions/36571284/why-django-logging-is-not-working


### How to import 
The error 'SyntaxError: import * only allowed at module level' happens if you try to import * from within a function. See [stack overflow](https://stackoverflow.com/questions/39342990/python-import-or-a-list-from-other-level)
If you import * in a file, then that is fine. 

### Markdown cheatsheet
* [Github guide on Mastering Markdown](https://guides.github.com/features/mastering-markdown/)


### Coverage configuration files, include, exclude, etc.
* http://coverage.readthedocs.io/en/latest/config.html#

### How to scrap HTML
* https://www.dataquest.io/blog/web-scraping-tutorial-python/

### How to find email address in a string
* https://stackoverflow.com/questions/17681670/extract-email-sub-strings-from-large-document
* https://developers.google.com/edu/python/regular-expressions


### Django landing page
* In root urls, point '' to urls of app where landing page is
* In app where landing page lives, add urlpattern: `url(r'^$', views.ne_list, name='index'),`
* # https://tutorial.djangogirls.org/en/django_urls/

### Git, see the remotes
* In the root of the repository `git remote -v`
Reference: https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes


### How to install atom
* Using snap `sudo snap install --classic atom`
Reference: https://insights.ubuntu.com/2017/05/11/atom-is-now-available-as-a-snap-for-ubuntu/


### How to write Git commit messages
I did like this article, enjoyed his tone
* [How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/)
* Then, if you do a Google search you find [Writing good commit messages](https://github.com/erlang/otp/wiki/Writing-good-commit-messages)
* [How To Write A Proper Git Commit Message](https://medium.com/@steveamaza/how-to-write-a-proper-git-commit-message-e028865e5791)


### How to auto-login in Xubuntu 16.04
https://gist.github.com/mishaAe/0019381addb8bebfcaaa64b45eb5f117


### List of Python packages
There is a bug in Ubuntu (see [stack overflow](https://stackoverflow.com/questions/39577984/what-is-pkg-resources-0-0-0-in-output-of-pip-freeze-command) and [Ubuntu](https://bugs.launchpad.net/ubuntu/+source/python-pip/+bug/1635463) that renders pip freeze incorrectly. Please do issue `pip freeze` as:
`pip freeze | grep -v "pkg-resources" > requirements.txt`
