def detect_filetype(link):
    url_length = len(link)
    end_url = link[url_length - 3:url_length]

    if end_url == "csv" or end_url == "tsv" or end_url == "xml":
        extension = end_url

    else:
        extension = "unknown"
    return extension
