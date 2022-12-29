import cv2
import sys
import os
from os import path

if len(sys.argv) == 1:
    print("Must be supplied with two parameters: A PNG image and a name of the macro to be created")
    quit()
    
try:
    IMAGE = sys.argv[1]
except:
    print("Error: Need a PNG image to be supplied")
try:
    MACRO_NAME = sys.argv[2]
except:
    print("Error: Need a macro name to be supplied")
cv_image = cv2.imread(IMAGE, 0)

if not path.exists(IMAGE):
    print(IMAGE + " does not appear to be a valid path")
    quit()

if path.splitext(IMAGE)[1] != ".png":
    print(IMAGE + " does not appear to be a PNG file")
    quit()

MACRO_FILE = MACRO_NAME+".mak"
if path.isfile(MACRO_NAME+".mak"):
    print("Macro named " + MACRO_NAME + " already exists, deleting current version.")
    os.remove(MACRO_NAME+".mak")

with open(MACRO_FILE, "a") as file_object:
    file_object.write(MACRO_NAME)
    file_object.write("\n")
    file_object.close()

CURSOR_LEFT = "\t\tKEYBOARD_CURSOR_LEFT\n\tEnd of group\n"
CURSOR_RIGHT = "\t\tKEYBOARD_CURSOR_RIGHT\n\tEnd of group\n"
CURSOR_UP = "\t\tKEYBOARD_CURSOR_UP\n\tEnd of group\n"
CURSOR_DOWN = "\t\tKEYBOARD_CURSOR_DOWN\n\tEnd of group\n"
MINE = "\t\tSELECT\n\tEnd of group\n\t\tSELECT\n\tEnd of group\n"

PICTURE_COLUMNS = cv_image.shape[1]
PICTURE_ROWS = cv_image.shape[0]

for column in range(PICTURE_COLUMNS):
    for row in range(PICTURE_ROWS):
        if cv_image[row][column] == 143:
            start_pos = [row,column]

if not start_pos:
    print("PNG file needs to have a pixel with a grayscale value of 143 which is the 'origin' of the macro. Please amend the image to include this.")
start_pos_row = start_pos[0]
start_pos_column = start_pos[1]

for z in range(start_pos_column):
    with open(MACRO_FILE, "a") as file_object:
        file_object.write(CURSOR_LEFT)
        file_object.close()

for z in range(start_pos_row):
    with open(MACRO_FILE, "a") as file_object:
        file_object.write(CURSOR_UP)
        file_object.close()

for row in range(PICTURE_ROWS):
    for column in range(PICTURE_COLUMNS):
        if cv_image[row][column] != 0:
            with open(MACRO_FILE, "a") as file_object:
                file_object.write(MINE)
                file_object.write(CURSOR_RIGHT)
                file_object.close()
        else:
            with open(MACRO_FILE, "a") as file_object:
                file_object.write(CURSOR_RIGHT)
                file_object.close()
                
        if column == (PICTURE_COLUMNS-1):
            with open(MACRO_FILE, "a") as file_object:
                file_object.write(CURSOR_DOWN)
                file_object.close()
                for res in range(PICTURE_COLUMNS):
                    with open(MACRO_FILE, "a") as file_object:
                        file_object.write(CURSOR_LEFT)
                        file_object.close()
                file_object.close()

with open(MACRO_FILE, "a") as file_object:
    file_object.write("End of macro\n")
    file_object.close()
    print("Macro written")
