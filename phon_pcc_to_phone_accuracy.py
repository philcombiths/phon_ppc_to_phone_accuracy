import pandas as pd

# Load the CSV file
df = pd.read_csv('IPA Patterns.csv')

# Group by 'IPA Target' and aggregate by summing the values for all number columns
aggregated_df = df.groupby('IPA Target').sum()

# Calculate the Accuracy column
aggregated_df['% Accuracy'] = (aggregated_df['# Correct'] / aggregated_df['Other_GFTA2.GFTA2_transcriptions_example']) * 100

# Reset the index to make 'IPA Target' a column again
aggregated_df.reset_index(inplace=True)

# Drop the 'IPA Actual' column
aggregated_df.drop(columns=['IPA Actual'], inplace=True)

# Maintain the original order of IPA Targets, handling missing values
original_order = df['IPA Target'].drop_duplicates().dropna()
aggregated_df = aggregated_df.set_index('IPA Target').reindex(original_order).reset_index()

# Save the aggregated data to a new CSV file
aggregated_df.to_csv('Aggregated_IPA_Patterns.csv', index=False)

print("The aggregated data has been saved to 'Aggregated_IPA_Patterns.csv' with the original order of IPA Targets maintained.")