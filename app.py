from flask import Flask, request, redirect
import twitter
import twilio.twiml

app = Flask(__name__)

#Credentials to access Twitter API
#######
 ######
#######
 ######
@app.route("/", methods=['GET', 'POST'])
def main():
    """Respond to incoming calls with a simpled text message."""
    trends = api.GetTrendsWoeid(1)
    message = ''
    topTrends = []
    for i in xrange(5):
        message += ' (' + str(i + 1) + ') ' + trends[i].name +'\n'



    #print(trends)

    print(request.form['Body'])
    resp = twilio.twiml.Response()

    user_input = request.form['Body'].strip()
    if (user_input == "Trending"): #If we text "Trending"
        resp = twilio.twiml.Response()       #Then this block runs
        resp.message("Here are the top 5 trending tweets worldwide!")
        resp.message(message + "Enter a trending topic:") #REPLACE WITH TOP 5 TRENDS
                    #   resp.message("Please select a trend (1-5): ")
        #resp.message("Enter a trending topic: ")

    else:
        results = api.GetSearch(raw_query= "q=" + (user_input) + "&result_type=popular&count=1")
        #resp.message("Please type Trending")
        for x in results:
            resp.message(str(x.text).encode("utf-8"))


        #resp.message(results)
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
