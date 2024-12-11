import cv2
import easyocr
import datefinder

def getDate (path):
    try:
        image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

        reader = easyocr.Reader(['en'])
        result = reader.readtext(image)

        text = ""
        for (bbox, txt, prob) in result:
            text += (txt + " ")

        dates = list(datefinder.find_dates(text))

        if len(dates) != 0:
            date = dates[0].date()
            return str(date)

    except:
        return("Image not found")
