''' Creation Date: 24/11/2022 '''

import pandas
from factor_analyzer import FactorAnalyzer

# Load data
dataframe = pandas.read_csv('data.csv')

# Define type
paf = FactorAnalyzer(method='principal')
paf.set_params(n_factors=2, rotation="oblimin")

# Apply data
paf.fit(dataframe)

# Show results
print(f"Variable Factor Loading Scores:\n{paf.loadings_}\n")
print(f"Variable Communality Scores:\n{paf.get_communalities()}\n")
print(f"Variable Uniqueness Scores:\n{paf.get_uniquenesses()}\n")
