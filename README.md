spacetimegeo
==============================
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/mikhailsirenko/spacetimegeo/master)

Exploratory analysis of citizens mobility with a Gaussian mixture model. This respository is a part of research conducted by Verma et al. (2020).

Introduction
------------

Quite often, transportation planning operates with a simple model that takes into account only population counts. That is, the more people live in a neighborhood, the more metro stations will be built to support expected demand. With this project, we aimed to explore relationships between the population of London neighborhoods and ridership represented by "tap ins" made with Oyster card. 

Data
------------
In this study we used four open access data sets:

1. Office for National Statistics (2019). Census Output Area population estimates – London, England (supporting information). Retrieved from https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/datasets/censusoutputareaestimatesinthelondonregionofengland
2. London Datastore (2019). Statistical GIS Boundary Files for London. Retrieved from https://data.london.gov.uk/dataset/statistical-gis-boundary-files-london
3. Transport for London (2020). Transport for London API. Retrieved from https://api-portal.tfl.gov.uk/docs
4. Wikimedia Commons (2020). London Underground geographic maps/CSV. Retrieved from https://commons.wikimedia.org/wiki/London_Underground_geographic_maps/CSV

Methods
------------
This study follows a standard logic of the data science project. First, we gather the data and preprocess it. Second, we explore the data with a couple of visualizations. Finally, we apply a Gaussian mixture model (GMM) to cluster the stations (aggregated tap in) as well as individual passengers (generated tap ins).

Main findings
------------

Project organization
------------

Contributions & authors
------------

License
------------
[CC-BY-NC-SA-4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)

References
------------
1. Verma, T., Sirenko, M., Kornecki, I., Cunningham S., Araujo, N. A. M. (2020) Extracting Spatiotemporal Demand for Public Transit from Mobility Data. Manuscript submitted for publication.