import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import earthpy.plot as ep
from scipy.io import loadmat
from PIL import Image

# Load data
data = loadmat('Model/Salinas_corrected.mat')['salinas_corrected']
gt = loadmat('Model/Salinas_gt.mat')['salinas_gt']

# Move axis for RGB composite image
mdata = np.moveaxis(data, -1, 0)

def plot_data(data, title="Image"):
    fig, ax = plt.subplots(figsize=(12, 10))
    ax.imshow(data, cmap='nipy_spectral')
    ax.set_title(title)
    ax.axis('off')
    st.pyplot(fig)

def plot_rgb_image(mdata):
    fig, ax = plt.subplots(figsize=(15, 15))
    ep.plot_rgb(mdata, (29, 19, 9), ax=ax)
    st.pyplot(fig)

def main():
    st.title("Satellite Image Processing")
    
    menu = ["Home", "Image Prediction"]
    choice = st.sidebar.selectbox("Select Module", menu)
    
    if choice == "Home":
         # Display banner image
        banner_image = Image.open("banner.jpeg")  # Replace with your image path
        st.image(banner_image, use_column_width=True)
        st.subheader("Welcome to the Satellite Image Analysis App")
        st.write("This app processes and visualizes hyperspectral images.")
    
    elif choice == "Image Prediction":
        st.subheader("Image Visualization and Prediction")
        
        
        band_index = st.slider("Select Band Index", 0, 102, 29)
        
        if st.button("Show Selected Band Image"):
            fig, ax = plt.subplots(figsize=(12, 10))
            ax.imshow(data[:, :, band_index], cmap='nipy_spectral')
            ax.set_title(f"Band - {band_index}")
            ax.axis('off')
            st.pyplot(fig)
        
        if st.button("Show RGB Composite Image"):
            plot_rgb_image(mdata)

        if st.button("Show Ground Truth Data"):
            plot_data(gt, title="Ground Truth Data")
    
if __name__ == '__main__':
    main()