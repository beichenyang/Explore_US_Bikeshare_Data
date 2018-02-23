The major resources help me solve problems in this project is The Python
Standard Library Documentation. Here is the link:
https://docs.python.org/2/library/index.html

To read the .csv file, the read() function is not the best choice. Fortunately,
python provide the module csv dedicated in read and write tabular data in CSV
format.
link: https://docs.python.org/2/library/csv.html?highlight=csv

To calculate the day of a given day, I applied .weekday() function which is from
datetime module.
link: https://docs.python.org/2/library/datetime.html?highlight=date#module-datetime

To count and sort the records by given requests, if I directly store all data
into a list and write a function to count them, the running time of my naive
algorithms will become a serious problem for large csv file. So here I applied a
useful datatype - counter() which is from module collections. This datatype
provide a sub dict class to record the occurrences from given items and several
functions to sort the result. 
link: https://docs.python.org/2/library/collections.html?highlight=counter
