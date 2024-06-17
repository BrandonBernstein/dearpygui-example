import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='Custom Title', width=800, height=600)

def bmi(height, weight):
    # Convert height from cm to meters
    height_in_meters = height / 100.0
    # Calculate BMI
    bmi_value = weight / (height_in_meters ** 2)
    return bmi_value

def submit_callback(sender, app_data, user_data):
    weight = dpg.get_value("weight_slider")
    height = dpg.get_value("height_slider")
    name = dpg.get_value("name_input")

    # Calculate BMI
    bmi_value = bmi(height, weight)

    # Display the result
    dpg.set_value("bmi_result", f"{name}, your BMI is: {bmi_value:.2f}")

def theme_callback(sender, app_data, user_data):
    if sender == "menu_default":
        dpg.bind_theme("default_theme")
        dpg.hide_item("hotdog")
    elif sender == "menu_hotdog":
        dpg.bind_theme("hotdog_theme")
        dpg.show_item("hotdog")


with dpg.texture_registry():
    width, height, channels, data = dpg.load_image("hotdog.png")
    dpg.add_static_texture(width=width, height=height, default_value=data, tag="hotdog_texture")


with dpg.theme(tag="hotdog_theme"):

    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (255, 255, 0))      # Yellow background
        dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 0, 0))            # Red text
        dpg.add_theme_color(dpg.mvThemeCol_Button, (255, 0, 0))          # Red button
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (200, 0, 0))   # Darker red on hover
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (150, 0, 0))    # Even darker red on active
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (255, 255, 255))     # White frame background
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, (255, 200, 200)) # Light red on hover
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive, (255, 150, 150)) # Darker light red on active
        dpg.add_theme_color(dpg.mvThemeCol_SliderGrab, (255, 0, 0))      # Red slider grab
        dpg.add_theme_color(dpg.mvThemeCol_SliderGrabActive, (200, 0, 0)) # Darker red on active grab


width, height, channels, data = dpg.load_image("hotdog.png")

with dpg.texture_registry():
    texture_id = dpg.add_static_texture(400, 600, data)

with dpg.window(tag="BMI Calculator", width=400, height=600):
    with dpg.menu_bar():
        with dpg.menu(label="Themes"):
            dpg.add_menu_item(label="Default", callback=theme_callback, tag="menu_default")
            dpg.add_menu_item(label="Hotdog Stand", callback=theme_callback, tag="menu_hotdog")

    dpg.add_text("Please enter your details")
    dpg.add_slider_float(label="Weight (kg)", default_value=70.0, max_value=150.0, min_value=30.0, tag="weight_slider")
    dpg.add_slider_int(label="Height (cm)", default_value=170, max_value=250, min_value=100, tag="height_slider")
    dpg.add_input_text(label="Name", tag="name_input")
    dpg.add_button(label="Submit", tag="submit_button", callback=submit_callback)
    dpg.add_text("", tag="bmi_result")

    with dpg.drawlist(300,400,tag = "hotdog"):

        dpg.draw_image("hotdog_texture", (0, 0), (300, 300), uv_min=(0, 0), uv_max=(1, 1))

    dpg.hide_item("hotdog")

with dpg.theme(tag="submit_button_text_theme"):
    with dpg.theme_component(dpg.mvButton):
        dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255))
dpg.bind_item_theme("submit_button", "submit_button_text_theme")

dpg.set_viewport_title("BMI Calculator")


# Setup Dear PyGui and show the viewport
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("BMI Calculator", True)
dpg.start_dearpygui()
dpg.destroy_context()