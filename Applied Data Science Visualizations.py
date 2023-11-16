#Setting the Working Directory
import os
os.chdir("C:\\Users\\LENOVO\\Downloads")
#Loading the Data
import pandas as pd
#Load the data from the uploaded CSV file
file_path = "Smoking.csv"
smoking_data = pd.read_csv(file_path)
#Displaying the first few rows of the dataset to understand its structure and contents
smoking_data.head()

#Line Plot
import matplotlib.pyplot as plt
#Function to create a line plot
def line_plot(data, x, y, hue, title, xlabel, ylabel):
    """
    Creates a line plot for given data.

    Parameters:
    data (DataFrame): The pandas DataFrame containing the data.
    x (str): The column name to be used for the x-axis.
    y (str): The column name to be used for the y-axis.
    hue (str): The column name to be used for grouping different lines.
    title (str): The title of the plot.
    xlabel (str): The label for the x-axis.
    ylabel (str): The label for the y-axis.
    """
    plt.figure(figsize=(10, 6))
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.plot(data[x], data[y], label=hue)
    plt.legend()
    plt.show()
#Group the data by age and smoking status and calculate the average BMI
grouped_data = smoking_data.groupby(['age', 'smoker']).mean().reset_index()
#Create the line plot
line_plot(grouped_data, 'age', 'bmi', 'smoker', 'Average BMI by Age for Smokers and Non-Smokers', 'Age', 'Average BMI')
#Bar Chart
#Function to create a bar chart
def bar_chart_pyplot(data, x, hue, title, xlabel, ylabel):
    """
    Creates a bar chart for given data using only matplotlib.pyplot.

    Parameters:
    data (DataFrame): The pandas DataFrame containing the data.
    x (str): The column name to be used for the x-axis.
    hue (str): The column name to be used for differentiating bars.
    title (str): The title of the plot.
    xlabel (str): The label for the x-axis.
    ylabel (str): The label for the y-axis.
    """
    #Pivot the data for plotting
    pivoted_data = data.groupby([x, hue]).size().unstack()
    pivoted_data.plot(kind='bar', stacked=False, figsize=(10, 6))
    #Customizing the plot
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(axis='y')
    plt.legend(title=hue)
    plt.show()
#Create the bar chart using only pyplot
bar_chart_pyplot(smoking_data, 'region', 'smoker', 'Number of Smokers and Non-Smokers in Different Regions', 'Region', 'Count')
#Pie Chart
#Function to create a pie chart
def pie_chart(data, column, title):
    """
    Creates a pie chart for given data.

    Parameters:
    data (DataFrame): The pandas DataFrame containing the data.
    column (str): The column name to be used for the pie chart segments.
    title (str): The title of the plot.
    """
    plt.figure(figsize=(8, 8))
    plt.title(title)
    data[column].value_counts().plot.pie(autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff'])
    plt.ylabel('')
    plt.show()
#Filter the data to include only smokers
smokers_data = smoking_data[smoking_data['smoker'] == 'yes']
#Create the pie chart
pie_chart(smokers_data, 'sex', 'Gender Distribution Among Smokers')
