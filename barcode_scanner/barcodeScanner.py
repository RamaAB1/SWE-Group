from pyzbar import pyzbar
import cv2
import pandas as pd
import requests
from datetime import datetime
from glob import glob
from Base_code import Ingredient, Node,Linked_list

def decode(image):
   
    decoded_objects = pyzbar.decode(image)
    for obj in decoded_objects:
        image = draw_barcode(obj, image)
        barcode = obj.data.decode("utf-8")
        api_url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
        response = requests.get(api_url)

        if response.status_code == 200:
            product_data = response.json()
            if product_data["status"] == 1:
                product = product_data["product"]
          
            else:
                print("Product not found!")
        else:
            print(f"Failed to fetch data: {response.status_code}")

    return image, f"Product Name: {product['product_name']}", f"Brand: {product['brands']}"


def draw_barcode(decoded, image):
    image = cv2.rectangle(image, (decoded.rect.left, decoded.rect.top), 
                            (decoded.rect.left + decoded.rect.width, decoded.rect.top + decoded.rect.height),
                            color=(0, 255, 0),
                            thickness=5)
    return image

def addManually (new_ingredient, date_entry):
    # year, month, day = map(int, date_entry.split('/'))
    date = datetime.strptime(date_entry,"%Y-%m-%d").date()
    # datetime(year, month, day)
    return new_ingredient, date

def Barcode_reader ():
    barcodes =  glob(r"C:\Users\ramaa\Downloads\SWE\SWE-Group-main\SWE-Group-main\SWE-Group\hotSauce_barcode.jpg")
    # print(f"Found barcodes: {barcodes}")
    for barcode_file in barcodes:
        img = cv2.imread(barcode_file)
        img,name,brand = decode(img)
        print(name,brand)

        cv2.imshow("img", img)
       
        if img is None:
            return f"Failed to load image: {barcode_file}"
        else:
            return f"Loaded image: {barcode_file}"


if __name__ == "__main__":

    new_list = Linked_list()

    new_ingredient, date_entry = addManually (input('Enter the name of the ingredient: \n'), input('Enter a date (i.e. YYYY-MM-DD): '))
    print( addManually("Milk", "2024-12-17"))
    new_list = Linked_list()
    new_list.insert_end(Ingredient(new_ingredient,date_entry))
    

    Barcode_reader()
  



