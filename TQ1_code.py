from PIL import Image
import numpy as np

## Optional statement to change working directory in case
## it's not same as the directory of this file
# import os
# os.chdir("path_to_working_directory")

# Through images 1 to 3
for i in range(1, 4):
    # Open and convert TIF image to NumPy array
    im_current= Image.open(f"TQ1/41077_120219_S000090_ch0{i}.tif")
    arr = np.array(im_current)
    # Save as CSV
    np.savetxt(f"image_{i}.csv", arr, delimiter=",")
