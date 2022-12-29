import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from scipy import stats
def amit(fourier_data, theoretical_stdev=None):

    fig, ax = plt.subplots(figsize=(16, 10))
    ax.set(xlabel="SFT value", ylabel="PDF", yscale="log")


    ax.hist(
        fourier_data.imag.ravel(),
        density=True,
        bins="auto",
        histtype="step",
        lw=2,
        label="Imaginary part",
    )

    if theoretical_stdev is not None:
        x = np.linspace(-4 * theoretical_stdev, 4 * theoretical_stdev, 1000)
        y = stats.norm(scale=theoretical_stdev).pdf(x)
        print(y)


    ax.legend()

