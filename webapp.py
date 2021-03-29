from flask import Flask, request, Markup, render_template
import os
import json
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

def render_fun_fact():
    state_chosen = request.args['states']
    
    
                           
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
    
    def fun_fact_by_state(state)
    first_county = "ZZZZZZZ"
    for county in counties:
    	if county["County"] < first_county and county[State] == state:
    		first_county = county["County"]
    	return first_county
    
    
    
    if __name__ == '__main__':
        
        app.run(debug=True)
        
        
        
        
