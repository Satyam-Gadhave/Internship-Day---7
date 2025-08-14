# Internship-Day---7
Image resizer tool

First we import "os", its a built in module that helps interact with the computer's file system, and "Image" it is the class inside PIL that lets us open, edit, save images.
Then we creates folders to store our original images(input) and  a folder to store the resized images(output).
We use new_size a tuple meaning width 400 pixels and height 400 pixels.
os.makedirs() is used to create a new folder and parent folder if needed.exist_ok=True avoids an error if the folder already exists.
We then use the for keyword to create a loop that run the intended block for each file in the folder.
We use if to create a condition that will run only when certain functions are fulfilled.
We then use try and except to find out any error that may occur during execution.
