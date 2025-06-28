'''
In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:

.gif - image/gif
.jpg - image/jpeg
.jpeg - image/jpeg
.png - image/png
.pdf - application/pdf
.txt - text/plain
.zip - application/zip
If the file's name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.

'''




def main():
    
    file_enter = input("File name: ").lower().strip()
    print(file_mediatype(file_enter))
    
def file_mediatype(file):
    
    
    #Check if each ".ext" in the user input "file" exists
    if '.jpg' in file or '.jpeg' in file:
        return 'image/jpeg'
    elif '.gif' in file:
        return 'image/gif'
    elif '.png' in file:
        return 'image/png'
    elif '.pdf' in file:
        return 'application/pdf'
    elif '.text' in file:
        return 'text/plain'
    elif '.zip' in file:
        return 'application/zip'
    else:
        return 'application/octet-stream'
main()