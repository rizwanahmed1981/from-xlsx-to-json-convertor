import pandas as pd
import os

def excel_to_json(input_file):
    # Load the Excel file
    df = pd.read_excel(input_file)

    # Create output file name
    base = os.path.splitext(input_file)[0]
    output_file = f"{base}.json"

    # Convert to JSON
    df.to_json(output_file, orient="records", indent=4)

    print(f"✅ Converted '{input_file}' to '{output_file}'")

if __name__ == "__main__":
    # Ask for file name
    file_name = input("Enter the Excel file name (with .xlsx): ")

    if os.path.exists(file_name):
        excel_to_json(file_name)
    else:
        print("❌ File not found. Please make sure the .xlsx file is in the same folder.")
