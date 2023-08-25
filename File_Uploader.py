import requests
import turtle
import time
import csv
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import smtplib 
from datetime import datetime
import streamlit as st


st.set_page_config(layout="wide")
turtle.Screen().bgcolor("black")
sample_size = 10
urls = [
    'https://devdashboard.tradingblock.com',
    'https://betadashboard.tradingblock.com',
    'https://dashboard.tradingblock.com',
    'https://vt.tradingblock.com',
    'https://ny4staging.tradingblock.com',
    'https://beta.tradingblock.com',
    'https://api3.tradingblock.com'
]

def measure_response_time(url):
    start_time = time.time_ns()
    response = requests.get(url)
    end_time = time.time_ns()
    response_time = (end_time - start_time) / 1000000
    return response_time

def measure_slidingwindow_avg_time(): 
    arr = avg_response_times[url]
    numbers_series = pd.Series(arr) # Convert array of integers to pandas series

    windows = numbers_series.rolling(window) # Get the window of seriesof observations of specified window size
    moving_averages = windows.mean() # Create a series of moving averages of each window
    moving_averages_list = moving_averages.tolist() # Convert pandas series back to list

    # Remove null entries from the list
    final_list = moving_averages_list[window - 1:]
    avg_slidingwindow = np.array(final_list)
    slidingwindow[url].append(avg_slidingwindow[-1])
    print("sliding window avg. is:",slidingwindow[url])

def alert_function():
    #Create your SMTP session 
    smtp = smtplib.SMTP('smtp.gmail.com', 587) 

    #Use TLS to add security 
    smtp.starttls() 

    #User Authentication 
    smtp.login("gilbertdevil20@gmail.com", "fjzrvkspuyrmaptc")

    #Defining The Message 
    message = "Tradingblock webite is down" 
    
    #Sending the Email
    smtp.sendmail("gilbertdevil20@gmail.com","mshah@tradingblock.com",message) 

    #Terminating the session 
    smtp.quit() 
    print ("Email sent successfully!") 

def plot_data_from_csv(filename):
    df = pd.read_csv(filename, )
    for url in urls:
        url_df = df[df['URL'] == url]
        x = url_df['Date and Time']
        y = url_df['Average Response Time (ms)']
        y1 = url_df['Sliding Window Average']
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(x=x, y=y, mode="lines", name="Avg Response Times"))
        fig.add_trace(go.Scatter(x=x, y=y1, mode="lines", name="Slidingwindow Avg Times"))

        fig.update_layout(
            xaxis=dict(
                rangeselector=dict(
                    buttons=list([
                        dict(count=1,
                            step="second",
                            stepmode="backward"),
                    ])
                ),
                rangeslider=dict(
                    visible=True
                ),
                
            ),
            title=f'Average Response & Sliding Window Average Time for {url}', xaxis_title="Time", yaxis_title="Average Response Time (ms)"
        )

        if url == 'https://devdashboard.tradingblock.com':
            with plot_spot1.container():
                col1, col2 = st.columns(2)
                with plot_spot1:
                    col1.write(fig)

        if url == 'https://betadashboard.tradingblock.com':
            with plot_spot1.container():
                col1, col2 = st.columns(2)
                with plot_spot1:
                    col2.write(fig)

        if url == 'https://dashboard.tradingblock.com':
            with plot_spot2.container():
                col1, col2 = st.columns(2)
                with plot_spot2:
                    col1.write(fig)

        if url == 'https://vt.tradingblock.com':
            with plot_spot2.container():
                col1, col2 = st.columns(2)
                with plot_spot2:
                    col2.write(fig)

        if url == 'https://ny4staging.tradingblock.com':
            with plot_spot3.container():
                col1, col2 = st.columns(2)
                with plot_spot3:
                    col1.write(fig)

        if url == 'https://beta.tradingblock.com':
            with plot_spot3.container():
                col1, col2 = st.columns(2)
                with plot_spot3:
                    col2.write(fig)
                    
        if url == 'https://api3.tradingblock.com':
            with plot_spot4.container():
                col1, col2 = st.columns(2)
                with plot_spot4:
                    col1.write(fig)

def plot_data_from_upload_csvfile(uploaded_files):
    df = pd.read_csv(uploaded_files)
    for url in urls:
        url_df = df[df['URL'] == url]
        x = url_df['Date and Time']
        y = url_df['Average Response Time (ms)']
        y1 = url_df['Sliding Window Average']
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(x=x, y=y, mode="lines", name="Avg Response Times"))
        fig.add_trace(go.Scatter(x=x, y=y1, mode="lines", name="Slidingwindow Avg Times"))

        fig.update_layout(
            xaxis=dict(
                rangeselector=dict(
                    buttons=list([
                        dict(count=1,
                            step="second",
                            stepmode="backward"),
                    ])
                ),
                rangeslider=dict(
                    visible=True
                ),
                
            ),
            title=f'Average Response & Sliding Window Average Time for {url}', xaxis_title="Time", yaxis_title="Average Response Time (ms)"
        )

        if url == 'https://devdashboard.tradingblock.com':
            with plot_spot1.container():
                col1, col2 = st.columns(2)
                with plot_spot1:
                    col1.write(fig)

        if url == 'https://betadashboard.tradingblock.com':
            with plot_spot1.container():
                col1, col2 = st.columns(2)
                with plot_spot1:
                    col2.write(fig)

        if url == 'https://dashboard.tradingblock.com':
            with plot_spot2.container():
                col1, col2 = st.columns(2)
                with plot_spot2:
                    col1.write(fig)

        if url == 'https://vt.tradingblock.com':
            with plot_spot2.container():
                col1, col2 = st.columns(2)
                with plot_spot2:
                    col2.write(fig)

        if url == 'https://ny4staging.tradingblock.com':
            with plot_spot3.container():
                col1, col2 = st.columns(2)
                with plot_spot3:
                    col1.write(fig)

        if url == 'https://beta.tradingblock.com':
            with plot_spot3.container():
                col1, col2 = st.columns(2)
                with plot_spot3:
                    col2.write(fig)
                    
        if url == 'https://api3.tradingblock.com':
            with plot_spot4.container():
                col1, col2 = st.columns(2)
                with plot_spot4:
                    col1.write(fig)

interval = 60  # 1 minute
window = 5
# Initialize dictionaries to store average response times and intervals for each URL
avg_response_times = {url: [] for url in urls}
intervals = {url: [] for url in urls}
slidingwindow = {url:[] for url in urls}



left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image("https://uploads-ssl.webflow.com/5d5c50dcee289053140e5d5f/5d5d88ca3e9e5acdd003f839_logo.svg", width=400 )

plot_spot1 = st.empty()
plot_spot2 = st.empty()
plot_spot3 = st.empty()
plot_spot4 = st.empty()

with st.sidebar:
    uploaded_files = st.file_uploader("Choose a CSV file", type = ['csv'])

while True:
    if uploaded_files is not None:
        plot_data_from_upload_csvfile(uploaded_files)
        break
    for url in urls:
        print("URL:", url)
        times = []
        
        for i in range(sample_size):
            response_time = measure_response_time(url)
            times.append(response_time)

        average_time = sum(times) / len(times)
        avg_response_times[url].append(average_time)
        intervals[url].append(datetime.now().strftime("%m-%d-%Y %H:%M:%S"))

        print("Average Response Time (ms):", average_time)
        print()
        
        # ----------------------------------------------------------------------------#
        # for sliding Window Average calculations 
        if len(avg_response_times[url]) >= window:
            
            measure_slidingwindow_avg_time()
            
            #--------------------------------------------------------------------------#
            # for calculate 3rd standard deviation 
            sliding_window_df = pd.DataFrame(slidingwindow[url]) #convert list into dataframe 
            slidingwindow_std = (sliding_window_df.mean() + 3 * sliding_window_df.std())
            slidingwindow_std = slidingwindow_std.values.tolist()
            print("Third sigma value:",slidingwindow_std)
            
            #---------------------------------------------------------------------------#
            #Gives Alerts 
            if slidingwindow[url][-1] > slidingwindow_std: 
                alert_function() 
        else: 
            slidingwindow[url].append(None)

    # Write CSV file
    filename = datetime.now().strftime('Monitoring-%Y-%m-%d.csv')
    fieldnames = ['URL', 'Average Response Time (ms)', 'Date and Time', 'Sliding Window Average']

    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for url in urls:
            for interval, avg_time, Sliding_avg in zip(intervals[url], avg_response_times[url], slidingwindow[url]):
                writer.writerow({
                    'URL': url,
                    'Average Response Time (ms)': avg_time,
                    'Date and Time': interval,
                    'Sliding Window Average': Sliding_avg
                })
    print("CSV file generated:", filename)
    
    plot_data_from_csv(filename)

    time.sleep(1)

