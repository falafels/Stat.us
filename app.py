from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""

    print(request.form['Body'])
    resp = twilio.twiml.Response()
    if (request.form['Body'] == "Trending"):
        resp = twilio.twiml.Response()
        resp.message("Yo what up")
    else:
        resp.message("Please type Trending")
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
