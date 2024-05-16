When creating forms in the Build-Ops "Form Builder Module", all forms must be drawn on by hand, resulting in sloppy looking forms.
This program uses pyautogui to look for all instances of an image on the screen and draw a text box over each one. 

To use this program: 
1: Make sure there is a recognizable pattern for the program to follow. It matches pixels, so it is very sensitive.
2: Using the snipping tool, save a picture of the field area that it will look for. IE: Each form field has |_________| where the field will go.
3: Save the picture as target.png within the pics subfolder
4: Make sure the "forms" tab is selected within the PDF editor.
5: Run the program, it should draw a box then crash with the "ImageNotFoundException". 
6: Using the Snipping tool, save a screenshot of the blue "Ok" button.
7: Press Ok, then Restart the program.

The confidence for which the program recognized the picture can be changed.
The distance the program over or undershoots the target distance can be changed.


