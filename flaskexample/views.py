from flaskexample.a_Model import ModelIt
from flask import render_template
from flask import request
from flaskexample import app
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import pandas as pd
import psycopg2
import pickle

# Python code to connect to Postgres
# You may need to modify this based on your OS,
# as detailed in the postgres dev setup materials.

@app.route('/')


@app.route('/index')
def index():
   return render_template("Soccer_Broker.html")

@app.route('/input')
def Soccer_Broker_input():
   return render_template("input.html")

@app.route('/output')
def Soccer_Broker_output():
 #pull 'birth_name' from input field and store it
   age = request.args.get('age')
   nationality = request.args.get('nationality')
   club = request.args.get('club')
   pre_MV= request.args.get('pre_MV')
   apps= request.args.get('apps')
   goals = request.args.get('goals')
   assists = request.args.get('assists')
   ppm= request.args.get('ppm')
   mins_played = request.args.get('mins_played')
   #just select the Cesareans  from the birth dtabase for the name that the user inputs
   #query = "SELECT index,names, mv FROM market_value WHERE names='%s'" % player
   #print(query)
   #query_results=pd.read_sql_query(query,con)
   #print(query_results)
   #names= []
   the_result = ModelIt(age, pre_MV,apps,ppm,goals,assists,mins_played)
   return render_template("output.html", the_result=the_result)
