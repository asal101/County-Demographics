from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json
app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('home.html')
                           
@app.route("/response")
def render_response():
    color = request.args['color'] 
    #The request object stores information about the request sent to the server.
    #args is an ImmutableMultiDict (like a dictionary but can have mutliple values for the same key and can't be changed)
    #The information in args is visible in the url for the page being requested. ex. .../response?color=blue
    if color == 'pink':
        reply = "That's my favorite color, too!"
    else:
        reply = "My favorite color is pink."
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
       
        
    
    
    
    
    
