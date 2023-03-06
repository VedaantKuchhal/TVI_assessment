from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

## Optional statement to change working directory in case
## it's not same as the directory of this file
# import os
# os.chdir("OneDrive - Olin College of Engineering/Desktop/Other College Stuff/PGPStuff/TVI_Intern_Technical_Questions-master/")

# Open ground truth binary mask and convert to array
im_bmask= Image.open(f"TQ2/binary_41077_120219_S000090_L01.tif")
arr_bmask = np.array(im_bmask)

# Open the clearest image (..._ch03) and convert to array
im_real= Image.open(f"TQ1/41077_120219_S000090_ch03.tif")
arr_real = np.array(im_real)

# Flatten to 1-D array, convert to binary mask
r_real = arr_real.reshape(arr_real.shape[0]*arr_real.shape[1])
for i in range(r_real.shape[0]):
    # Threshold value of 3500 was narrowed down through
    # manual testing to give the most accurate results
    if r_real[i] > 3500:
        r_real[i] = 1
    else:
        r_real[i] = 0

# Convert back to 2-D array
arr_real = r_real.reshape(arr_real.shape[0],arr_real.shape[1])

# Calculate accuracy
overlap = np.bitwise_xor(arr_bmask, arr_real)
accuracy = 1 - (np.sum(overlap)/arr_real.size)
print(f"Percentage of pixels correctly segmented compared to ground truth: {str(np.round(accuracy*100, 2))}%")

# Display binary mask
plt.imshow(arr_real, cmap="gray")
plt.show()

