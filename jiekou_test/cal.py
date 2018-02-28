from flask import Flask,request
from flask import redirect
app=Flask(__name__)
@app.route('/plus')
def plus():
    x=request.args.get('x',type=int)
    y=request.args.get('y',type=int)
    return str(x+y)
@app.route('/sub')
def sub():
    x = request.args.get('x', type=int)
    y=request.args.get('y',type=int)
    return str(x-y)

if __name__=='__main__':
    app.run(threaded=True)