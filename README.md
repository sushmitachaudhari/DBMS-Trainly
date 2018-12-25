# cs5200-Trainly
Project : This project was done in the course CS5200 - Database Management System at Northeastern University.

#How to Install

This project  is bbuilt using Python Tornado framework.

The project can be run directly on a system  where python and mysql is installed.
It assumes that MySQL is running on port 3306, if not you can change the setting in main.py  file

Make sure to install following dependencies:
*torndb
*mysqlclient

Once all the dependencies are installed, the application can be run by executing main.py


How To Run:
To run this application, you have to create a database named "project" in mysql first.
execute all the ddl and dml sql statement.
After that, run main.py,

Go to  'http://localhost:8000/' in your browser, then you will get into the login page.

Application Description:
There are three python files that take the main functions.

main.py will connect to the database and do all settings and connect all parts in this program.

handlers.py will bundle differnt route to exact handlers in views.py

view.py have all handlers, which will load in the background, connecting database, get or update data, and present the data in the html files if needed.

templates directory includes all the html files, which will present differnt pages.

static directory includes css file that define the style used in html files.


DEMO VIDEO:
https://www.youtube.com/watch?v=ywgwDgic9z0&feature=youtu.be
