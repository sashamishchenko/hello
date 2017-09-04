from bottle import route, run, template

@route('/hello/<name>')
def index(name):
    return template('<b>Hi {{name}}</b>!', name=name)

run(host='192.168.1.103', port=8282)
