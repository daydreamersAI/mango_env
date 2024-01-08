from PIL import Image, ImageGrab, ImageDraw
from pynput.mouse import Controller
import time

def capture_screen_with_cursor(output_path):
    # Capture the entire screen
    screenshot = ImageGrab.grab()

    # Get the current mouse cursor position
    mouse = Controller()
    cursor_position = mouse.position

    # Create a blank image for the cursor
    cursor_image = Image.new('RGBA', (32, 32), (0, 0, 0, 0))

    # Draw a simple cursor on the blank image
    draw = ImageDraw.Draw(cursor_image)
    draw.line([(0, 16), (32, 16)], fill=(255, 0, 0, 255), width=2)
    draw.line([(16, 0), (16, 32)], fill=(255, 0, 0, 255), width=2)

    # Paste the cursor image onto the screenshot at the cursor position
    screenshot.paste(cursor_image, cursor_position, cursor_image)

    # Save the screenshot with the cursor
    screenshot.save(output_path, "PNG")

if __name__ == "__main__":
    output_path = "screenshot_with_cursor.png"  # Replace with your desired output path and filename
    capture_screen_with_cursor(output_path)
