# -*- coding: utf-8 -*-

__author__ = "Paolo Mattiolo"
__credits__ = ["Paolo Mattiolo", "Edmondo Conetta"]
__license__ = "GPL"
__version__ = "0.0.1"
__email__ = "mattiolo@gmail.com"
__status__ = "Development"


import sys

from klein import Klein
from twisted.python.filepath import FilePath
from twisted.web.static import File
from twisted.web.template import (Element, XMLFile, XMLString, flattenString,
                                  renderer, tags)

import libs.log
from libs.controllers import AboutController, HomeController, Pages
from libs.grabber import Grabber

app = Klein()
pages = Pages()


@app.route('/')
def main_page(request):
    return pages.get_page("dashboard")


@app.route('/about')
def about_page(request):
    return pages.get_page("about")


@app.route('/assets/', branch=True)
def static(request):
    return File("./html/assets")


@app.route('/images/', branch=True)
def images(request):
    return File("./html/images")


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
