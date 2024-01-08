from PIL import Image, ImageDraw
from screeninfo import get_monitors

def get_screen_resolution():
    monitors = get_monitors()
    resolution = []
    for monitor in monitors:
        print("Monitor {} - Resolution: {}x{}".format(monitor.name, monitor.width, monitor.height))
        resolution.append(f'{monitor.width}x{monitor.height}')
    return resolution

def add_grid(image_path, n, output_path):
    # Open the image
    image = Image.open(image_path)

    # Get image dimensions
    width, height = image.size

    # Calculate the size of each grid cell
    cell_width = width / n
    cell_height = height / n

    # Create a drawing object
    draw = ImageDraw.Draw(image)

    # Add grid lines
    for i in range(1, n):
        # Vertical grid lines
        draw.line([(i * cell_width, 0), (i * cell_width, height)], fill="red", width=1)

        # Horizontal grid lines
        draw.line([(0, i * cell_height), (width, i * cell_height)], fill="red", width=1)

    # Save the image
    image.save(output_path, format='JPEG')

if __name__ == "__main__":
    resolutions = get_screen_resolution()
    
    # Assuming you want to use the first resolution from the list
    image_path = "screenshots\screenshot.jpg"  # Replace with the path to your image
    grid_size = 5  # Change this to the desired grid size (nxn)
    output_path = f"screenshots\screenshot_{resolutions[0]}.jpg"
    
    add_grid(image_path, grid_size, output_path)
