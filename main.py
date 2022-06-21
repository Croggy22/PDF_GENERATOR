import pprint
import uuid
import lorem
import pandas as pd
from reportlab.pdfgen.canvas import Canvas
from decouple import config
PDF_OUTPUT_PATH = config('PDF_OUTPUT_PATH')
CSV_OUTPUT_PATH = config('CSV_OUTPUT_PATH')

# Create empty list to store file names into
names = []
files_to_create = input("How may files do you want to create? ")

# Loop over range from input
# Create files with UUID to ensure uniqueness, append each to names[]
# Output each file to dir
# Open and draw text at coords from random lorem sentence then save back to dir
for i in range(int(files_to_create)):
    name = f"Test-{uuid.uuid4()}.pdf"
    names.append(name)
    canvas = Canvas(f"output_pdfs/{name}")
    canvas.drawString(10, 700, f'{lorem.sentence()}')
    canvas.save()
pprint.pp(f'Printing list of names: {names}')

# Create pandas DataFrame given list of names[]
# Output names to .csv file for further processing
df = pd.DataFrame(names)
df.to_csv('output_names.csv', header=False)

# Create clickable links within terminal to file paths for convenience in post-processing
print(f"PDF Output generated: file:///{PDF_OUTPUT_PATH}")
print(f"Excel Output generated: file:///{CSV_OUTPUT_PATH}")
