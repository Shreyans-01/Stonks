<h1 align="center"> Stonks - Stock Analyser</h1>

## Introduction

To keep up with the ever-growing need of money, people try to diversify their income by investing in the stock market.
Hence, it has become increasingly difficult for one to manually keep track of the stocks on a daily basis. Many software’s are used for this purpose but a certain amount of technical expertise is required to use these and hence, we made this application to make it easy for users to track all their stocks with the prediction value for the next day.
Stonks aims to help traders with complete analysis and predictions, both numerically and graphically.

## What it does ?

Stonks provides features such as:
1. Accepting Ticker Symbol of the desired Stock from the user.
2. User can choose to obtain average open, close, high, low and volume values.
3. The user can also choose to view the above selected values graphically.
4. The user can view the charts for 30,60 and 90 days. 
5. Detailed analysis of the graph is also provided.
6. The user can also see the predicted values of closing price for the next day of a stock at the press of a button.

## How we built it ?

This project is largely GUI oriented. The GUI was made using Tkinter. The UI consists of three pages, each having its own let of functionalities. For obtaining Stock data we use yFinance library. After getting the stock prices and data, the average of each function can be calculated. Further, for plotting we have used matplotlib as well as Plotly. Matplotlib provides a to the point, static graph within the GUI itself and Plotly plots a bigger, detailed map, which can be obtained using the button provided.

## Challenges we ran into ?

1. Tensorflow issues with latest Python Versions(3.9):

    Solution: Downgrade Python Version.


2. Integrate Matplotlib Graph into Tkinter Window.

    Solution: Used canvas.

3. Accuracy of Deep Learning model was extremely low.

    Solution: For each of the training, testing and cross validation dataset, scaling was done to prevent over fitting.

4. yFinance does not provide directly usable data.

    Solution: Used indexing.
    
## How to run it ?

1. Clone the Repository.
2. Change the image paths in code with respect to your system.
3. Navigate to stockanalyzer folder.
4. Run the file using the command `python GUI.py`

And Et Voila !, the GUI will be up and running.
