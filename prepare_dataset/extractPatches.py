
def extractPatches(image,patchSize,step):
    (patchW, patchH) = patchSize
    (stepW,stepH) = step
    (h,w) = image.shape[:2]
    patches = []
    startY = 0
    while(startY<h):
        startX = 0
        while(startX<w):
            patches.append(image[startY:startY+patchH,startX:startX+patchW])
            startX += stepW
        startY += stepH
    return patches
















