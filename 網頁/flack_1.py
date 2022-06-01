from flask import Flask
app = Flask(__name__)

#路由
"""
def index():
    return 'Hello'
app.add_url_rule('/', 'index', index)
"""

@app.route('/index.html')
@app.route('/')
def index():
    return 'Hello'

@app.route('/about')
def about():
    return '關於我'

@app.route('/faq/')
def faq():
    return('問題集')

if __name__ == '__main__':
    app.run()   #啟動伺服器
