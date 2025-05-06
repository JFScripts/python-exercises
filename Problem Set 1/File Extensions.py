def main():
    file = input("Type the name of a file:\n")
    file, format = file.upper().split(".")

    match format:
        case "AAC":
            print("audio/aac")
        case "ABW":
            print("application/x-abiword")
        case "ARC":
            print("application/x-freearc")
        case "AVI":
            print("video/x-msvideo")
        case "AZW":
            print("application/vnd.amazon.ebook")
        case "BIN":
            print("application/octet-stream")
        case "BMP":
            print("image/bmp")
        case "BZ":
            print("application/x-bzip")
        case "BZ2":
            print("application/x-bzip2")
        case "CSH":
            print("application/x-csh")
        case "CSS":
            print("text/css")
        case "CSV":
            print("text/csv")
        case "DOC":
            print("application/msword")
        case "DOCX":
            print("application/vnd.openxmlformats-officedocument.wordprocessingml.document")
        case "EOT":
            print("application/vnd.ms-fontobject")
        case "EPUB":
            print("application/epub+zip")
        case "GIF":
            print("image/gif")
        case "HTM" | "HTML":
            print("text/html")
        case "ICO":
            print("image/vnd.microsoft.icon")
        case "ICS":
            print("text/calendar")
        case "JAR":
            print("application/java-archive")
        case "JPEG" | "JPG":
            print("image/jpeg")
        case "JS":
            print("text/javascript")
        case "JSON":
            print("application/json")
        case "JSONLD":
            print("application/ld+json")
        case "MID" | "MIDI":
            print("audio/midi")
        case "MJS":
            print("text/javascript")
        case "MP3":
            print("audio/mpeg")
        case "MP4":
            print("video/mp4")
        case "MPEG":
            print("video/mpeg")
        case "MPKG":
            print("application/vnd.apple.installer+xml")
        case "ODP":
            print("application/vnd.oasis.opendocument.presentation")
        case "ODS":
            print("application/vnd.oasis.opendocument.spreadsheet")
        case "ODT":
            print("application/vnd.oasis.opendocument.text")
        case "OGA":
            print("audio/ogg")
        case "OGV":
            print("video/ogg")
        case "OGX":
            print("application/ogg")
        case "OTF":
            print("font/otf")
        case "PNG":
            print("image/png")
        case "PDF":
            print("application/pdf")
        case "PPT":
            print("application/vnd.ms-powerpoint")
        case "PPTX":
            print("application/vnd.openxmlformats-officedocument.presentationml.presentation")
        case "RAR":
            print("application/vnd.rar")
        case "RTF":
            print("application/rtf")
        case "SH":
            print("application/x-sh")
        case "SVG":
            print("image/svg+xml")
        case "SWF":
            print("application/x-shockwave-flash")
        case "TAR":
            print("application/x-tar")
        case "TIF" | "TIFF":
            print("image/tiff")
        case "TS":
            print("video/mp2t")
        case "TTF":
            print("font/ttf")
        case "TXT":
            print("text/plain")
        case "VSD":
            print("application/vnd.visio")
        case "WAV":
            print("audio/wav")
        case "WEBA":
            print("audio/webm")
        case "WEBM":
            print("video/webm")
        case "WEBP":
            print("image/webp")
        case "WOFF":
            print("font/woff")
        case "WOFF2":
            print("font/woff2")
        case "XHTML":
            print("application/xhtml+xml")
        case "XLS":
            print("application/vnd.ms-excel")
        case "XLSX":
            print("application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        case "XML":
            print("application/xml")
        case "XUL":
            print("application/vnd.mozilla.xul+xml")
        case "ZIP":
            print("application/zip")
        case "3GP":
            print("video/3gpp")
        case "3G2":
            print("video/3gpp2")
        case "7Z":
            print("application/x-7z-compressed")
        case _:
            print("application/octet-stream")



main()
