import io
from google.cloud import vision
from PIL import Image

# Set up Google Cloud Vision API client
client = vision.ImageAnnotatorClient()

# Function to analyze image and separate text and visual elements
def analyze_image(image_path):
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    # Perform OCR to extract text from the image
    response = client.text_detection(image=image)
    texts = response.text_annotations

    if texts:
        # Extracted text
        extracted_text = texts[0].description
        print("Extracted Text:")
        print(extracted_text)

        # Perform basic image segmentation (placeholder)
        segmented_images = segment_image(image_path)

        # Bonus: Save segmented images and generate HTML output (optional)

    else:
        print("No text found in the image")

# Function for basic image segmentation
def segment_image(image_path):
    with Image.open(image_path) as img:
        # Implement basic segmentation techniques here
        # For example, you can use thresholding, contour detection, or edge detection
        # to isolate individual visual elements

        # Placeholder - Replace with actual segmentation code
        segmented_images = [img]

        return segmented_images

# Main function
def main(image_path):
    # Analyze the image
    analyze_image(image_path)

# Example usage
if __name__ == "__main__":
    image_path = "path/to/your/image.jpg"
    main(image_path)
