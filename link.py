import numpy as np
import pandas as pd
import json
import codecs


data_file = 'data/data.csv'
map_json = 'geojson/china_provinces.json'
output = 'china_geo.json'

attributes = ['Population2010']


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.bool_):
            return bool(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(MyEncoder, self).default(obj)


df = pd.read_csv(data_file)
f = codecs.open(map_json, 'r', 'utf-8')
geo = json.load(f)

for g in geo['features']:
    match = df[df['ID'] == g['properties']['id']]
    for attr in attributes:
        g['properties'][attr] = match[attr].iloc[0]
    print(g['properties'])

with open(output, 'w') as f:
    json.dump(geo, f, cls=MyEncoder)
