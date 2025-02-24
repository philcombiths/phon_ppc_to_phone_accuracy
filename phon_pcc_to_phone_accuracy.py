import pandas as pd
import os

def aggregate_ipa_patterns():
    """
    Aggregates IPA patterns from CSV files in a specified folder.

    This function prompts the user to input the folder path containing the CSV files.
    It processes each CSV file in the specified folder by grouping the data by 'IPA Target'
    and summing the values for all number columns. It also calculates an accuracy percentage
    for each 'IPA Target' and maintains the original order of 'IPA Target' values in the output.
    The aggregated data is saved to new CSV files in the same folder with the prefix 'Aggregated_'.
    """
    # Prompt the user to input the folder path
    folder_path = input("Please enter the folder path containing the CSV files: ")

    # Iterate over each file in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            input_csv = os.path.join(folder_path, filename)
            
            # Load the CSV file
            df = pd.read_csv(input_csv)

            # Get column names from the original input file
            columns = df.columns

            # Group by 'IPA Target' and aggregate by summing the values for all number columns
            aggregated_df = df.groupby(columns[0]).sum()

            # Calculate the Accuracy column
            aggregated_df['% Accuracy'] = (aggregated_df[columns[3]] / aggregated_df[columns[2]]) * 100

            # Reset the index to make 'IPA Target' a column again
            aggregated_df.reset_index(inplace=True)

            # Drop the 'IPA Actual' column
            aggregated_df.drop(columns=[columns[1]], inplace=True)

            # Maintain the original order of IPA Targets, handling missing values
            original_order = df[columns[0]].drop_duplicates().dropna()
            aggregated_df = aggregated_df.set_index(columns[0]).reindex(original_order).reset_index()

            # Save the aggregated data to a new CSV file
            output_csv = os.path.join(folder_path, f'Aggregated_{filename}')
            aggregated_df.to_csv(output_csv, index=False)

            print(f"The aggregated data has been saved to '{output_csv}' with the original order of IPA Targets maintained.")

# Run the function
aggregate_ipa_patterns()