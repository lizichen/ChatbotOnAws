import sys, os, bottle

sys.path = ['/var/www/restapi/'] + sys.path

# Change working directory so relative paths (and template lookup) work again
os.chdir(os.path.dirname(__file__))

import apiserver         # This loads the REST framework that you have implemented as apiserver.py (The file that handles get/post requests)

# ... build or import your bottle application here ...
# Do NOT use bottle.run() with mod_wsgi
application = bottle.default_app()
