# medical_data_visualizer.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data(csv_file="medical_examination.csv"):
    """
    Load the medical examination CSV data into a pandas DataFrame.
    """
    data = pd.read_csv(csv_file)
    return data

def draw_cat_plot(data):
    """
    Draw a categorical plot using seaborn and return the figure object.
    Update 'column_x' and 'column_y' with your CSV column names.
    """
    # Example: replace with your real columns
    column_x = "cholesterol"   # categorical variable
    column_y = "age"           # numerical variable

    fig = sns.catplot(data=data, x=column_x, y=column_y, kind="bar").fig
    return fig

def draw_heat_map(data):
    """
    Draw a heatmap of correlations between numerical columns.
    Returns the figure object.
    """
    corr = data.corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
    return fig
