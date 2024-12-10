import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'
image = cv2.imread("img.png", cv2.IMREAD_GRAYSCALE)

#OTSU threshold
ret, thresh1 = cv2.threshold(image, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

#numbers in argument can be changed, they change the output
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (40, 40))

# Apply dilation on threshold image
dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)

# Find contours
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# Create text file
file = open("recognised.txt", "w+")
file.write("")
file.close()

# Create copy of image
img_cpy = image.copy()

# recognised = []

for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    
    # Draw a rectangle on copied image
    rect = cv2.rectangle(img_cpy, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Crop the text block for giving input to OCR
    cropped = img_cpy[y:y + h, x:x + w]

    # Apply OCR on the cropped image
    text = pytesseract.image_to_string(cropped)

    # recognised.append(text)
    # Open the file in append mode and append text to file
    file = open("recognised.txt", "a")
    file.write(text)
    file.write("\n")
    
    # Close the file
    file.close()

# print(recognised)


# # We can read image by path by
#     # image_path = 'path_to_image.jpg'
#     # image = cv2.imread(image_path)
#     # if image is not None:
#     #     cv2.imshow('Image', image)
#     #     cv2.waitKey(0)
#     #     cv2.destroyAllWindows()
#     # else:
#     #     print("Couldn't load image")
# # If image not found it returns None
# # We can read image in color by changing second argument in imread to cv2.IMREAD_COLOR
# # We can save the output picture by using cv2.imwrite('path_to_output.jpg', (name of variable for read image ))
# # #To maintain same dimension ratio, just smaller image
#     # (h, w) = image.shape[:2]
#     # ratio = h / w
#     # new_width = 600
#     # new_height = int (ratio * new_width)
#     # resized_image = cv2.resize(image, (new_width, new_height))

# # resized_image = cv2.resize(image, (600, 400))
# # cv2.imshow("resized", resized_image)


# image = cv2.imread("Smile.jpg")
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# # window_name = "Image"
# # cv2.imshow(window_name, image)

# ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
# rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (20, 20))
# diltion = cv2.dilate(thresh1, rect_kernel, iterations = 1)
# contours, hirearchy = cv2.findContours(diltion, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# file = open("recognised.txt", "w+")
# file.write ("")
# file.close()

# # cntr_list = []
# for cntr in contours:
#     x, y, w, h = cv2.boundingRect(cntr)

# imgcpy = gray.copy()
# rect = cv2.rectangle(imgcpy, (x, y), (x+w, y+h), (0, 255, 0), 2)
# cropped = imgcpy[y:y + h, x:x + w]

# file = open("recognised.txt", "a")
# text = pytesseract.image_to_string(cropped)

# file.write(text)
# file.write("\n")
# file.close()
# # cntr_list.append([x, y, text])

# cv2.waitKey(0)
# cv2.destroyAllWindows()