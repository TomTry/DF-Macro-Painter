# DF-Macro-Painter
A simple python file to create a mining macro for Dwarf Fortress from a PNG image

This is a very simple Python program which iterates over a grayscale PNG image and mines out any white squares in that image.
The starting point for the image / mining is defined by a pixel with grayscale value of 143 so all images must contain such a pixel.
Two parameters need to be supplied: a path for a PNG file and a name for the macro. The macro which is created can then be moved to the DF macros folder and used like any other
