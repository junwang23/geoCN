# geoCN

Geographic data of China visualized with geojson maps.

### Map

Maps are in the ```geojson``` folder. Besides the province level and the city level map, there is also a province level map, output form the ```link.py```, associated with population data.

### Data Files

Two data files are in the ```data``` folder. Currently there is only province level population data. More data in both levels can be added. The ```id``` field of each data file matches the ```properties:id``` field of each feature in the correponding map.

A simple Python script (```link.py```) is given here to link the data with the map. Please change the value of the variables in the beginning of the script to select the files and data attributes.