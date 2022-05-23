import mss
import numpy as np
from PIL import Image
import os

from skimage.filters import threshold_otsu


ITEMS_IMAGES_PATH = os.path.join(os.getcwd(), 'Images', 'Items', '')

__all__ = ['item_recognizer']

def _screen_acquisition():

    # Acquire all screen
    with mss.mss() as sct:

        # 1 monitor FullHD
        monitor = {"top": 0, "left": 0, "width": 1920, "height": 1080}

        screen_array = np.array(sct.grab(monitor))
        screen_array = Image.fromarray(screen_array).convert('L')
        screen_array = np.array(screen_array)

    return screen_array


def _get_hold_items(screen: np.array) -> list:
    """
    Description
    -----------
    Subdivide the portion of the screen into 6 bunches, where
    items are hold in game by the champion.

    Parameters
    ----------
    screen : numpy.array
        Array containing the grayscale values of the whole screen.

    Return
    ------
    list : List of numpy.array objects relative to the items spots in game.

    """

    x_step = [49 * i for i in range(0, 3)]  # Three item columns
    y_step = [47 * i for i in range(0, 2)]  # Two item rows

    # At the moment, all the position values are found empirically
    return [screen[947 + y:987 + y, 1131 + x:1171 + x] for y in y_step for x in x_step]


def _image_comparison(img_items_list : list) -> list:
    """
    Description
    -----------
    Perform an image recognition and get the name of the object , if it exists.

    Parameters
    ----------
    img_items_list : list
        List containing the array bunches obtained from '_get_hold_items()' function.

    Return
    ------
    list : List with the items names found, if they exist.

    """

    result = []

    # Must use img_names because some files are not recognized, so the position shifts
    img_names = []

    # .png files in dir
    images = [img for img in os.listdir(ITEMS_IMAGES_PATH) if img.endswith('.png')]

    try:

        # Compare each bunch ...
        for img_array in img_items_list:

            # For every image keep track of the score
            scores = []

            # Threshold (Otsu). Remove borders
            img_array = np.where(img_array >= 0.9*threshold_otsu(img_array), 255, 0)[3:-3, 3:-3]

            # ... with every default image
            for img_name in images:

                # Convert to numpy grayscale
                test = np.array(Image.open(os.path.join(ITEMS_IMAGES_PATH, img_name)).convert("L"))

                if test.size == 1600:

                    # Threshold (Otsu) and Get number of equal pixels. Remove borders
                    test = np.where(test >= 0.9*threshold_otsu(test), 255, 0)[3:-3, 3:-3]

                    missed = np.abs(test - img_array)
                    score = np.count_nonzero(missed) / img_array.size
                    scores.append(score)
                    img_names.append(img_name)

            # Lower threshold => more similar (it's a difference)
            if np.min(scores) < 0.3:

                # If two images have the same score we take the first one. Is it a problem? yes.
                # Can this happen? don't know, I guess and hope not, it's not likely for sure.
                img_position = np.where(scores == np.min(scores))[0][0]
                result.append(img_names[img_position][:-4])
    except:
        pass

    if len(result) == 0:
        result = [None] * 6

    return result


def item_recognizer() -> list:
    """
    Description
    -----------
    Get the name of each object hold by the champion in game,
    by confronting the images with the default ones.

    Return
    ------
    list : List of strings with the items names.

    """

    # Analyze bunches: get screenshot, divide it in bunches and perform the comparison.
    result = np.array(_image_comparison(_get_hold_items(_screen_acquisition())), dtype=object)

    if np.any(result):

        return result[result.nonzero()[0]]

    else:
        print("- No Items found.")
        return [None]*6

