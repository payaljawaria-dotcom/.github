import pandas as pd
import sys
# import os
# print("Current directory:", os.getcwd())
# print("Files here:", os.listdir())
# print("It is here")
# df = pd.read_excel('Int B.Tech_M.tech.xlsx')
# print(df.head())
# import pandas as pd

def print_specific_excel_row(file_path, sheet_name, row_index):
    # """
    # Reads an Excel file and prints a specific row.

    # Args:
    #     file_path (str): The path to the Excel file.
    #     sheet_name (str): The name of the sheet to read.
    #     row_index (int): The 0-based index of the row to print.
    #                      (e.g., 0 for the first row, 1 for the second, etc.)
    # """
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)

        if row_index < 0 or row_index >= len(df):
            print(f"Error: Row index {row_index} is out of bounds for the DataFrame.")
            return

        specific_row = df.iloc[row_index - 1]
        print(f"Row at index {row_index}:")
        print(specific_row)

    except FileNotFoundError:
        print(f"Error: Excel file not found at '{file_path}'")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
if len(sys.argv) > 1 and sys.argv[1].strip():
    excel_file = sys.argv[1]
else:
    excel_file = "Int B.Tech_M.tech.xlsx"
sheet = "Sheet1"                     # Replace with your sheet name
if len(sys.argv) > 2 and sys.argv[2].strip():
    desired_row_index = int(sys.argv[2])
else:
    desired_row_index = 2     # Replace with the 0-based index of the row you want to print

print_specific_excel_row(excel_file, sheet, desired_row_index)
