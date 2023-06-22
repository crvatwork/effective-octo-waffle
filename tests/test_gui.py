import pytest

from color_theory import gui
from color_theory.gui import ColorHolder

blue_rgb = (0, 0, 255)
blue_hex = "#0000ff"
yellow_rgb = (255, 255, 0)
yellow_hex = "#ffff00"


def test_invert_color():
    color_180_rgb, color_180_hex = gui.invert_color(blue_rgb)
    assert color_180_rgb == yellow_rgb
    assert color_180_hex == yellow_hex


def test_color_holder():
    test_holder = ColorHolder()
    test_holder.chooser_value = (blue_rgb, blue_hex)
    test_holder.complement_value = (yellow_rgb, yellow_hex)
    assert test_holder.backflip is False
    assert test_holder.hex("complement") == yellow_hex
    assert test_holder.hex() == blue_hex
    assert test_holder.rgb("complement") == yellow_rgb
    assert test_holder.rgb() == blue_rgb
    with pytest.raises(ValueError):
        test_holder.rgb("bogus")
    with pytest.raises(ValueError):
        test_holder.hex("dude")
