# This file includes filter functions for eunice

import numpy as np
import pandas as pd

class filter:
    def main(self):
        df = pd.read_csv('discord_data/exam.csv')
        df.head()
class_filter = filter()
class_filter.main()