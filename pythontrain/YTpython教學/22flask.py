from flask import Flask
app=Flask(__name__)

@app.route("/")#
def home():
    return "hello Flask"

@app.route("/test")
def test():
    return "this is test"


if __name__=="__main__":#如果以主程式運行
    app.run()           #立刻執行







