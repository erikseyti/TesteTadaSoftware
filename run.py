from app import app
# from gevent import pywsgi
# from geventwebsocket.handler import WebSocketHandler
# server = pywsgi.WSGIServer(('0.0.0.0', 8080), app, handler_class=WebSocketHandler)
# server.serve_forever()
app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)
