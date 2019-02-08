def ModelIt(age, pre_MV,apps,ppm,goals,assists,mins_played):
 import pickle
 import numpy as np
  # Python code to connect to Postgres
 # You may need to modify this based on your OS,
 # as detailed in the postgres dev setup materials.
 loaded_model = pickle.load(open('RF_model.sav', 'rb'))
 #pre_MV=pre_MV*1000000
 X_features=np.matrix([age, pre_MV,apps,ppm,goals,assists,mins_played])
 #print(np.isinf(X_features).any())
 result = loaded_model.predict(X_features)

 delta=((result-int(pre_MV))/int(pre_MV))*100
 result=result
 def human_format(num):
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    # add more suffixes if you need them
    return '%.2f%s' % (num, ['', 'K', 'M', 'G', 'T', 'P'][magnitude])
 human_format(result)
 delta=human_format(delta.round())
 base_chart = {
    "values": [40, 10, 10, 10, 10, 10, 10],
    "labels": ["-", "0", "20", "40", "60", "80", "100"],
    "domain": {"x": [0, .48]},
    "marker": {
        "colors": [
            'rgb(255, 255, 255)',
            'rgb(255, 255, 255)',
            'rgb(255, 255, 255)',
            'rgb(255, 255, 255)',
            'rgb(255, 255, 255)',
            'rgb(255, 255, 255)',
            'rgb(255, 255, 255)'
        ],
        "line": {
            "width": 1
        }
    },
    "name": "Gauge",
    "hole": .4,
    "type": "pie",
    "direction": "clockwise",
    "rotation": 108,
    "showlegend": False,
    "hoverinfo": "none",
    "textinfo": "label",
    "textposition": "outside"
}

   #if fromUser != 'Default':
 return result[0].round(),delta
   #return 'check your input'
