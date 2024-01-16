# average.py 
# introducing the statistics module

from statistics import mean
from logging import INFO, basicConfig, info

basicConfig(level=INFO)
average = mean ([1, 2, 3, 4, 5])
info(f'The average is {average}')



# Path: average.py