import sys

from klein import Klein
app = Klein()

@app.route('/')
def pg_root(request):
    return 'I am the root page!'

@app.route('/about')
def pg_about(request):
    return 'I am a Klein application!'

#release or develop selection
if len(sys.argv) > 1 : 
    resource = app.resource    
else:
    app.run("localhost", 8080)

