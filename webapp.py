from flask import Flask, request, Markup, render_template
import os
import json
app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('home.html')
                           
@app.route("/response")
def render_response():
    
    
   # color = request.args['color'] 
    
    
    #The request object stores information about the request sent to the server.
    #args is an ImmutableMultiDict (like a dictionary but can have mutliple values for the same key and can't be changed)
    #The information in args is visible in the url for the page being requested. ex. .../response?color=blue
    
    
   # if color == 'pink':
   #     reply = "That's my favorite color, too!"
  #  else:
  #      reply = "My favorite color is pink."
  #  return render_template('response.html', response = reply)

    
  def get_state_options():
    listOfStates=[]
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data) 
    for county in counties:
        if not (county["State"]) in listOfStates):
            listOfStates.append(county["State"])
            first_state = state ["State"]

        
Markup("<State=\"" + s + "\">" + s + "</State>")


if __name__=='__main__':
    app.run(debug=False)
    
    
    
    
    
    
    
    
    
