import colorsys
import tkinter
from tkinter import messagebox, ttk
from tkinter.colorchooser import askcolor

import sv_ttk

""" Code examples taken from:
https://thingsgrow.me/2020/01/02/navigating-through-000000-and-ffffff-color-theory-in-python/
https://www.pythontutorial.net/tkinter/tkinter-color-chooser/
https://stackoverflow.com/a/3380739
"""

root = tkinter.Tk()
root.title("Fishing For Compliments")
root.geometry("350x250")
sv_ttk.set_theme("dark")
color_info = {}


def choose_color():
    color_info["picked"] = askcolor(title="Tkinter Color Chooser")
    color_info["backflip"] = False
    root.configure(bg=color_info["picked"][1])


def complimentary_color():
    try:
        val = color_info["picked"][0]
    except KeyError:
        messagebox.showerror(title="Error", message="Please select a color first")
        return
    # value has to be 0 < x 1 in order to convert to hls
    r, g, b = map(lambda x: x / 255.0, val)
    # hls provides color in radial scale
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    # get hue changes at 150 and 210 degrees
    deg_180_hue = h + (180.0 / 360.0)
    color_180_rgb = list(
        map(lambda x: round(x * 255), colorsys.hls_to_rgb(deg_180_hue, l, s))
    )
    hex_color = "#%02x%02x%02x" % (tuple(color_180_rgb))
    if not color_info["backflip"]:
        color_info["complement"] = (tuple(color_180_rgb), hex_color)
        color_info["backflip"] = True
        root.configure(bg=color_info["complement"][1])
    else:
        root.configure(bg=color_info["picked"][1])
        color_info["backflip"] = False


ttk.Button(root, text="Select a color", command=choose_color).pack(expand=True)

ttk.Button(root, text="Show complimentary color", command=complimentary_color).pack(
    expand=True
)


def main():
    root.mainloop()


if __name__ == "__main__":
    main()
