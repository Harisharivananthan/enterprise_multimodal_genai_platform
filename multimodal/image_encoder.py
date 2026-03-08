from sentence_transformers import SentenceTransformer
from PIL import Image

model = SentenceTransformer("clip-ViT-B-32")

def encode_image(image_path):
    image = Image.open(image_path).convert("RGB")
    vector = model.encode(image)
    return vector.tolist()