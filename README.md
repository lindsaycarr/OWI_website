
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
	
	GOOGLE_ANALYTICS_CODE = '' #this only needs to be set on production
	
	```

Now you can run the application within the virtualenv by executing:
`python run.py`

The application can be accessed at 127.0.0.1:5050/

## How to submit more content for the OWI website

1. Within the data directory at https://github.com/USGS-CIDA/OWI_website/tree/master/data there are three YAML files, one for project, people, and partners
2. If you have an update, you can either fork the code and edit locally, and then submit a pull request, or you can even edit the content directly on the github webapp and pubmit the pull request from there.


## How to build the static content

1. in your instance directory change the freeze line to `FREEZE = True`
2. run the application within the virtualenv by executing `python run.py` while in the project directory
3. A `build` directory will appear under the `owi_website` directory that has the contents of the static version of the page, generated using the flask-freezer extension

## Optional: deployment to Amazon S3
(stolen from here: http://www.bernhardwenzel.com/blog/2013/07/01/jinja-with-yaml)

While I’m at it here’s how you could deploy to Amazon s3. Setting up an Amazon S3 container to serve as a host for static websites is a matter of a few steps (and it’s reasonably priced). Instructions can be found on Amazon (basically, create container, enable static hosting, make container public and setup routing if you want to use your own domain).

As a deployment tool I use is `s3cmd` (install with `sudo apt-get install s3cmd` and configure `s3cmd --configure`).

To update my contents the `sync` command can be used. Let’s say the static files are under `<project>/owi_website/build` and I have a S3 bucket named `<BUCKET-NAME>`. To deploy, I do following:

```
cd <project>
s3cmd sync -r owi_website/build/ s3://<BUCKET-NAME>

```

Note: the trailing slash of `owi_website/build/` is crucial. Without it, the command copies the folder including the `build` directory, but to copy only the contents into the root folder of my S3 bucket the slash has to be added.