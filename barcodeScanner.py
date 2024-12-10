from pyzbar import pyzbar
import cv2
import pandas as pd
import requests
from datetime import datetime
from glob import glob


class Ingredients:
    def __init__(self, ingredient_name, date):
        self.ingredient_name = ingredient_name
        self.date = date
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def deleteFromEnd(self):
        if self.head is None:
            return "The list is empty" 
        if self.head.next is None:
            self.head = None 
            return
        temp = self.head
        while temp.next.next: 
            temp = temp.next
            temp.next = None  

    def add_ingredient(self, new_ingredient_name, new_date):
            new_node = Ingredients(new_ingredient_name,new_date) 
            if self.head is None:
                self.head = new_node  
                self.tail = new_node
                
            else:
                self.tail.next = new_node
                self.tail = new_node
            self.length += 1

    def printList(self):
        temp = self.head 
        while temp:
            print(temp.ingredient_name,end=' ') 
            print(temp.date,end=' ') 
            temp = temp.next 
        print() 



def decode(image):
    # decodes all barcodes from an image
    decoded_objects = pyzbar.decode(image)
    for obj in decoded_objects:
        # draw the barcode
        print("detected barcode:", obj)
        image = draw_barcode(obj, image)
        # print barcode type & data
        print("Type:", obj.type)
        print("Data:", obj.data)
     
        barcode = obj.data.decode("utf-8")
        api_url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
        response = requests.get(api_url)

        if response.status_code == 200:
            product_data = response.json()
            if product_data["status"] == 1:
                product = product_data["product"]
                print(f"Product Name: {product['product_name']}")
                print(f"Brand: {product['brands']}")

            else:
                print("Product not found!")
        else:
            print(f"Failed to fetch data: {response.status_code}")

    return image


def draw_barcode(decoded, image):
    image = cv2.rectangle(image, (decoded.rect.left, decoded.rect.top), 
                            (decoded.rect.left + decoded.rect.width, decoded.rect.top + decoded.rect.height),
                            color=(0, 255, 0),
                            thickness=5)
    return image

def addManually ():
    new_ingredient = input('Enter the name of the ingredient: ')
    date_entry = input('Enter a date (i.e. YYYY,MM,DD): ')
    year, month, day = map(int, date_entry.split(','))
    date = datetime(year, month, day)
    return new_ingredient, date


if __name__ == "__main__":

    llist = LinkedList()
    new_ingredient_name, new_date = addManually ()
    llist.add_ingredient (new_ingredient_name, new_date)
    llist.printList()

    barcodes =  glob(r"C:\Users\ramaa\Downloads\photo_2024-12-06_12-39-01.jpg")
    print(f"Found barcodes: {barcodes}")
    for barcode_file in barcodes:
        img = cv2.imread(barcode_file)
        img = decode(img)
        cv2.imshow("img", img)
        cv2.waitKey(0)
        img = cv2.imread(barcode_file)
        if img is None:
            print(f"Failed to load image: {barcode_file}")
            print(f"You can add manually:\n")     
            continue
        else:
            print(f"Loaded image: {barcode_file}")



