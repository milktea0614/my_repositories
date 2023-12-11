import math
import matplotlib.pyplot as plt
import numpy as np


def hex_to_RGB(hex_str):
    """ #FFFFFF -> [255,255,255]"""
    #Pass 16 to the integer function for change of base
    return [int(hex_str[i:i+2], 16) for i in range(1,6,2)]

def get_color_gradient(c1, c2, n):
    """
    Given two hex colors, returns a color gradient
    with n colors.
    """
    assert n > 1
    c1_rgb = np.array(hex_to_RGB(c1))/255
    c2_rgb = np.array(hex_to_RGB(c2))/255
    mix_pcts = [x/(n-1) for x in range(n)]
    rgb_colors = [((1-mix)*c1_rgb + (mix*c2_rgb)) for mix in mix_pcts]
    return ["#" + "".join([format(int(round(val*255)), "02x") for val in item]) for item in rgb_colors]


if __name__ == "__main__":
    plt.style.use('_mpl-gallery')

    # create data
    standard_x = 200
    standard_y = 300
    distance = 100
    distance_1 = 100

    x_list = []
    y_list = []
    x_list_inverse = []
    y_list_inverse = []

    _move_times = int(180 / 5) + 1

    for i in range(0, _move_times):
        x1 = int(standard_x + (distance * math.cos(math.radians(5*i + 45))))
        y1 = int(standard_y + (distance * math.sin(math.radians(5*i + 45))))
        print(f"[counterclockwise][{5*i + 45}] {x1},{y1}")

        x1_inverse = int(standard_x - (distance_1 * math.cos(math.radians(225-5*i))))
        y1_inverse = int(standard_y - (distance_1 * math.sin(math.radians(225-5*i))))
        print(f"[clockwise] {x1_inverse},{y1_inverse}")

        x_list.append(x1)
        y_list.append(y1)

        x_list_inverse.append(x1_inverse)
        y_list_inverse.append(y1_inverse)


    # plot
    fig, ax = plt.subplots()
    ax.scatter(x_list, y_list, color=get_color_gradient("#ff4133", "#ff928a", len(x_list)))
    ax.scatter(x_list_inverse, y_list_inverse, color=get_color_gradient("#003ba8", "#7dd4ff", len(x_list)))

    ax.set(xlim=(0, 500), ylim=(0, 500))

    plt.show()