from PIL import Image
import os

def resize_image(input_image_path, output_folder, sizes):
    # Open the input image
    image = Image.open(input_image_path)

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    resized_images = {}

    # Loop through the specified sizes and resize the image
    for size in sizes:
        new_image = image.resize((size, size), Image.LANCZOS)
        new_image_path = os.path.join(output_folder, f"{size}x{size}_{os.path.basename(input_image_path)}")
        new_image.save(new_image_path)

        resized_images[size] = new_image_path

    return resized_images

if __name__ == "__main__":
    input_image = os.path.join(os.getcwd(), "input.png")  # Replace with your input image path
    output_folder = os.path.join(os.getcwd(), "resized_images")
    sizes = [40, 60,58,87,76,114,80,120,180,128,192,136,1024,152,167]  # Add or remove sizes as needed

    resized_images = resize_image(input_image, output_folder, sizes)
    print("Resized images:", resized_images)
