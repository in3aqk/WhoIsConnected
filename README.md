# WhoIsConnect

Who is connected to my RemoteRig?

This is a web utility that detect who is connected to a [RemoteRig](https://www.remoterig.com) unit.



This utility is useful when a transceiver unit is shared between many HamRadio operators.

The utility is developed in Python 3.x and it includes a Twisted web server.

It's studied to be installed as a service in a RasberryPI client on the same network of the remote RemoteRig Unit.



# System requirements

* Python 3.8 or more
* RaspebrryPI
* Raspian
* Or any Linux / Windows system



## Libraries

The following python libraries are required

### Twisted

The web server is based on twisted and twistd

```bash
# Installation
pip3 install twisted

# BeautifulSoup
pip3 install beautifulsoup4
```



### Klein

The web server is based on klein web server

<https://github.com/twisted/klein>



#### Klein documentation

<https://klein.readthedocs.io/en/latest/>



## Templating

The page templating is developed using Twisted templates

https://twistedmatrix.com/documents/current/web/howto/twisted-templates.html

https://twistedmatrix.com/documents/current/web/howto/


# Admin

The web page style is based on the Pure Admin project

https://github.com/uretgec/pure-admin