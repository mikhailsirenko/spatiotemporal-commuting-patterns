import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib
from math import ceil
import numpy as np
from copy import deepcopy

def plot_counts(gdf, labels, n_components, label_names=None, figsize=(18,8), plot_median=False, sharex=False, savefig=True):
    '''
    Split counts data based on the cluster and plot it
    
    Args:
        gdf (DataFrame or GeoDataFrame) : Original counts dataset   
        labels (array) : A set of cluster labels
        k (int) : Selected number of clusters
        figsize (tuple) : Size of the figure to be displayed
        plot_median (bool) : Plot median?
        sharex (bool) : Share x-axis?
        savefig (bool) : Save figure?
        
    Returns:
        NoneType
        
    '''
    
    result = pd.DataFrame(gdf.loc[:,'0200-0215':'0145-0200'])

    # Assign the cluster labels
    result['labels'] = labels
    
    # Plot the results
    ncols = 3
    nrows = ceil(n_components / ncols)
    fig, ax = plt.subplots(ncols=ncols, nrows=nrows, figsize=figsize, sharex=sharex)
    k = 0
    for i in range(0, nrows):
        for j in range(0, ncols):
            # Select stations of a certain cluster
            df = result[result["labels"] == k].drop("labels", axis=1).T
            
            # Plot it
            # With median
            if plot_median:
                df.plot(ax=ax[i, j], legend=False, alpha=0.75, linewidth=0.25, color="gray")
                median = df.T.median()
                q1 = df.T.quantile(0.1)
                q3 = df.T.quantile(0.9)
                ax[i, j].plot(median.index, median, color='#0C5DA5', linewidth=1)
                ax[i, j].fill_between(median.index, q1, q3, color='#0C5DA5', alpha=0.25)
            
            # Without
            else:
                df.plot(ax=ax[i, j], legend=False)
                
            # Adjust ticks for better understanding
            # x_ticks = [9, 25, 41, 57, 73, 89]
            # x_ticks_labels = ["04:00", "08:00", "12:00", "16:00", "20:00", "00:00"]
            
            x_ticks = [0, 9, 17, 25, 33, 41, 49, 57, 65, 73, 81, 89, 96]
           # x_ticks_labels = ["04:00","06:00","08:00","10:00","12:00","14:00","16:00","18:00","20:00","22:00","00:00"]
            x_ticks_labels = ["2","4","6","8","10","12","14","16","18","20","22","0", "2"]
            
            ax[i, j].set_xticks(x_ticks)
            ax[i, j].set_xticklabels(x_ticks_labels)
            ax[i, j].get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda y, p: format(int(y), ',')))
            if label_names != None:
                ax[i, j].set_title(f"{label_names[k]}, {df.shape[1]} stations ($k={k}$)")
            else:
                ax[i, j].set_title(f"Cluster {k + 1}, {df.shape[1]} stations")
            ax[i, j].set_xlabel("Time $t$ (hours)")
            # ax[i, j].set_ylabel("Passengers per hour") # , fontsize=12)
            ax[i, j].set_xlim(9, 96)
            start, end = min(df.min()), max(df.max())
            ax[i, j].yaxis.set_ticks(np.arange(start, end + (end - start) / 6, (end - start) / 6))
            ax[i, j].yaxis.set_major_locator(plt.MaxNLocator(6))
            # ax[i, j].yaxis.set_major_locator(plt.LinearLocator())
            ax[i, j].set_ylim(0)
            k += 1
        
        ax[0, 0].set_ylabel(r'$P_i^{k}(t)$') # , fontsize=12)
        ax[1, 0].set_ylabel(r'$P_i^{k}(t)$') # , fontsize=12)
            
    fig.tight_layout()
    
    if savefig:
        plt.savefig('../figures/fig3a.png', dpi=300)