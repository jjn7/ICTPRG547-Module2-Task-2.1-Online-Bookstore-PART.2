# Image validation utilities for book cover images
# Using Pillow library to check if image files are valid

from PIL import Image
import os

def validate_image(file_path):
    """
    Check if a file is a valid image using Pillow
    Returns (success, message) tuple
    """

    # Check if file path is provided
    if not file_path or file_path.strip() == "":
        return (True, "No image provided")  # Optional field, so this is okay

    # Check if file exists
    if not os.path.exists(file_path):
        return (False, f"Image file not found: {file_path}")

    # Try to open and validate the image using Pillow
    try:
        # Open the image file
        img = Image.open(file_path)

        # Verify it's actually an image by checking format
        if img.format not in ['JPEG', 'PNG', 'GIF', 'BMP']:
            return (False, f"Unsupported image format: {img.format}")

        # Check image dimensions are reasonable (not corrupted)
        width, height = img.size
        if width < 1 or height < 1:
            return (False, "Invalid image dimensions")

        # Close the image file
        img.close()

        # If we got here, the image is valid
        return (True, f"Valid {img.format} image ({width}x{height})")

    except Exception as e:
        # Pillow throws an exception if the file isn't a valid image
        return (False, f"Invalid image file: {str(e)}")


def get_image_info(file_path):
    """
    Get basic info about an image file
    Returns a dictionary with format, size, etc.
    """

    if not file_path or not os.path.exists(file_path):
        return None

    try:
        img = Image.open(file_path)

        info = {
            'format': img.format,
            'width': img.size[0],
            'height': img.size[1],
            'mode': img.mode  # RGB, RGBA, etc.
        }

        img.close()
        return info

    except Exception:
        return None
