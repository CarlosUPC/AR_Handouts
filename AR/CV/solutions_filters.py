def boxFilter(img):

    # normalize
    img = img / 255.0

    # kernel
    ksize = 11
    krn = np.zeros((ksize, ksize))
    krn[:, :] = 1.0 / (ksize * ksize)

    # filter
    filtered = convolve(img, krn)

    return filtered


    def convolve(img, krn):

        ksize, _ = krn.shape
        krad = int(ksize/2)

        height, width, depth = img.shape
        framed = np.ones((height + 2*krad, width + 2*krad, depth))
        framed[krad:-krad, krad:-krad] = img

        # filter

        filtered = np.zeros(img.shape)
        for i in range(0, height):
            for j in range(0, width):
                filtered[i, j] = (framed[i:i+ksize, j:j+ksize] * krn[:, :, np.newaxis]).sum(axis=(0,1))

        return filtered