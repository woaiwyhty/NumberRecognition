from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from Train import classify
from Train import initFeatureSet

def recognize(filename):
    img = np.array(Image.open(filename))
    black = np.array([0, 0, 0]);
    result = [];

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if (img[i][j] == black).all():
                result.append(1);
            else:
                result.append(0);

    zeroOneArray = np.array(result);
    featureSet, labels = initFeatureSet();
    mK = 3;

    return classify(zeroOneArray, featureSet, labels, mK);
