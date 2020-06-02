spacetimegeo
==============================

Exploratory analysis of citizens mobility with a Gaussian mixture model

Introduction
------------

Quite often, transportation planning operates with a simple model that takes into account only population counts. That is, the more people, the more metro station should be built. With this project, we aimed to explore relationships between the population of London neighborhoods and ridership represented by "tap ins" and "tap outs" made with Oyster card. 

To do this, we follow the standard logic of the data science project. First, we gather the data and preprocess it. Second, we explore the data with a variety of data visualizations. Finally, we apply the Gaussian mixture model (GMM) to cluster the stations based on "tap in" data. 

We found that often there is a mismatch between the population and ridership. There are specific neighborhoods where the population is low, but ridership is high. To improve the planning model, we analyzed the clusters and came up with a categorization of the adjacent territory. In this model, the ridership is treated as a proxy for place use. For example, if there is a high number of people tapping in the morning and much less in the evening, we consider the area as residential. With GMM, we identified six relevant clusters that somehow represent a function of space around metro stations. The transportation model that takes into account these clusters can be more precise.

Data
------------
In this study we used four open access data sets:

1. Office for National Statistics (2019). Census Output Area population estimates – London, England (supporting information). Retrieved from https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/datasets/censusoutputareaestimatesinthelondonregionofengland
2. London Datastore (2019). Statistical GIS Boundary Files for London. Retrieved from https://data.london.gov.uk/dataset/statistical-gis-boundary-files-london
3. Transport for London (2020). Transport for London API. Retrieved from https://api-portal.tfl.gov.uk/docs
4. Wikimedia Commons (2020). London Underground geographic maps/CSV. Retrieved from https://commons.wikimedia.org/wiki/London_Underground_geographic_maps/CSV

Methods
------------

Main findings
------------

Project organization
------------

Contributions & authors
------------

License
------------

References
------------
