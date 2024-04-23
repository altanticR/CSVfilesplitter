import argparse
import csv
import os
import logging

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# There are 2 functions that you can call. split_csv and split_csh
# split_csv splits the CSV table with no headers to multiple documents based on the number of rows that you specified. Each file only have records and no header. 
# You need to provide the input file name, the file name of your output, your row_limit and the directory/folder to save the output file.
# split_csv_h does the same function but split tables with headers. 
  
def split_csv(input_filename, output_prefix, row_limit, output_folder):
    """
    Splits a CSV file into multiple parts with a given number of rows in each, and stores them in a specified folder.

    :param input_filename: The path to the input CSV file.
    :param output_prefix: The prefix for the output files.
    :param row_limit: The maximum number of rows in each output file.
    :param output_folder: The folder where the output files will be stored.
    """
    try:
        # Ensure the output directory exists
        os.makedirs(output_folder, exist_ok=True)

        with open(input_filename, 'r', newline='', encoding='utf-8') as input_file:
            reader = csv.reader(input_file)
            file_count = 1
            records_written = 0
            output_file_path = os.path.join(output_folder, f"{output_prefix}{file_count}.csv")

            # Use 'with' statement for better resource management
            with open(output_file_path, 'w', newline='', encoding='utf-8') as output_file:
                writer = csv.writer(output_file)

                for row in reader:
                    if records_written == row_limit:
                        # Increment file_count and update output file path
                        file_count += 1
                        output_file_path = os.path.join(output_folder, f"{output_prefix}{file_count}.csv")
                        output_file.close()
                        output_file = open(output_file_path, 'w', newline='', encoding='utf-8')
                        writer = csv.writer(output_file)
                        records_written = 0
                    
                    writer.writerow(row)
                    records_written += 1
        logging.info("File splitting completed successfully.")
    except Exception as e:
        logging.error(f"Failed to split CSV file due to: {e}")
        raise

def split_csv_h(input_filename, output_prefix, row_limit, output_folder):
    """
    Splits a CSV file into multiple parts with a given number of rows in each, and stores them in a specified folder.
    Assumes the CSV file has a header row.

    :param input_filename: The path to the input CSV file.
    :param output_prefix: The prefix for the output files.
    :param row_limit: The maximum number of rows in each output file (excluding the header).
    :param output_folder: The folder where the output files will be stored.
    """
    try:
        # Ensure the output directory exists
        os.makedirs(output_folder, exist_ok=True)

        with open(input_filename, 'r', newline='', encoding='utf-8') as input_file:
            reader = csv.reader(input_file)
            headers = next(reader)  # Extract the header row
            file_count = 1
            records_written = 0
            output_file_path = os.path.join(output_folder, f"{output_prefix}{file_count}.csv")

            # Start the first output file and write the header
            output_file = open(output_file_path, 'w', newline='', encoding='utf-8')
            writer = csv.writer(output_file)
            writer.writerow(headers)

            for row in reader:
                if records_written == row_limit:
                    # Increment file_count and update output file path
                    file_count += 1
                    output_file_path = os.path.join(output_folder, f"{output_prefix}{file_count}.csv")
                    output_file.close()  # Close the current file
                    output_file = open(output_file_path, 'w', newline='', encoding='utf-8')
                    writer = csv.writer(output_file)
                    writer.writerow(headers)  # Write the header in the new file
                    records_written = 0  # Reset the record count

                writer.writerow(row)
                records_written += 1

            # Close the last output file
            output_file.close()
        logging.info("File splitting completed successfully.")
    except Exception as e:
        logging.error(f"Failed to split CSV file due to: {e}")
        raise

# Usage
if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description='Split a CSV file into multiple smaller files.')
        parser.add_argument('function', choices=['split_csv', 'split_csv_h'], default='split_csv_h', nargs='?',
                        help='Function to run: split_csv for no headers, split_csv_h for headers. Default is split_csv_h.')
        parser.add_argument('input_filename', type=str, help='The path to the input CSV file.')
        parser.add_argument('output_prefix', type=str, help='The prefix for the output files.')
        parser.add_argument('row_limit', type=int, help='The maximum number of rows in each output file.')
        parser.add_argument('output_folder', type=str, help='The folder where the output files will be stored.')
        args = parser.parse_args()

        # Conditional execution based on user's choice
        if args.function == 'split_csv':
            split_csv(args.input_filename, args.output_prefix, args.row_limit, args.output_folder)
        elif args.function == 'split_csv_h':
            split_csv_h(args.input_filename, args.output_prefix, args.row_limit, args.output_folder)
            print("File Splitting Done")
    except Exception as error:
        print(f"An error occurred: {error}")
