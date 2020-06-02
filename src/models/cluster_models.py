import pandas as pd
import numpy as np
import pickle
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score
from tqdm import tqdm

def gmm(features, max_components, print_covergence=False, random_state=12345, data_type='entry', save_models=True):
    '''
    Perform Gaussian mixture model (GMM).
    
    Args:
        features (DataFrame or GeoDataFrame) : Counts data     
        max_components (int) : Max number of components for GMM
        print_convergence (bool) : Print GMM convergence?
        random_state (int) : Random state
        data_type (str) : Type of input data: entry or exit
        save_models (bool) : Save pretrained models?

    Returns:
        labels (dict) : Resulting labels
        probs (dict) : Probabilities of cluster assignment
        weights (dict) : Cluster weights
        means (dict) : Means
        covariances (dict) : Covariances
        metrics (DataFrame) : Computed clustering metrics
        
    '''

    X = features.values
    
    labels = {}
    probs = {}
    weights = {}
    means = {}
    covariances = {}
    metrics = pd.DataFrame({"Silhouette score": [], "Calinski-Harabasz": [], "Davies-Bouldin": []})
    criterion = pd.DataFrame({"AIC": [], "BIC": []})
    models = {}
    
    for i in tqdm(range(2, max_components + 1)):
        # Initialize model
        gmm = GaussianMixture(n_components=i, random_state=random_state, n_init=50, covariance_type='full')

        # Fit the data
        gmm = gmm.fit(X)
        
        # Save the model
        if save_models:
            filename = f'../models/stations/gmm_{data_type}_{i}.sav'
            pickle.dump(gmm, open(filename, 'wb')) 
        
        # Get the labels and parameters
        labels[i] = gmm.predict(X)
        probs[i] = np.around(gmm.predict_proba(X), 3)
        weights[i] = gmm.weights_
        means[i] = gmm.means_
        covariances[i] = gmm.covariances_
        
        # Print convergence
        if print_covergence:
            print(f"For {i} components convergence={gmm.converged_} on {gmm.n_iter_} iteration.")
                
        # Calcualte the metrics
        metrics = metrics.append(
            {
                "Silhouette score": silhouette_score(
                    X,
                    labels[i],
                    random_state=random_state
                ),
                "Calinski-Harabasz": calinski_harabasz_score(
                    X, labels[i]
                ),
                "Davies-Bouldin": davies_bouldin_score(
                    X, labels[i]
                ),
            },
            ignore_index=True
        )

        criterion = criterion.append(
            {
                "AIC" : gmm.aic(X),
                "BIC" : gmm.bic(X)
            },
            ignore_index=True
        )

    metrics.index = [j for j in range(2, max_components + 1)]
    criterion.index = [j for j in range(2, max_components + 1)]
    
    return (labels, probs, weights, means, covariances, criterion, metrics)