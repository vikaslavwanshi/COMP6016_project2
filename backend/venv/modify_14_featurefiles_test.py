import pandas as pd

def modify_csv(input_file, output_file):
    # Define the columns to keep
    columns_to_keep = [
        'AIT504', 'FIT501', 'FIT502', 'FIT503', 'FIT504', 'P501', 'P502',
        'PIT501', 'PIT502', 'PIT503', 'FIT601', 'P601', 'P602', 'P603', 'Normal/Attack'
    ]

    df = pd.read_csv('SWaT_Dataset_Normal_v1_modified.csv')

    # Strip any leading/trailing spaces from column names
    df.columns = df.columns.str.strip()

    # Check if all columns are present in the dataframe
    missing_columns = [col for col in columns_to_keep if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing columns in input file: {missing_columns}")

    # Keep only the specified columns
    df = df[columns_to_keep]

    # Change the value of the last column 'P603' from 1 to 2
    df['P603'] = df['P603'].replace(1, 2)

    # Write the modified dataframe to the output CSV file
    df.to_csv('SWaT_Dataset_Normal_v1_modified_test_file.csv', index=False)
    print(f"Modified CSV saved to {'SWaT_Dataset_Normal_v1_modified_test_file.csv'}")

# Example usage
input_file = 'input.csv'
output_file = 'output.csv'
modify_csv(input_file, output_file)
