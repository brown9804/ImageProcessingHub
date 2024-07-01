import cv2
import numpy as np
from PIL import Image
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def vectorize_image(image_path, output_path, num_colors=64):
    img = cv2.imread(image_path)
    pixels = img.reshape(-1, 3)
    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(pixels)
    quantized_pixels = kmeans.cluster_centers_[kmeans.labels_]
    quantized_img = quantized_pixels.reshape(img.shape)
    cv2.imwrite(output_path, quantized_img)
    img_rgb = cv2.cvtColor(quantized_img.astype(np.uint8), cv2.COLOR_BGR2RGB)
    fig, ax = plt.subplots()
    ax.imshow(img_rgb)
    ax.axis('off')
    fig.savefig(output_path.replace('.png', '.svg'), format='svg')
    fig.savefig(output_path.replace('.png', '.pdf'), format='pdf')

input_image_path = './input.png'
output_image_path = './vector_output.png'
vectorize_image(input_image_path, output_image_path)

