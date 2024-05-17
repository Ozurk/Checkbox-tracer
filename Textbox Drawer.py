import pyautogui as pya
import time
import pyscreeze
import tkinter
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk, ImageGrab


def save_target_image():
    # Check if there is an image in the clipboard
    try:
        img = ImageGrab.grabclipboard()
        if isinstance(img, Image.Image):
            # Ask the user where to save the image
            file_path = 'pics/target.png'
            if file_path:
                # Save the image to the specified path
                img.save(file_path)
                messagebox.showinfo("Success", "Image saved successfully!")
            else:
                messagebox.showwarning("Cancelled", "Image save cancelled.")
        else:
            messagebox.showerror("Error", "No image found in the clipboard.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save image: {e}")


def save_ok_image():
    # Check if there is an image in the clipboard
    try:
        img = ImageGrab.grabclipboard()
        if isinstance(img, Image.Image):
            # Ask the user where to save the image
            file_path = 'pics/ok.png'
            if file_path:
                # Save the image to the specified path
                img.save(file_path)
                messagebox.showinfo("Success", "Image saved successfully!")
            else:
                messagebox.showwarning("Cancelled", "Image save cancelled.")
        else:
            messagebox.showerror("Error", "No image found in the clipboard.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save image: {e}")


def textbox_maker():
    all_textboxes = list(pya.locateAllOnScreen("pics/target.png", confidence=int(confidence_entry.get())/100))
    textbox = all_textboxes[0]
    height = textbox.height
    width = textbox.width

    pya.moveTo(textbox.left + int(overshoot_width.get()), textbox.top + int(overshoot_height.get()))
    pya.click()
    pya.dragTo(textbox.left + width, textbox.top + height, 3, pya.easeOutQuad)
    # set over or under shoot above
    time.sleep(.5)

    pya.moveTo(pya.locateOnScreen("pics/ok.png", confidence=confidence_entry.get()))
    pya.click()
    for textboxes in all_textboxes:
        print(textboxes)
        textbox_maker()


def start_textbox_maker(event=None):
    try:
        attempts = 0
        while attempts < 25:
            try:
                textbox_maker()
            except pyscreeze.ImageNotFoundException:
                pya.scroll(-100)
                attempts += 1
                print("Attempt number: " + str(attempts) + " \nWill quit after 25 failed attempts")
                time.sleep(.25)
            except pya.ImageNotFoundException:
                pya.scroll(-150)
                attempts += 1
                print("Attempt number: " + str(attempts) + " \nWill quit after 25 failed attempts")
                time.sleep(.25)
    except ValueError:
        messagebox.showerror("error", "please enter a valid percentage.")


def force_quit():
    quit()


root = tkinter.Tk()
root.title('Textbox Maker GUI')
target_image = tkinter.Button(root, text="Save Target Image From Clipboard", command=save_target_image)
target_image.pack()
ok_image = tkinter.Button(root, text="Save 'Ok' Image From Clipboard", command=save_ok_image)
ok_image.pack()
confidence_label = tkinter.Label(root, text="Enter the confidence percentage for the target image:")
confidence_label.pack()
confidence_entry = tkinter.Entry(root)
confidence_entry.pack()
overshoot_height_label = tkinter.Label(root, text="Enter the overshoot height distance in pixels")
overshoot_height_label.pack()
overshoot_height = tkinter.Entry(root)
overshoot_height.pack()
overshoot_width_label = tkinter.Label(root, text="Enter the overshoot width distance in pixels")
overshoot_width_label.pack()
overshoot_width = tkinter.Entry(root)
overshoot_width.pack()
start_button = tkinter.Button(root, text="Start", command=start_textbox_maker)
start_button.pack()
force_quit_button = tkinter.Button(root, text="Force Quit", command=force_quit, bg='red', fg='white')
force_quit_button.pack()

root.bind('<Return>', start_textbox_maker)
root.mainloop()


