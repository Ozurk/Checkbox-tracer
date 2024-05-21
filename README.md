When creating forms in the Build-Ops "Form Builder Module", all forms must be drawn on by hand, resulting in sloppy looking forms.
This program uses pyautogui to look for all instances of an image on the screen and draw a text box over each one. 

To use this program: 
1: Make sure there is a recognizable pattern for the program to follow. It matches pixels, so it is very sensitive.

2: Using the snipping tool, save a picture of the field area that it will look for. IE: Each form field has |_________| where the field will go.

3: Copy the snip to the clipboard.

4: Run Checkbox Drawer.exe or checkbox Drawer python.py

5: Click "Copy target image from clipboard"

6: Make sure the "forms" tab is selected within the PDF editor.

7: Draw a textbox by hand

8: Using the Snipping tool, save a screenshot of the blue "Ok" button. Click "Copy Ok pic from clipboard"

9: Set the confidence (85 is a good place to start).

10: Set the overshoot Height and Width

11: Click the start button and let your hand of the mouse.

The confidence for which the program recognized the picture can be changed.
The Overshoot fields are used to fine-tune where the checkbox gets placed..

**Due to the nature of the program, you will not be able to use the mouse while the program is running. Pyautogui has a built-in failsafe.
  To force quit the program, "slam" the cursor into the top right or top left corner of the screen**.

