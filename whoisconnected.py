# -*- coding: utf-8 -*-

__author__ = "Paolo Mattiolo"
__credits__ = ["Paolo Mattiolo","Edmondo Conetta"]
__license__ = "GPL"
__version__ = "0.0.1"
__email__ = "mattiolo@gmail.com"
__status__ = "Development"



import sys
from klein import Klein
from twisted.web.template import Element, XMLString, renderer
from libs.grabber import Grabber
import libs.log


"""
class HelloElement(Element):
    loader = XMLString(
        '<h1 '
        'xmlns:t="http://twistedmatrix.com/ns/twisted.web.template/0.1"'
        '>Hello, <span t:render="name"></span>!</h1>')

    def __init__(self, name):
        self._name = name

    @renderer
    def name(self, request, tag):
        return self._name
"""


app = Klein()

@app.route('/')
def pg_root(request):
    return 'Home page'

"""
@app.route('/whois')
def pg_whois(request):
    return 'Whois'

@app.route('/about')
def pg_about(request):
    return 'Who is connected to RemoteRig'

@app.route('/hello/<string:name>')
def home(request, name='world'):
    return HelloElement(name)
"""

grabber = None


def init():
    grabber = Grabber()
    page = grabber.getInfoPage()
    if page:
        print(page)
    

init()

#release or develop selection
if len(sys.argv) > 1 : 
    resource = app.resource
else:
    app.run("localhost", 8080)

