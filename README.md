# geoCN

Geographic data of China visualized with geojson maps.

### Map

Two maps are included in the ```geojson``` folder, one is the province level map and the other is the city level map.

### Data Files

Two data files are in the ```data``` folder. Currently there is only province level population data. More data in both levels can be added. The ```id``` field of each data file matches the ```properties:id``` field of each feature in the correponding map.

A simple Python script (```link.py```) is given here to link the data with the map. Please change the value of the variables in the beginning of the script to select the files and data attributes.