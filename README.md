# CSV Splitter Utility

A Python utility to split large CSV files into smaller files based on a specified number of rows per file.

## Description

The CSV Splitter Utility is designed to handle the division of large CSV files into manageable parts without requiring external libraries beyond Python's standard modules. This utility provides two main functions:

- `split_csv_h`: Splits a CSV file with headers into multiple files, ensuring that each split file starts with the header followed by the specified number of rows. This is the default function if no not specified.
- `split_csv`: Splits a CSV file without headers into multiple files, each containing a specified number of rows.

Both functions ensure that no data is lost during the splitting process and that files are named systematically for easy organization.

## Contributing

We welcome any and all contributions! Here are some ways you can get started:

__Report bugs__: If you encounter any bugs, please let us know. Open up an issue and let us know the problem.

__Contribute code__: If you are a developer and want to contribute, follow the instructions below to get started!

__Suggestions__: If you don't want to code but have some awesome ideas, open up an issue explaining some updates or imporvements you would like to see!
Documentation: If you see the need for some additional documentation, feel free to add some!

## How to Use

To use this utility from GitHub:

1. Fork this repository __(Optional)__.

2. Clone the forked repository.

2. **Navigate to the Repository Folder:**
   ```bash
   cd CSVfilesplitter

3. **Run the Script:**
   * For CSVs with headers (by default):
     ```bash
     python csvfilesplitter.py split_csv_h <input_filename> <output_prefix> <row_limit> <output_folder>
   * For CSVs without headers:
     ```bash
     python csvfilesplitter.py split_csv_h <input_filename> <output_prefix> <row_limit> <output_folder>
     
Replace <input_filename>, <output_prefix>, <row_limit>, and <output_folder> with your actual file path, desired output file prefix, maximum number of rows per output file, and output directory path, respectively.

## Example
Splitting a file named ibm.csv (it has header) or ibmwoh.csv (it has no header) into smaller files with 500 records each (excluding the header for files created by split_csv_h):

    ### CSV File with a header (by default)
    ```bash
    python csvfilesplitter.py split_csv ibm.csv ibm_output 500 ./ibm

   or

    ### CSV File without a header
    ```bash
    python csvfilesplitter.py split_csv ibmwoh.csv ibmwoh_output 500 ./ibmwoh

The "ibm.csv" file has a header. The "ibmwoh.csv" file does not have a header. 
## Requirements
    * Python 3.x
    * Standard libraries: os, csv, logging

Ensure Python is installed and properly configured in your environment to run the scripts.

## Contributions
Contributions are welcome! Please fork the repository and submit pull requests with your enhancements.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.
