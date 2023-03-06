## TQ2
Q: Briefly describe any distinct visual properties of the objects segmented by the ground truth mask.

A: The objects appear to be relatively round in shape, relatively small and in multiple clusters that vary in size but not by a huge amount. Individual objects don't appear to be spatially related or interconnected in an easily discernable way.

Q: How could you use these characteristics to generate your own segmentation mask of these objects?

A: Since the objects are independent, don't have straight edges, and the mask is a binary segmentation, I would do a simple threshold segmentation here with a single global threshold.

## TQ3
Q1: What modifications would you make to your segmentation method in TQ2 to preserve accuracy and efficiency on this larger data?

A1: I would probably change the segmentation method entirely, since I would have a large set of images to train a more complex model on.
    
    
Q2: Are there any potential limitations or corner cases that could produce poor results with this segmentation method?

A2: A clear corner case that the current method struggles to deal with is the presence of light patches (in the TQ1 images this can be seen as a along a line on the right) that will still be detected by the mask even though it is not part of the ground truth. The current method also fails to capture the outline of objects accurately so that would need to be worked on.

