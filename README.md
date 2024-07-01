# sticky_notes_app

This repository contains the source code for a sticky notes application I created as part of a skills bootcamp in software engineering. It will allow users to create, read, edit and delete posts that all other users will also be able to see.

## Description
The application first requires users to log in before proceeding beyond the home page. Djangos built in authentication form has been used to ensure that any user must log in using their correct details before being able to proceed. The option is also there for new users to create a new account using a user creation form.

Once logged in, users can see a brief overview of every post that has been created previously whether that be by the user themselves, or other users. The user can click on any of the posts in order to see the full thing, or they can create a post of their own.

If a user opts to view one of their own posts in full, the option is there for them to delete or edit the post should they desire. These two options only appear if the username that the user is logged in as matches the author of the post. Otherwise, the user can only read the post.
Superusers can also be created in order to manage posts and users. A superuser will be able to access the Django admin panel. From here, they can see both a list of users, and a list of posts. They can delete, update or create both posts and user accounts.

This application will be useful as a way of communication across small and medium sized businesses. Particularly those who have several office locations or have employees who work from home. By making sure all employees are signed up to the app, it can help ensure that all employees are up to date with the latest events at the company. The managers of the company can also sign up as superusers so they can monitor posts and users and ensure everyone is using the application appropriately.

## Getting Started
### Dependencies
In order to run this programme, you will need to first install:
* asgiref==3.8.1
* Django==5.0.6
* flake8==7.1.0
* mccabe==0.7.0
* pycodestyle==2.12.0
* pyflakes==3.2.0
* sqlparse==0.5.0
* tzdata==2024.1

### Installing
To install this app:
1.	Press the big green “<> Code” button to expand the drop-down menu
2.	Click Download Zip
3.	In this Zip folder open the sticky_notes_app-main directory.
4.	Then move the “Task 24” directory to a relevant location on your device.

### Executing Programme
1.	In your terminal ensure you are currently within the “Task 24” directory.
2.	Inside the terminal navigate in to sticky_notes_app.

  	'''

  	cd sticky_notes_app

  	'''

4. Make the any migrations to the database

    '''

    py manage.py makemigrations

    py manage.py migrate

    '''

6. Run Server

    '''
   
    py manage.py runserver
   
    '''
