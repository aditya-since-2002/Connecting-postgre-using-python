# Connecting postgre using python
 

[![N|Solid](https://www.python.org/static/img/python-logo@2x.png)](https://code.visualstudio.com/docs/python/environments)

- Hey there
-  ✨let's begin✨

## Setting up virtual enviroment using cmd

**If you don't have pip installed follow below step**

> sudo apt-get install python-pip

**Installing Virtual Env**

> pip install virtualenv

**Check your Installation**

> virtualenv --version

**Create the virtual env**

>virtualenv virtualenv_name

**To activate the enviroment**

>Go to the file using CMD and in the scripts type **activate**

**To deactivate the enviroment**

>Write **deactivate** in the running virtual enviroment


## What is Virtual Enviroment?

To read more about virtual enviroment [read here](https://docs.python.org/3/library/venv.html#:~:text=A%20virtual%20environment%20is%20a%20directory%20tree%20which%20contains%20Python,as%20expected%20with%20virtual%20environments.)

## What is postgresql?

To read documentation about postgresql [read here](https://www.postgresql.org/docs/current/index.html)

## What is python?

To read documentation about python [read here](https://docs.python.org/)

## What is pycopy2?

To read documentation about pscopy2 [read here](https://pypi.org/project/psycopg2/)

## Connection between python and postgresql

**psycopg2.connect(dbname="postgres",user="postgres",password="####",host="localhost",port="5433")**

>dbname is the name of the databasefile
>user is the name that user has registred for the username in postgres
>password is the key that the user used while registering on postgres
>host is the place where the data is going to be stored 
>port is a virtual point where network connections start and end.






