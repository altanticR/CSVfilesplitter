# CSV Splitter Utility

A Python utility to split large CSV files into smaller files based on a specified number of rows per file.

## Description

The CSV Splitter Utility is designed to handle the division of large CSV files into manageable parts without requiring external libraries beyond Python's standard modules. This utility provides two main functions:

- `split_csv`: Splits a CSV file without headers into multiple files, each containing a specified number of rows.
- `split_csv_h`: Splits a CSV file with headers into multiple files, ensuring that each split file starts with the header followed by the specified number of rows.

Both functions ensure that no data is lost during the splitting process and that files are named systematically for easy organization.

## Contributing

We welcome any and all contributions! Here are some ways you can get started:

Report bugs: If you encounter any bugs, please let us know. Open up an issue and let us know the problem.
Contribute code: If you are a developer and want to contribute, follow the instructions below to get started!
Suggestions: If you don't want to code but have some awesome ideas, open up an issue explaining some updates or imporvements you would like to see!
Documentation: If you see the need for some additional documentation, feel free to add some!

## How to Use

To use this utility from GitHub:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/csv-splitter.git

2. **Navigate to the Repository Folder:**
   ```bash
   cd csv-splitter

3. **Run the Script:**
For CSVs without headers:
bash
Copy code
python split_csv.py <input_filename> <output_prefix> <row_limit> <output_folder>
For CSVs with headers:
bash
Copy code
python split_csv_h.py <input_filename> <output_prefix> <row_limit> <output_folder>
Replace <input_filename>, <output_prefix>, <row_limit>, and <output_folder> with your actual file path, desired output file prefix, maximum number of rows per output file, and output directory path, respectively.
Example
Splitting a file named example.csv into smaller files with 500 records each (excluding the header for files created by split_csv_h):

bash
Copy code
python split_csv_h.py example.csv example_output 500 ./output
Requirements
Python 3.x
Standard libraries: os, csv, logging
Ensure Python is installed and properly configured in your environment to run the scripts.

Contributions
Contributions are welcome! Please fork the repository and submit pull requests with your enhancements.

License
This project is licensed under the MIT License - see the LICENSE.md file for details.

css
Copy code

This README is structured to provide a clear, easy-to-follow guide for us
