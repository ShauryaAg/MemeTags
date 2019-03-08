from PIL import Image
import pytesseract
import csv
import os
import test


pathname = 'C:\\Users\\Shaurya Agarwal\\Documents\\HackathonProject\\MemeTagging\\test_images'
filenamelist = os.listdir(pathname)

lines = [["FilePath", "Tags", "MemeTemplate"]]
file_ext = [".png", ".jpeg", ".jpg"]

for imagename in filenamelist:
    for file_ext_name in file_ext:
        if file_ext_name in imagename:
            filename = pathname + "\\" + imagename

            text = pytesseract.image_to_string(Image.open(filename))

            text = text.replace("\n", " ")

            x = test.ret_strClassification(filename)
            lines.append([filename, text, x])

            with open('memetags.csv', 'w') as writeFile:
                writer = csv.writer(writeFile)
                writer.writerows(lines)
            writeFile.close()




def ret_dirPath():
    return pathname