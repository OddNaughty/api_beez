from flask import Flask, request

app = Flask(__name__)
app.config.update(
    DEBUG=True
)


@app.route("/hives/", methods=['POST'])
@app.route("/hive/<hive_id>", methods=['POST'])
def hive_endpoint(hive_id=None):
    print(request.get_json(force=True))
    return "Received some shit o/."


# Launch server with python3 main.py :P.
if __name__ == "__main__":
    app.run(port=9000, debug=True)
