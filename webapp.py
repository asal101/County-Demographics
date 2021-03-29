from flask import Flask, request, Markup, render_template
import os
import json
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')
                           
def get_state_options():
    ListOfStates = []
    with open('county_demographics.json') as demographics_data:
         counties = json.load(demographics_data)
            for county in counties:
                if not (county["State"] in ListOfStates):
                    ListOfStates.append(county["State"])
                    
            options = ""
         for state in ListOfStates:
            options = options + Markup("<option value=\"" + s + "\">" + s + "</option>")
        return options
    
    
    if __name__ == '__main__':
        
        app.run(debug=True)
    
    
    
    
    
    
  
