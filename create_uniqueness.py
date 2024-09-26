import pandas as pd

# Read the CSV data into a DataFrame
df = pd.read_csv('F:\\街道的相似性\\new1\\street_similarity_through.csv')

# Sort the values in the 'road1' and 'road2' columns for consistency and expand them back into two separate columns
df[['road1', 'road2']] = df[['road1', 'road2']].apply(lambda x: sorted([x['road1'], x['road2']]), axis=1, result_type='expand')


# Group the data by 'road2' and calculate the mean for specified similarity measures
uniqueness2 = df.groupby('road2').agg({
    'similarity_SV': 'mean',
    'similarity_safe': 'mean',
    'similarity_function': 'mean'
}).reset_index()

# Save the resulting DataFrame to a new CSV file
uniqueness2.to_csv('F:\\街道的相似性\\new1\\unique.csv', index=False)
