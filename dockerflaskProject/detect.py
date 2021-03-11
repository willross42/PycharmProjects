import requests
import csv
import os

def detect_filetype(link):
    xml_tag = '<?xml version="1.0" encoding="UTF-8" ?>'
    xml_comp = "['" + xml_tag + "']"

    # Get status codes
    req = requests.get(link)
    status = req.status_code
    print("ATTEMPTING DETECT:\n", req)
    if status == 200:
        print('Success!')
    elif status == 404:
        print('Not Found.')

    url_content = req.content
    # print(url_content)

    csv_file = open("catalogue.csv", 'wb')
    csv_file.write(url_content)
    csv_file.close()

    print("First line is :")

    with open('catalogue.csv', newline='') as f:
        reader = csv.reader(f)
        next(reader)
        row2 = next(reader)  # gets the first line

        # Ignore Header row
        print(row2)
        # If first relevant row matches XML template then is XML, else test for CSV or TSV
        if xml_comp == str(row2):
            extension = "XML"

        else:
            try:
                sample_bytes = 1024
                sniffer = csv.Sniffer()
                csv_dialect = sniffer.sniff(
                    open("catalogue.csv").read(sample_bytes))
                csv_file.close()
                print("For url: ", link, "\nDeliminator: ", csv_dialect.delimiter)

                if csv_dialect.delimiter == "|":
                    extension = "CSV"
                else:
                    extension = "invalid delimiter "

            except:
                extension = "unknown"

        print("File format: " + extension)

    return extension
