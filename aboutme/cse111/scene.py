
import tkinter as tk
from random import randrange

def main():
    # The width and height of the scene window.
    width = 800
    height = 500
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

# creating a frame object
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Calling the draw scene function
    draw_scene(canvas, 0, 0, width-1, height-1)
    root.mainloop()


def draw_scene(canvas, left_scene, top_scene, scene_right, scene_bottom):

    tree_middle = left_scene + 700
    tree_at_top = top_scene + 255

    height_of_tree = 150
    roof_top_y = top_scene + 120
    roof_top_x = left_scene + 250
    left_roof_y = top_scene + 300
    left_roof_x = left_scene + 250
    right_roof_y = top_scene + 300
    right_roof_x = left_scene + 320
    
    draw_sky(canvas, left_scene, top_scene, scene_right, scene_bottom)
    draw_clouds(canvas, left_scene + 450, top_scene + 50, scene_right - 50,
                scene_bottom - 300)
    draw_clouds(canvas, left_scene + 400, top_scene + 100, scene_right - 200,
                scene_bottom - 260)
    draw_clouds(canvas, left_scene + 550, top_scene + 120, scene_right - 60,
                scene_bottom - 260)
    draw_sun(canvas, left_scene + 100, top_scene + 50, scene_right - 600, scene_bottom
             - 350)
    draw_sun_ray(canvas, left_scene + 100, top_scene + 150, scene_right - 600,
                 scene_bottom - 450)
    draw_sun_ray(canvas, left_scene + 150, top_scene + 20, scene_right - 650,
                 scene_bottom - 320)
    draw_sun_ray(canvas, left_scene + 60, top_scene + 100, scene_right - 560,
                 scene_bottom - 400)
    draw_grass_blade(canvas, left_scene, top_scene +
                     500, scene_right, scene_bottom)
    draw_pinetree(canvas, tree_middle, tree_at_top, height_of_tree)

    
    #drawing a full house
    draw_house(canvas, left_scene + 200, top_scene + 300, scene_right - 500,
               scene_bottom - 100)
    draw_door(canvas, left_scene + 240, top_scene + 370, scene_right - 540,
              scene_bottom - 100)
    draw_window(canvas, left_scene + 220, top_scene + 320, scene_right - 560,
                scene_bottom - 160)
    draw_window(canvas, left_scene + 260, top_scene + 320, scene_right - 520,
                scene_bottom - 160)
    draw_roof(canvas, roof_top_y, roof_top_x, left_roof_y, left_roof_x,
              right_roof_y, right_roof_x)
    draw_roof(canvas, roof_top_y, roof_top_x, left_roof_y, left_roof_x - 70,
              right_roof_y, right_roof_x)

#drawing the sky
def draw_sky(canvas, sky_left, sky_top, sky_right, sky_bottom):
    canvas.create_rectangle(sky_left, sky_top, sky_right, sky_bottom,
                            fill="#6FBFE2", width=False)


def draw_pinetree(canvas, peak_x, peak_y, height):

    width_of_trunk = height / 8
   #building a trunk of a tree
    height_of_trunk = height / 3
    left_trunk = peak_x - width_of_trunk / 2
    right_trunk = peak_x + width_of_trunk / 2
    bottom_trunk = peak_y + height
    width_skirt = height / 2
    height_of_skirt = height - height_of_trunk
    left_skirt = peak_x - width_skirt / 2
    right_skirt = peak_x + width_skirt / 2
    bottom_skirt = peak_y + height_of_skirt

    # Draw the trunk of the pine tree.

    canvas.create_rectangle(left_trunk, bottom_skirt,
                            right_trunk, bottom_trunk,
                            outline="gray19", width=3, fill="tan2")
    # Draw the crown of the pine tree.
    canvas.create_polygon(peak_x, peak_y,
                          right_skirt, bottom_skirt,
                          left_skirt, bottom_skirt,
                          outline="gray19", width=1, fill="green")


def draw_grass_blade(canvas, left_scene, top_scene, scene_right, scene_bottom):
    for i in range(left_scene, scene_right, 10):
        canvas.create_rectangle(i, top_scene, i, randrange(401, 431), outline="green",
                                width=8)


def draw_sun(canvas, left_scene, top_scene, scene_right, scene_bottom):
    canvas.create_oval(left_scene, top_scene, scene_right, scene_bottom,
                       fill='yellow', outline="yellow")
    canvas.create_line(left_scene, top_scene, scene_right, scene_bottom,
                       fill='yellow', width='2')


def draw_sun_ray(canvas, left_scene, top_scene, scene_right, scene_bottom):
    canvas.create_line(left_scene, top_scene, scene_right, scene_bottom,
                       fill='yellow', width='2')

#draw clouds
def draw_clouds(canvas, cloud_left, cloud_top, cloud_right, cloud_bottom):
    canvas.create_oval(cloud_left, cloud_top, cloud_right, cloud_bottom,
                       fill="#f3f2ed", outline='#f3f2ed')


# Draw the house
def draw_house(canvas, left_scene, top_scene, scene_right, scene_bottom):
    canvas.create_rectangle(left_scene, top_scene, scene_right, scene_bottom,
                            fill="tan", outline='blue')


def draw_door(canvas, left_scene, top_scene, scene_right, scene_bottom):
    canvas.create_rectangle(left_scene, top_scene, scene_right, scene_bottom,
                            fill="yellow", outline='yellow')


def draw_window(canvas, left_scene, top_scene, scene_right, scene_bottom):
    canvas.create_rectangle(left_scene, top_scene, scene_right, scene_bottom,
                            fill="yellow", outline='red')


def draw_roof(canvas, roof_top_y, roof_top_x, left_roof_y, left_roof_x,
              right_roof_y, right_roof_x):
    canvas.create_polygon(roof_top_x, roof_top_y, left_roof_x, left_roof_y,
                          right_roof_x, right_roof_y, fill="brown", outline="yellow")


# Call the main function

main()
