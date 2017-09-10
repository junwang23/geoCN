# geoCN

Geographic data of China visualized with geojson maps.

### Map

Maps are in the ```geojson``` folder. Besides the province level and the city level map, there is also a province level map, output form the ```link.py```, associated with population and density data.

A demo of the maps with d3.js showing the China administrative divisions is available [here](https://bl.ocks.org/junwang23/a9c19cae124371dc8ffa8ff1f66d9437).

### Data Files

Two data files are in the ```data``` folder. Currently there is only province level population and density data. More data in both levels can be added. The ```id``` field of each data file matches the ```properties:id``` field of each feature in the correponding geojson map.

A d3.js demo mapping the China population density is available [here](https://bl.ocks.org/junwang23/98848dbddc4c34b53e25f07932f11e1c).

A simple Python script (```link.py```) is included to link the data with the map. Please change the value of the variables in the beginning of the script to select the files and demanded data attributes.