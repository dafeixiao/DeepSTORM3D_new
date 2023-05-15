import numpy as np
import matplotlib.pyplot as plt


def scatter_plot_matrix3d(mat3d):
    """
    scatter plot of a 3D matrix
    mat3d: ndarray, rank3
    pass test?
    """
    z_size = mat3d.shape[0]
    x_size = mat3d.shape[1]
    y_size = mat3d.shape[2]
    xg, yg, zg = np.meshgrid(np.linspace(0, x_size, x_size), np.linspace(0, y_size, y_size),
                             np.linspace(0, z_size, z_size), indexing='xy')

    fig = plt.figure(123)
    ax = fig.add_subplot(projection='3d')
    ax.scatter(xg.flatten(), yg.flatten(), zg.flatten(), c=mat3d.flatten())
    plt.show()


def image_overlay_rendering(im1, im2, threshold=0.1):
    """
    im1: the base image, ndarray, rank2, project01, grayscale
    im2: the overlay image, ndarray, rank2, project01
    threshold: threshold for im2, [0, 1], larger threshold includes more of im2
    """
    fig = plt.figure(102)
    im1 = (im1 - im1.min()) / (im1.max() - im1.min())
    im2 = (im2 - im2.min()) / (im2.max() - im2.min())

    im_base = np.stack((im1,) * 3, axis=-1)
    im_color = im_base.copy()
    im_color[:, :, [0, 2]] = 0  # get the color

    mask = im2 > threshold
    mask = np.expand_dims(mask, axis=2)

    im_synthetic = im_base * (1 - mask) + im_color * mask
    plt.imshow(im_synthetic)
    plt.draw()
    plt.pause(0.05)




