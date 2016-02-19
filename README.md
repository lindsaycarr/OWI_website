
#OWI Website






To run this application locally, you will need to do the following:

1. Create a virtualenv using python 2.7 and install the requirements in requirements.txt. This can be done as follows while in the project directory:
  1. Run `virtualenv --python=python2.7 env`
  2. Activate your virtualenv (depends on whether linux or windows)
  3. Run `pip install -r requirements.txt`
2. Change to the `instance` directory and create config.py. It should contain the following:
	```python
	DEBUG = True
	
	#this turns off and on the flask-freezer functionality.  If it is True, flask-freezer will 
	#constantly rebuild the static version of the page 
	FREEZE = False
	
	```

Now you can run the application within the virtualenv by executing:
`python run.py`

The application can be accessed at 127.0.0.1:5050/

To generate the pygments css (learn more about pygments here: http://pygments.org/:

1. set the current directory in the shell to the css directory in the static folder
2. activeate the project virtualenv
3. enter the following shell command:
```shell
$ pygmentize -S default -f html > codehilite.css
```

