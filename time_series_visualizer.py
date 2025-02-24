import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

import numpy as np
np.float = float

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates= ["date"], index_col = "date")

# Clean data
df = df[((df["value"] >= df["value"].quantile(0.025)) & (df["value"] <= df["value"].quantile(0.975)))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize = (12, 6))
    ax.plot(df.index, df["value"])
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")


    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar = df_bar.groupby([df_bar.index.year, df_bar.index.month]).mean()
    df_bar = df_bar.unstack()

    month_num = df_bar.columns.get_level_values(1)
    df_bar.columns = month_num.map(lambda x: pd.to_datetime(f'2020-{x:02d}-01').month_name())

    ###############
    ax = df_bar.plot(kind="bar", figsize=(12, 6))
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    ax.legend(title="Months")
    fig = plt.gcf()
    # Draw bar plot
    """
    fig = df_bar.plot(kind = "bar", figsize = (12, 6))
    fig.legend(title = "Months")
    fig.set_xlabel("Years")
    fig.set_ylabel("Average Page Views")
    """


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1,2, figsize = (30, 10))
    sns.boxplot(x = "year", y = "value", data = df_box, ax = axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    sns.boxplot(x = "month", y = "value", data = df_box, ax = axes[1],
                order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
    