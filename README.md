# AI4ClimbingGrade
Final project for the Building AI course

## Summary

An AI method to estimate trekking routes duration, based on the distance and positive and negative slopes using data from Wikiloc


## Background

* This project tries to give the possibility to estimate the duration of a never done route
* Takes into account the diference between the trekking rithm when the slope is positive or negative. 
* This times are difficult to estimate with other tools, sice, for example, Google Maps could doesn't have the routes accessible
* It makes an average from all Wikiloc users trekking speeds

## How is it used?

You must download the routes info from wikiloc.com. To do so you have to execute the script GetDataFromWikiloc.py passing as argument the url of the page where are listed all the routes: https://ca.wikiloc.com/rutes-senderisme/

Once you executed the file a data.txt will be generated containing the distance, negative and positive slopes and duration of all routes. Then we distribute the data between the training_data.txt and the testing_data.txt, wich will serve as training and testing data files respectively.

Finally, with the training and testing data files with its corresponding content, we can execute the predict_duration_LG.py script which will do the prediction of the duraton of the routes conteined in the testing_data.txt file fitting the system with the data from testiung_data.txt.

## Data sources and AI methods

To collect data I used the [Wikiloc application](https://ca.wikiloc.com/). 

## Challenges

This tool uses the global positive and negative slope, that means that a route that climbs 100 meters, then goes 50 meters down and goes up again 50 meters, all in a horizontal move of 1 km, will have the same duration of a route of the same lenght but that just climbs 100 meters and finishes going down 50 meters, although in the first case the total vertical traveled distance is 150 meters and in the second case is 100 meters.

## What next?

Next step is improve the tool maybe using other methods and adding other parameters related with the duration of a trekking route.

## Acknowledgments

* University of Helsinki
* Reaktor
* Wikiloc community
