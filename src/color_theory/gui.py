import colorsys
import tkinter
from dataclasses import dataclass, field
from tkinter import messagebox, ttk
from tkinter.colorchooser import askcolor

import sv_ttk

""" Code examples taken from:
https://thingsgrow.me/2020/01/02/navigating-through-000000-and-ffffff-color-theory-in-python/
https://www.pythontutorial.net/tkinter/tkinter-color-chooser/
https://stackoverflow.com/a/3380739
"""


@dataclass
class ColorHolder:
    chooser_value: tuple = field(default_factory=tuple)
    complement_value: tuple = field(default_factory=tuple)
    backflip: bool = False

    def rgb(self, color_data="picked"):
        if color_data == "picked":
            return self.chooser_value[0]
        elif color_data == "complement":
            return self.complement_value[0]
        else:
            raise ValueError("Wrong value passed to method")

    def hex(self, color_data="picked"):
        if color_data == "picked":
            return self.chooser_value[1]
        elif color_data == "complement":
            return self.complement_value[1]
        else:
            raise ValueError("Wrong value passed to method")


root = tkinter.Tk()
root.title("Fishing For Complements")
root.geometry("350x250")
sv_ttk.set_theme("dark")
color_info = ColorHolder()


def choose_color():
    color_info.chooser_value = askcolor(title="Tkinter Color Chooser")
    root.configure(bg=color_info.hex())


def invert_color(color_rgb: tuple):
    # value has to be 0 < x 1 in order to convert to hls
    r, g, b = map(lambda x: x / 255.0, color_rgb)
    # hls provides color in radial scale
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    # get hue changes at 150 and 210 degrees
    deg_180_hue = h + (180.0 / 360.0)
    color_180_rgb = tuple(
        map(lambda x: round(x * 255), colorsys.hls_to_rgb(deg_180_hue, l, s))
    )
    hex_color = "#%02x%02x%02x" % (color_180_rgb)
    return color_180_rgb, hex_color


def complementary_color():
    try:
        rgb_color = color_info.rgb()
    except IndexError:
        messagebox.showerror(title="Error", message="Please select a color first")
        return
    rgb_color, hex_color = invert_color(rgb_color)
    if not color_info.backflip:
        color_info.complement_value = (rgb_color, hex_color)
        color_info.backflip = True
        root.configure(bg=color_info.hex("complement"))
    else:
        root.configure(bg=color_info.hex())
        color_info.backflip = False


ttk.Button(root, text="Select a color", command=choose_color).pack(expand=True)
ttk.Button(root, text="Show complementary color", command=complementary_color).pack(
    expand=True
)


def main():
    root.mainloop()


if __name__ == "__main__":
    main()
