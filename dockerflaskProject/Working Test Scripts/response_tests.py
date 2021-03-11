import requests
import csv

def main():
    # Test URLs, comment out as required
    link1 = "https://www.indiandcold.com/media/photo_export.csv"
    link2 = "http://commondatastorage.googleapis.com/newfeedspec/example_feed_txt.zip"
    link3 = "https://factionskis.com/pages/photoslurp-product-feed"

    link = link3

    xml_tag = '<?xml version="1.0" encoding="UTF-8" ?>'
    xml_comp = "['" + xml_tag + "']"

    # Get status codes
    req = requests.get(link)
    status = req.status_code
    print(req)
    print(status)
    if status == 200:
        print('Success!')
    elif status == 404:
        print('Not Found.')

    # content = response.content
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

        print(row2)
        # If header row matchs XML template then is XML, else test for CSV or TSV
        if xml_comp in str(row2):
            extension = "XML"

        else:
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

        print("File format: " + extension)


main()