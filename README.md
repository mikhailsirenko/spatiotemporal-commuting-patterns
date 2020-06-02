spacetimegeo
==============================

Analysis of citizens mobility with a Gaussian Mixture Model

Introduction
------------

Quite often, transportation planning operates with a simple model that takes into account only population counts. That is, the more people, the more metro station should be built. With this project, we aimed to explore relationships between the population of London neighborhoods and ridership represented by "tap ins" and "tap outs" made with Oyster card. 

To do this, we follow the standard logic of the data science project. First, we gather the data and preprocess it. Second, we explore the data with a variety of data visualizations. Finally, we apply the Gaussian mixture model (GMM) to cluster the stations based on "tap in" data. 

We found that often there is a mismatch between the population and ridership. There are specific neighborhoods where the population is low, but ridership is high. To improve the planning model, we analyzed the clusters and came up with a categorization of the adjacent territory. In this model, the ridership is treated as a proxy for place use. For example, if there is a high number of people tapping in the morning and much less in the evening, we consider the area as residential. With GMM, we identified six relevant clusters that somehow represent a function of space around metro stations. The transportation model that takes into account these clusters can be more precise.

Data
------------
In this study we used four data sets:

1.
2. 
3. 
4.

All of them are open-access and can be find online here (see References).

Methods
------------
* Describe preprocessing (creation of individual traces)
* Clustering of stations
* Clustering of individual traces
* Note on complexity of the task

Results
------------


Project Organization
------------

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    ├── figures            <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │                     predictions
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    └──
--------

Contributions & authors
------------

License
------------

References
------------