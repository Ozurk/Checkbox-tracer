import pyautogui as pya
import time
import pyscreeze
import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk, ImageGrab
import collections


def save_ok_image():
    # Check if there is an image in the clipboard
    try:
        img = ImageGrab.grabclipboard()
        if isinstance(img, Image.Image):
            # Ask the user where to save the image
            file_path = '../pics/ok.png'
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


def save_target_image():
    # Check if there is an image in the clipboard
    try:
        img = ImageGrab.grabclipboard()
        if isinstance(img, Image.Image):
            # Ask the user where to save the image
            file_path = '../pics/target.png'
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


def create_help_window():
    help_window = tk.Tk()
    help_window.geometry("800x800")
    help_frame = tk.Frame(help_window)
    help_frame.columnconfigure(0, weight=1)
    help_frame.pack(fill="x")
    header = tk.Label(help_frame, text="How to use this tool", bg="#84cc34", fg="black",
                      font=("Times New Roman", 20, "bold"),width=850)
    header.grid(column=0, row=0, sticky=tk.NW)

    step_1_label = tk.Label(help_frame, text="Step 1", bg="#a8a8a8")
    step_1_label.grid(column=0, row=1, sticky=tk.NW, padx=15)

    step_1_text = tk.Message(help_frame, text="Begin by setting the zoom of the Build-Ops webpage to where all "
                                              "fields are in frame, and the window zoomed in as close as possible")
    step_1_text.grid(column=0, row=2, sticky=tk.NW, padx=15)

    step_2_label = tk.Label(help_frame, text="Step 2", bg="#a8a8a8")
    step_2_label.grid(column=0, row=3, sticky=tk.NW, padx=15)

    step_2_text = tk.Message(help_frame, text="""	
Take a screenshot of the empty form field using the snipping tool.
Start As close as possible to the top left corner of the field, without cropping anything out.
Drag to the bottom right corner of the field. 
This tool may take some trial and error to get the edges cropped correctly.
Copy the image to the clipboard.""", width="850")
    step_2_text.grid(column=0, row=4, sticky=tk.NW)

    step_3_label = tk.Label(help_frame, text="Step 3", bg="#a8a8a8")
    step_3_label.grid(column=0, row=5, sticky=tk.NW, padx=15)

    step_3_text = tk.Message(help_frame, text="Click the “Copy Target image from Clipboard” button.")
    step_3_text.grid(column=0, row=6, sticky=tk.NW)

    step_4_label = tk.Label(help_frame, text="Step 4", bg="#a8a8a8")
    step_4_label.grid(column=0, row=7, sticky=tk.NW, padx=15)

    step_4_text = tk.Message(help_frame, text="""
On the Build-Ops webpage, click forms draw a small textbox somewhere and take a screenshot of the blue button using the snipping tool.
From here click and drag a small textbox somewhere on the screen.
This will cause a dialog box to appear with some controls on it. 
take a screenshot of the blue “OK” button.
Click the “Save Ok Image from Clipboard” button on the application window.""", width="850")
    step_4_text.grid(column=0, row=8, sticky=tk.NW, padx=10, pady=10)

    step_5_label = tk.Label(help_frame, text="Step 5", bg="#a8a8a8")
    step_5_label.grid(column=0, row=9, sticky=tk.NW, padx=15)

    step_5_text = tk.Message(help_frame, text="""
Set the confidence percentage and overshoot distances.
Confidence is a number between 1 and 100. 
The higher the confidence, the “pickier” the program is about matching the target photo. 
If the confidence is set too high, the application will miss fields.
If the confidence is set too low, the application will add fields where they are not wanted.
A good starting point is 85.
Overshoot X and Y are the distances (In pixels) the application overshoots the bottom right corner.
A higher overshoot width with result in the box being created wider.
A higher overshoot height will result in a taller box
The overshoot fields do not affect the starting position. Only the ending position.
The speed at which the program works can be changed as well. 
The smaller the number, the faster the textboxes will be created.
The faster the program runs, the harder it is to stop if it is needed so be careful.
As the speed increases, the overshoot values will need to be increased.
""", width="850")
    step_5_text.grid(column=0, row=10, sticky=tk.NW)


class TextBoxDrawer:
    def __init__(self):
        self.start_button_text_var = None
        self.start_button = None
        self.overshoot_height_variable = None
        self.speed_variable = None
        self.header = None
        self.speed = None
        self.overshoot_height_entry = None
        self.main_frame = None
        self.overshoot_width_entry = None
        self.overshoot_height = None
        self.confidence_entry = None
        self.ok_image = None
        self.target_image = None
        self.root = None
        self.create_application()

    def create_application(self):
        self.root = tk.Tk()
        self.root.resizable(False, False)
        self.root.title('Build-Ops Form Field creator')
        self.root.iconbitmap("../pics/logo.ico")
        core_logo = Image.open("../pics/logo.gif")
        core_logo_copy = core_logo
        core_image = ImageTk.PhotoImage(core_logo_copy)
        self.header = tk.Label(self.root, image=core_image, bg="#ffffff")
        self.header.image = core_image
        self.header.pack(fill="x")
        self.main_frame = tk.Frame(self.root, bg="#a8a8a8")

        self.main_frame.rowconfigure(0, weight=1)
        self.main_frame.rowconfigure(1, weight=1)
        self.main_frame.rowconfigure(2, weight=1)
        self.main_frame.rowconfigure(10, weight=1)
        self.main_frame.pack()

        self.target_image = tk.Button(self.main_frame, text="Save Target Image From Clipboard",
                                      command=save_target_image, borderwidth=5, bg="#84cc34",
                                      font=("Cambria", 10, "bold"))
        self.target_image.grid(row=0, column=0, sticky=tk.NSEW, padx=10, pady=10)

        self.ok_image = tk.Button(self.main_frame, text="Save 'Ok' Image From Clipboard", command=save_ok_image,
                                  borderwidth=5, bg="#84cc34", font=("Cambria", 10, "bold"))
        self.ok_image.grid(row=0, column=1, sticky=tk.NSEW, padx=10, pady=10)

        confidence_label = tk.Label(self.main_frame, text="Enter the confidence percentage for the target image:")
        confidence_label.grid(row=1, column=0, columnspan=2, sticky=tk.NSEW)

        confidence_variable = tk.StringVar()
        confidence_variable.set("85")

        self.confidence_entry = tk.Spinbox(self.main_frame, from_=50, to=100, increment=1,
                                           textvariable=confidence_variable,
                                           justify=tk.CENTER)
        self.confidence_entry.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.overshoot_height_variable = tk.StringVar()
        self.overshoot_height_variable.set("0")
        overshoot_height_label = tk.Label(self.main_frame, text="Enter the overshoot height distance in pixels")
        overshoot_height_label.grid(row=3, column=0, columnspan=2, sticky=tk.NSEW)

        self.overshoot_height_entry = tk.Spinbox(self.main_frame, from_=0, to=100, increment=1,
                                                 textvariable=self.overshoot_height_variable,
                                                 justify=tk.CENTER)
        self.overshoot_height_entry.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        overshoot_width_label = tk.Label(self.main_frame, text="Enter the overshoot width distance in pixels")
        overshoot_width_label.grid(row=5, column=0, columnspan=2, sticky=tk.NSEW)
        self.overshoot_width_entry = tk.Spinbox(self.main_frame, from_=0, to=100, increment=1,
                                                justify=tk.CENTER)
        self.overshoot_width_entry.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        speed_label = tk.Label(self.main_frame, text="Enter the time (in seconds) each box is 'drawn'")
        speed_label.grid(row=7, column=0, columnspan=2, sticky=tk.NSEW)
        self.speed_variable = tk.StringVar()
        self.speed_variable.set("3")
        self.speed = tk.Spinbox(self.main_frame, from_=.01, to=10, increment=.1, textvariable=self.speed_variable,
                                justify="center")
        self.speed.grid(row=8, column=0, columnspan=2, padx=10, pady=10)
        self.start_button_text_var = tk.StringVar(self.main_frame)
        self.start_button_text_var.set("Start")
        self.start_button = tk.Button(self.main_frame, textvariable=self.start_button_text_var,
                                      command=self.start_textbox_maker,
                                      font=("Cambria", 20, "bold"), bg="#79B532", borderwidth=7)
        self.start_button.grid(row=9, column=0, columnspan=2, sticky=tk.NSEW)
        credit_hunter = tk.Label(self.main_frame, text="Created By Hunter Metzger", bg='black', fg='white',
                                 anchor=tk.SW)
        credit_hunter.grid(row=11, column=0, columnspan=2, sticky=tk.NSEW)
        help_button = tk.Button(self.main_frame, bitmap="question", command=create_help_window)
        help_button.grid(row=10, columnspan=2, sticky=tk.NSEW)
        self.main_frame.bind('<Return>', self.start_textbox_maker)

    def create_textbox(self):
        time.sleep(.1)
        all_textboxes = list(
            pya.locateAllOnScreen("../pics/target.png", confidence=int(self.confidence_entry.get()) / 100))
        textbox = all_textboxes[0]
        height = textbox.height
        width = textbox.width
        overshoot_height = int(self.overshoot_height_entry.get())
        overshoot_width = int(self.overshoot_width_entry.get())
        speed = float(self.speed.get())
        print(f"Instances of target images on screen = {all_textboxes}")
        pya.moveTo(textbox.left, textbox.top)
        pya.click()
        pya.dragTo(textbox.left + width + int(overshoot_width),
                   textbox.top + height + int(overshoot_height),
                   speed, pya.easeOutQuad)
        # set over or under shoot above
        pya.moveTo(pya.locateOnScreen("../pics/ok.png", confidence=.8))
        pya.click()
        time.sleep(.5)
        for textboxes in all_textboxes:
            # print(f"Instances of target images on screen = {len(all_textboxes)}", textbox)

            self.create_textbox()

    def run_mainloop(self):
        self.root.mainloop()

    def start_textbox_maker(self, event=None):
        try:
            attempts = 0
            while attempts < 100:
                if attempts == 99:
                    pya.scroll(5000)
                try:
                    self.create_textbox()
                except pyscreeze.ImageNotFoundException as e:
                    pya.scroll(-50)
                    attempts += 1
                    self.start_button_text_var.set(f"looking for target image: attempt number: {attempts}")
                    self.start_button.update()
                except pya.ImageNotFoundException as e:
                    self.start_button_text_var.set(f"looking for target image: attempt number: {attempts}")
                    self.start_button.update()
                    pya.scroll(-50)
                    attempts += 1

        except ValueError:
            messagebox.showinfo("error", "Please fill out all the fields.")


if __name__ == "__main__":
    application = TextBoxDrawer()
    application.run_mainloop()
