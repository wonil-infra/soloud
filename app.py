from flask import Flask
import socket   # 호스트네임 가져오기용

app = Flask(__name__)

@app.route("/")
def hello():
    hostname = socket.gethostname()
    return f"Hello from soloud! (pod: {hostname})"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

