# ghost-flask
A Flask based version of the Ghost markdown editor.
I wanted to rebuild my website on Flask but I was a big fan of Ghost so I wanted to continue using their editor.
I used timsayshey/Ghost-Markdown-Editor and added some styling to make it look the Ghost's editor.
The schema is based loosely off the schema that ghost uses so that porting over posts will be easier

## Getting set up
You will need virtualenv for the following to work.
Run these commands while inside the project's working directory:

```
make env
. env/bin/activate
python db_create
python run.py
```
