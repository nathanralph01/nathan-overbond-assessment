# nathan-overbond-assessment

Date: 2020-03-07

Author: Nathan Ralph

Language: Python (Version 3.9)

Description:
A raw data graphing prorgam made in python using the matplotlib library, created for the PEY overbond Assessment. Given a raw data file, specific data-values
such as Issuance Date, CleanBid, CleanAsk, and Last Price are extracted. A scatter plot is created with the Issuance Dates on the x-axis and CleanBid, CleanAsk,
and Last Price values on the y-axis. On the scatter plot, different data-value types have different colours (CleanBid: Red, CleanAsk: Green, LastPrice: Blue).

How to use:
Simply run the main function as main(filename), where filename is the name of the desired data file. Testing was done on file data.tip (as seen in the repository),
which was taken from https://github.com/overbond/overbond-eng-test (original file name was XICE_Bond_Close2.tip). On the scatter plot the data spread is quite large. To get
a better view the matplotlib zoom tool can be used. 


* Libraries Used: Matplotlib, numpy
* Further documentation as to the purpose of each function can be seen in main.py.




