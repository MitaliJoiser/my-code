import os
from psd_tools import PSDImage
from PIL import Image

def print_layer_info(layer, indent=0):
    print("  " * indent + f"Layer Name: {layer.name}")
    
    if layer.bbox is not None:
        width, height = layer.bbox[2] - layer.bbox[0], layer.bbox[3] - layer.bbox[1]
        print("  " * indent + f"Dimensions: {width} x {height}")

    if hasattr(layer, 'text_data') and layer.text_data is not None:
        print("  " * indent + f"Text Content: {layer.text_data.text}")

    if layer.is_group():
        for child in layer:
            print_layer_info(child, indent + 1)

def extract_image_layers(layer, output_folder="extracted_images"):
    if not layer.is_group() and layer.visible:
        pil_image = layer.topil()
        os.makedirs(output_folder, exist_ok=True)
        pil_image.save(f"{output_folder}/{layer.name}.png")

def read_psd_file(file_path):
    psd = PSDImage.open(file_path)
    try:
        print("Layers in PSD file:")
        for layer in psd:
            print_layer_info(layer)

        # Create a folder for extracted images (if not exists)
        output_folder = "extracted_images"
        for layer in psd:
            extract_image_layers(layer, output_folder)
    finally:
        # You can optionally close the file, but it's not strictly necessary
        pass

if __name__ == "__main__":
    # path to your PSD file
    psd_file_path = 'psdfile.psd'
    read_psd_file(psd_file_path)
