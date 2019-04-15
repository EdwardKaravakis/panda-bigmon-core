"""
Created on 15.04.2019 by Tatiana Korchuganova
Function to transform data from standard Grafana API response to D3.js compatible
"""


def stacked_hist(series, group_by=None, split_series=None):
    plot_data = {}

    if not group_by:
        return plot_data
    if not split_series:
        split_series_value = 'all'

    tags = series[0]['tags'].keys()
    if group_by in tags:
        for s in series:
            split_series_value = s['tags'][split_series] if split_series else split_series_value
            if s['tags'][group_by] not in plot_data:
                plot_data[s['tags'][group_by]] = {}
            if split_series_value not in plot_data[s['tags'][group_by]]:
                plot_data[s['tags'][group_by]][split_series_value] = 0
            plot_data[s['tags'][group_by]][split_series_value] += s['values'][0][1]

    return plot_data