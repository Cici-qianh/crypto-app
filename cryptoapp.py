""" This python3.5 module will create the website homepage of the APP #
"""

import os.path
import cherrypy

#Obtain the directory path of this module:
cwd = os.path.dirname(os.path.abspath(__file__))
parentdir = os.path.dirname(cwd)
sitedir = os.path.join(parentdir, 'site')

# Start a web server with cherrypy:
class CryptoApp(object):
    @cherrypy.expose
    def index(self):
        return open(os.path.join(sitedir,"html/index.html")).read()

class Generator(object):
    @cherrypy.tools.accept(media = 'text/plain')
    @cherrypy.expose
    def GET(self):
        return
        
if __name__ == "__main__":
    conf = {
        '/': {'tools.staticdir.root': sitedir},
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': 'static'
        },
        '/generator': {
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        }
    }
webapp = CryptoApp()
webapp.generator = Generator()
cherrypy.quickstart(webapp, '/', conf)