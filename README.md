# MemeTags

### AI for entertainment

## Description:

You know how often you know that you have perfect meme for the situation, but you just can't find it in that large meme archive of yours. So, Here we present an application to tag your memes automatically taking various attributes like the text in the meme, the template of the meme and some other features. 

So, here we are using tesseract for the OCR purposes and inception architechture to classify memes on the basis of meme template.
It takes the path of the directory of the memes and creates a csv file with the image path, the text in the meme, and the meme template name.

The model currently trained was trained using realy less amout of data, so first, it can be trained using a lot of different meme templates and a lot of other attributes.

The tesseract architecture used has a lot of limitations and can only detect text if it is written properly. So, in the future we may use some other algorithm for the OCR purposes to get better results.

#### Prerequisites:

Download and install tesseract architechture using these links [tesseract-ocr-w64-setup-v4.0.0.20181030.exe](https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v4.0.0.20181030.exe) (64-bit), [tesseract-ocr-w32-setup-v4.0.0.20181030.exe](https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w32-setup-v4.0.0.20181030.exe) (32-bit) or [tesseract-ocr-setup-3.05.02-20180621.exe](https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-setup-3.05.02-20180621.exe), and add Tesseract-OCR directory to the Path. 

Also, install the following libraries: pillow and pytesseract, using ```pip install pillow``` and ```pip install pytesseract```
respectively.

### Instructions:

Create a folder named ```./training_images``` and make sub-directories of the different image classifications in it.
Next, create a folder named ```./test_images``` and put the images to be classified in that.

Now, run the retrain.py file to train the model and run the test.py file to test the model.
and then run main.py file classify the memes and create the .csv file.


## Screeenshot

![Screenshot of CSV file created](https://github.com/ShauryaAg/MemeTags/blob/master/CSVFileScreenshot.png)

## Future Scope:

In the future we may use this application to give recommendations on the basis of the person's likes and dislikes. Also, it will help search engines and to look for certain memes on the basis of search criteria.
In the future, we may add a feature to classify meme on the basis of type of meme that it is (if it's a dark humor or not OR if it's a programming meme or not and some more categories like this). The way we may implement this is by using NLP on the extracted text.

