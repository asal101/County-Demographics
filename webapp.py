from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json
app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('home.html')
                           
@app.route("/response")
def render_response():
    #color = request.args['color'] 
    
   # if color == 'pink':
        reply = "That's my favorite color, too!"
  #  else:
   #     reply = "My favorite color is pink."
    return render_template('response.html', response = reply)
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
    get_state_options:
      ListOfStates:
        options = options + [0] "State"
        for state in states:
        if state["State"]  < first_state:
            first_state = state ["State"]
       return first_state     
