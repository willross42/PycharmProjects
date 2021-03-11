import requests
import csv
import os

def detect_filetype(link):

    link = "https://www.indiandcold.com/media/photo_export.csv"
    url_length = len(link)
    end_url = link[url_length - 3:url_length]

    # If url ends in csv download file and use csv sniffer to verify
    if end_url == "csv" or end_url == "tsv" or end_url == "xml" or end_url == "zip ":
        extension = end_url

        # Write to csv file "downloaded.csv"
        req = requests.get(link)
        url_content = req.content
        csv_file = open("downloaded.csv", 'wb')
        csv_file.write(url_content)
        csv_file.close()

        print(url_content)
        # Detect deliminator
        f = open("downloaded.csv", 'r')
        with f:
            reader = csv.reader(f)
            next(reader)  # Skip header row.

            sample_bytes = 1024
            sniffer = csv.Sniffer()
            csv_dialect = sniffer.sniff(
            open("downloaded.csv").read(sample_bytes))
            csv_file.close()

        print("For url: ", link, "\nDeliminator: ", csv_dialect.delimiter)

        os.remove("downloaded.csv")

        if csv_dialect.delimiter != "|":
            extension = "invalid deliminator"
        else:
            extension = "definately " + extension

    else:
        extension = "unknown"

    return extension
