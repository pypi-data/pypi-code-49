import arcade

# Open the window. Set the window title and dimensions (width and height)
arcade.open_window(600, 600, "Drawing Primitives Example")

# Set the background color to white
# For a list of named colors see
# http://arcade.academy/arcade.color.html
# Colors can also be specified in (red, green, blue) format and
# (red, green, blue, alpha) format.
arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()

cx = 200
cy = 200

ox = 210
oy = 200

arcade.draw_point(cx, cy, arcade.color.RED, 5)

for angle in range(90):
    x, y = arcade.rotate_point(ox, oy, cx, cy, angle)
    arcade.draw_point(x, y, arcade.color.BLACK, 5)

arcade.draw_point(ox, oy, arcade.color.BLUE, 5)


arcade.finish_render()

arcade.run()
