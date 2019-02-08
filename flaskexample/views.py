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
def index():
       return render_template("Soccer_Broker.html")


@app.route('/input',methods=['GET'])
def Soccer_Broker_input():
    nationalities=['Brazil', 'Colombia', 'Kosovo', 'England', 'Mexico', 'Jamaica','Nigeria', 'Italy', 'Chile', 'Greece', 'Croatia', 'France',
       'Turkey', 'Wales', 'Netherlands', 'Scotland', 'Russia',
       'Argentina', 'Serbia', 'Paraguay', 'Uruguay', 'FYR Macedonia',
       'Germany', 'Ecuador', 'Ivory Coast', 'Norway', 'Armenia', 'Spain',
       'Republic of Ireland', 'Switzerland', 'Slovakia', 'Poland',
       'Austria', 'Denmark', 'United States', 'Belgium', 'Senegal',
       'Sweden', 'Benin', 'Algeria', 'Kenya', 'DR Congo', 'Tunisia',
       'Portugal', 'Iran', 'Ukraine', 'Cape Verde', 'Slovenia', 'Ghana',
       'Montenegro', 'Burkina Faso', 'Romania', 'Gambia', 'Cameroon',
       'Korea Republic', 'Venezuela', 'Costa Rica', 'Japan', 'Egypt',
       'Morocco', 'Mali']
    clubs=['Shakhtar Donetsk', 'Manchester City', 'others_teams',
       'FC Barcelona', 'Chelsea FC', 'Tottenham Hotspur',
       'Southampton FC', 'Liverpool FC', 'Atlético Madrid', 'FC Porto',
       'Atalanta BC', 'Juventus FC', 'AC Milan', 'US Sassuolo',
       'Arsenal FC', 'Udinese Calcio', 'SSC Napoli', 'SL Benfica',
       'ACF Fiorentina', 'Bayern Munich', 'Swansea City', 'Sevilla FC',
       'Stoke City', 'Manchester United', 'VfB Stuttgart', 'Real Madrid',
       'Valencia CF', 'UC Sampdoria', 'Genoa CFC', 'Aston Villa',
       'Inter Milan', 'Spartak Moscow', 'AS Roma', 'Hull City',
       'Borussia Mönchengladbach', 'Borussia Dortmund', 'AS Monaco',
       'Newcastle United']
    foot=['Left', 'Right','Both']
    roles=['midfield', 'forward', 'backward', 'keeper']

    return render_template("input.html", nationalities=nationalities, clubs=clubs, foot=foot, roles=roles)

@app.route('/output')
def Soccer_Broker_output():


 #pull 'birth_name' from input field and store it
   age = request.args.get('age')
   nationality = request.args.get('nationality')
   club = request.args.get('club')
   pre_MV=request.args.get('pre_MV')
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
