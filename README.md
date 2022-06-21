# PDF_GENERATOR

## Description

Generate "X" number of PDF files based on a terminal input field, insert lorem text, and save with UUID naming. Output the files to a directory. Save file names to .XLSX format for help with further processing (to be further used for generating XML for import processes etc.)

This is a rudimentary application run from command line, with no error handling on input and it will exit with errors if invalid inputs are received. I may come back to this as an enhancment later. Please sumbit a pull request if you are interested.

## Getting Started

### Dependencies

* Written on Python 3.10 
* See requirements.txt file for other library dependencies.
* Setup a venv


### Installing

* Clone and run locally, or run from cloud-based REPL
* .gitignore excludes output directories and .env file
* Create output_pdfs directory at project root so the app won't fail
* Create .env file using .env_example.txt as template

### Main Project Structure
```text
PDF_GENERATOR/
    └── output_pdfs/ <generated PDFs end up here>
    └──  venv/...
    └── output_names.csv <generated filename end up here>
    └── .env (see .env_example.txt for env variables)
    └── main.py
    └── README.md
    └── LICENSE.md
```

### Executing program

* Run from the command line
* Input desired number of PDF files


## Help

* No error handling on input field so it requires a valid input that can be cast to ```int``` - will error out if blank input is entered.

## Authors

* Craig Forsberg

## Version History

* 1.0
    * Initial Release

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
