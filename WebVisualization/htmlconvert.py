import pandas as pd

a = pd.read_csv('assets/cities.csv')

a.to_html('table.html')