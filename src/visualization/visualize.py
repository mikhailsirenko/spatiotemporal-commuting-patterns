import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib
from math import ceil
import numpy as np
from copy import deepcopy

def plot_sample_stations(gdf, figsize, sharex, sharey, savefig):
    '''
    Plot examples stations entry and exit by traffic volume for each of the clusters.
    
    Args:
        gdf (DataFrame or GeoDataFrame) : Counts data set with assinged clusters   
        figsize (tuple) : Size of the figure to be displayed
        sharex (bool) : Share x-axis?
        sharey (bool) : Share y-axis?
        savefig (bool) : Save figure?
        
    Returns:
        NoneType
        
    '''
    fig, ax = plt.subplots(nrows=6, ncols=3, figsize=figsize, sharex=sharex, sharey=sharey)
    
    # Define label names and corresponding colors
    label_names = ["Inner residential", "Polycentre", "CBD", "Mixed commuting", "Outer residential", "Potential feeder"]
    label_color_map = {"Outer residential": "#FF2C00", "CBD": "#00B945", "Polycentre": "#845B97", 
                       "Inner residential": "#FF9500", "Potential feeder": "#0C5DA5", "Mixed commuting": "#474747"}
    
    exit_stations = pd.read_csv('../data/interim/counts/Ex17week.csv')
    
    for i in range(6):
        current_label_name = gdf[gdf['label'] == i]['label_name'].iloc[0]
        current_label_stations = gdf[gdf['label'] == i]
        q10 = current_label_stations['total'].quantile(.1)
        q25 = current_label_stations['total'].quantile(.25)
        mean = current_label_stations['total'].mean()
        q75 = current_label_stations['total'].quantile(.75)

        q25_stations = current_label_stations[current_label_stations['total'] < q25]
        average_stations = current_label_stations[current_label_stations['total'] > mean - q10]
        average_stations = average_stations[average_stations['total'] < mean + q10]
        q75_stations = current_label_stations[current_label_stations['total'] > q75]

        q25_station_name = q25_stations['station_name'].tolist()[1]
        average_station_name = average_stations['station_name'].tolist()[1]
        q75_station_name = q75_stations['station_name'].tolist()[1]

        q25_station = pd.DataFrame(current_label_stations[current_label_stations['station_name'] == q25_station_name].loc[:,'0200-0215':'0145-0200']).T
        average_station = pd.DataFrame(current_label_stations[current_label_stations['station_name'] == average_station_name].loc[:,'0200-0215':'0145-0200']).T
        q75_station = pd.DataFrame(current_label_stations[current_label_stations['station_name'] == q75_station_name].loc[:,'0200-0215':'0145-0200']).T

        q25_station_exit = pd.DataFrame(exit_stations[exit_stations['station_name'] == q25_station_name].loc[:,'0200-0215':'0145-0200']).T
        average_station_exit = pd.DataFrame(exit_stations[exit_stations['station_name'] == average_station_name].loc[:,'0200-0215':'0145-0200']).T
        q75_station_exit = pd.DataFrame(exit_stations[exit_stations['station_name'] == q75_station_name].loc[:,'0200-0215':'0145-0200']).T

        q25_station.plot(ax=ax[i, 0], legend=False, color=label_color_map[current_label_name], linestyle='--', label='Entry')
        average_station.plot(ax=ax[i, 1], legend=False, color=label_color_map[current_label_name], linestyle='--', label='Entry')
        q75_station.plot(ax=ax[i, 2], legend=False, color=label_color_map[current_label_name], linestyle='--', label='Entry')

        q25_station_exit.plot(ax=ax[i, 0], legend=False, color=label_color_map[current_label_name], linestyle=':', label='Exit')
        average_station_exit.plot(ax=ax[i, 1], legend=False, color=label_color_map[current_label_name], linestyle=':', label='Exit')
        q75_station_exit.plot(ax=ax[i, 2], legend=False, color=label_color_map[current_label_name], linestyle=':', label='Exit')

        x_ticks = [0, 9, 17, 25, 33, 41, 49, 57, 65, 73, 81, 89, 96]
        x_ticks_labels = ["2","4","6","8","10","12","14","16","18","20","22","0","2"]

        all_stations_entry = [q25_station, average_station, q75_station]
        all_stations_exit = [q25_station_exit, average_station_exit, q75_station_exit]

        for j in range(0, 3):
            ax[i, j].set_xticks(x_ticks)
            ax[i, j].set_xticklabels(x_ticks_labels)
            ax[i, j].get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda y, p: format(int(y), ',')))
            ax[i, j].set_xlim(9, 96)
            ax[i, j].yaxis.set_major_locator(plt.MaxNLocator(6))
            ax[i, j].legend(['Entry', 'Exit'])
            ax[i, j].set_xlabel("Time $t$ (hours)")
            ax[i, j].set_ylim(0)

        ax[i, 0].set_title(q25_station_name)
        ax[i, 1].set_title(average_station_name)
        ax[i, 2].set_title(q75_station_name)

        ax[i, 0].set_ylabel(fr'{current_label_name} $P_i^{i}(t)$')

    if savefig:
        plt.savefig('../figures/sfig8.png', dpi=300)

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
            x_ticks = [0, 9, 17, 25, 33, 41, 49, 57, 65, 73, 81, 89, 96]
            x_ticks_labels = ["2","4","6","8","10","12","14","16","18","20","22","0", "2"]
            
            ax[i, j].set_xticks(x_ticks)
            ax[i, j].set_xticklabels(x_ticks_labels)
            ax[i, j].get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda y, p: format(int(y), ',')))
            if label_names != None:
                ax[i, j].set_title(f"{label_names[k]}, {df.shape[1]} stations ($k={k}$)")
            else:
                ax[i, j].set_title(f"Cluster {k + 1}, {df.shape[1]} stations")
            ax[i, j].set_xlabel("Time $t$ (hours)")
            ax[i, j].set_xlim(9, 96)
            ax[i, j].yaxis.set_major_locator(plt.MaxNLocator(6))
            ax[i, j].set_ylim(0)
            k += 1
        
        ax[0, 0].set_ylabel(r'$P_i^{k}(t)$')
        ax[1, 0].set_ylabel(r'$P_i^{k}(t)$')
            
    fig.tight_layout()
    
    if savefig:
        plt.savefig('../figures/fig3a.png', dpi=300)