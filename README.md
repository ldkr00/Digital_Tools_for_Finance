# Final Project

## Topic
Is the Swiss franc a safe haven for US investors during recessions?

## Approach
We focus on the recessions of the last 40 years namely July 1981- November 1982, July 1990 - March 1991, March 2001 - November 2001, December 2007 - June 2009 and February 2020 - today. Using the S&P 500 returns over these periods and the exchange rate CHF/USD, we run an OLS regression to investigate wether there is a significant correlation. To have enough data we use daily or weekly returns which we get from Yahoo Finance. If our estimate from the regression is significantly negative then we have some evidence that investing in the Swiss franc during recessions might be a good choice for US investors.

## Group Members
 - Lukas Dekker, 18-737-692
 - Denis Hallulli, 21-739-529
 - Dominic Krummenacher, 21-713-284

## How to run the Notebook using Docker:
 - Clone the Github Repo and store it locally
 - Start Docker
 - Start Terminal and navigate to the local repo
 - Create Image: docker build -t my-jupyter-notebook .
 - Run Image: docker run -d -p 8888:8888 my-jupyter-notebook start.sh jupyter notebook --NotebookApp.token=''
 - Open a web browser and go to the URL http://localhost:8888
 - Navigate to the notebook and open it
 
