# geocncities
China city-level map in geojson format including all city administrative level areas. Islands of South China Sea are not included currently but will be added in future.
The Taiwan province is not divided into counties, but very detailed geo-information can be found at [twgeojson](https://github.com/g0v/twgeojson).

The geojson files of the provinces as well as a province-level map are fetched from [china-geojson](https://github.com/antvis/china-geojson)

## Install

#### Method 1
Simply download/copy the china_city.json file at the root directory.

#### Method 2
Building the map from source requires node.js and node packages of fs and geojson-merge.

```$ npm install``` at the root directory and then ```$ node build.js``` to generate the geojson file.

## Demo Image

Run the index html page with any web server (e.g. [jekyll](http://jekyllrb.com/)), a leaflet demo should be shown as follows.

![](demo.png)



