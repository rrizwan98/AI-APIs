import google.generativeai as genai
import google.ai.generativelanguage as glm
import io
import yaml
import typing
import urllib.request
import IPython.display
from PIL import Image as PIL_Image
from PIL import ImageOps as PIL_ImageOps
genai.configure(api_key='AIzaSyCGEUherYJud9qvqRZ9EWW_tvbOJla5mjM')
encoding = 'utf-8'

def load_configuration(file_path):
    """
    purpose:
    --------
        Loads the configuration from the specified YAML file.
    Parameters:
    -----------
        file_path (str): Path to the YAML file
    Returns:
    -------- 
        dict: Configuration dictionary
    """
    
    with open(file_path, 'r', encoding=encoding) as file:
        return yaml.safe_load(file)

# Load configuration
config = load_configuration('app_config.yaml')
# Extract values
prompt1:str = config.get('prompt1', '')
prompt2:str = config.get('prompt2', '')
prompt3:str = config.get('prompt3', '')

def display_image(image: PIL_Image.Image, max_width: int = 600, max_height: int = 350) -> None:
    if image.mode != "RGB":
        image = image.convert("RGB")
    image_width, image_height = image.size
    if max_width < image_width or max_height < image_height:
        image = PIL_ImageOps.contain(image, (max_width, max_height))
    display_image_compressed(image)

def display_image_compressed(pil_image: PIL_Image.Image) -> None:
    image_io = io.BytesIO()
    pil_image.save(image_io, "jpeg", quality=80, optimize=True)
    image_bytes = image_io.getvalue()
    ipython_image = IPython.display.Image(image_bytes)
    IPython.display.display(ipython_image)

import urllib.request

def load_image_from_url(image_url: str) -> PIL_Image.Image:
    # Additional headers to mimic a web browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    # Create a request with headers
    request = urllib.request.Request(image_url, headers=headers)
    # Open URL and read image bytes
    with urllib.request.urlopen(request) as response:
        image_bytes = response.read()
    # Create a PIL Image object from the image bytes
    image = PIL_Image.open(io.BytesIO(image_bytes))
    return image

def count_dogs_in_image(image_url: str, prompt1: str = prompt1, prompt2: str = prompt2, prompt3: str = prompt3) -> None:
    # Load image from URL
    image = load_image_from_url(image_url)
    contents = [prompt1, prompt2, image, prompt3]
    # Generate content using the multimodal model
    multimodal_model = genai.GenerativeModel("gemini-pro-vision")
    responses = multimodal_model.generate_content(contents, stream=True)
    responses.resolve()
    # Display prompt and responses
    print("-------Prompt--------")
    print(contents)
    # display_image(image)

    print("\n-------Response--------")
    for response in responses:
        print(response.text)
    return responses.text

# Count dogs in an image
# count_dogs_in_image('https://images.pexels.com/photos/10824421/pexels-photo-10824421.jpeg', prompt1, prompt2, prompt3)
# count_dogs_in_image('https://images.pexels.com/photos/18639011/pexels-photo-18639011/free-photo-of-men-with-dogs-walking-on-cicek-pasaji-in-istanbul.jpeg', prompt1, prompt2, prompt3)
