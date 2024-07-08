import tkinter as tk
from tkinter import messagebox, Toplevel, Label
from PIL import Image, ImageTk
from wther import get_weather

def fetch_weather():
    city = city_entry.get()
    result, weather_description = get_weather(city)
    show_weather_info(result, weather_description)

def show_weather_info(result, weather_description):
    # Create a new top-level window
    weather_window = Toplevel(root)
    weather_window.title("Weather Info")
    weather_window.geometry("400x400")
    weather_window.configure(background="lightblue")

    # Display the weather information
    info_label = Label(weather_window, text=result, bg="lightblue", font=("Helvetica", 12))
    info_label.pack(pady=10)

    # Determine the image based on weather description
    if "clear" in weather_description.lower():
        image_path = "sunny.png"
    elif "cloud" in weather_description.lower():
        image_path = "cloudy.png"
    elif "rain" in weather_description.lower():
        image_path = "rainy.png"
    else:
        image_path = "default.png"

    # Load and display the image
    weather_image = Image.open(image_path)
    weather_image = weather_image.resize((200, 200), Image.ADAPTIVE)
    photo = ImageTk.PhotoImage(weather_image)
    image_label = Label(weather_window, image=photo, bg="lightblue")
    image_label.image = photo
    image_label.pack(pady=20)

    # Animate the image (simple opacity change)
    def animate_image():
        current_opacity = weather_image.info.get("transparency", 255)
        new_opacity = 128 if current_opacity == 255 else 255
        weather_image.putalpha(new_opacity)
        photo = ImageTk.PhotoImage(weather_image)
        image_label.config(image=photo)
        image_label.image = photo
        weather_window.after(500, animate_image)
    
    animate_image()

# Main window setup
root = tk.Tk()
root.title("Weather App")
root.geometry("500x400")
root.configure(background="lightblue")

# Fonts
title_font = ("Helvetica", 18, "bold")
label_font = ("Helvetica", 12)
entry_font = ("Helvetica", 12)

# Title label
title_label = tk.Label(root, text="Weather App", font=title_font, bg="lightblue")
title_label.pack(pady=20)

# City input
city_label = tk.Label(root, text="City Name", font=label_font, bg="lightblue")
city_label.pack(pady=10)
city_entry = tk.Entry(root, font=entry_font, justify='center')
city_entry.pack(pady=5)

# Get Weather button
get_weather_button = tk.Button(root, text="Get Weather", command=fetch_weather, font=label_font, bg="white", width=20)
get_weather_button.pack(pady=20)

# Start button animation
def animate_button():
    current_color = get_weather_button.cget("background")
    new_color = "lightblue" if current_color == "white" else "white"
    get_weather_button.config(background=new_color)
    root.after(500, animate_button)

animate_button()

# Run the application
root.mainloop()
