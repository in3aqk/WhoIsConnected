# -*- coding: utf-8 -*-

__author__ = "Paolo Mattiolo"
__credits__ = ["Paolo Mattiolo", "Edmondo Conetta"]
__license__ = "GPL"
__version__ = "0.0.1"
__email__ = "mattiolo@gmail.com"
__status__ = "Development"


import sys

from klein import Klein
from twisted.web.static import File
from twisted.python.filepath import FilePath
from twisted.web.template import (Element, XMLFile, XMLString, flattenString,
                                  renderer, tags)

import libs.log
from libs.grabber import Grabber
from libs.controllers import Pages
from libs.controllers import HomeController
from libs.controllers import AboutController

app = Klein()
pages = Pages()

@app.route('/')
def main_page(request):
    return pages.get_page("dashboard.html")

@app.route('/about')
def about_page(request):
    return pages.get_page("about.html")


@app.route('/assets/', branch=True)
def static(request):
    return File("./html/assets")


@app.route('/images/', branch=True)
def images(request):
    return File("./html/images")


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
        grabber.getHeadInfo()


init()

# release or develop selection
if len(sys.argv) > 1:
    resource = app.resource
else:
    app.run("localhost", 8080)
