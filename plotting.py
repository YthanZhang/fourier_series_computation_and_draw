import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d


def plot(numbers) -> None:
    plt.figure()
    plt.plot(numbers)


def plot_complex3d(numbers: list):
    real = [number.real for number in numbers]
    imag = [number.imag for number in numbers]
    time = [n for n in range(len(numbers))]

    plt.figure()
    f = plt.gca(projection="3d")
    f.plot(time, real, imag)


def plot_complex(numbers: list, xlim=(-2, 2), ylim=(-2, 2)):
    real = [number.real for number in numbers]
    imag = [number.imag for number in numbers]

    plt.figure()
    plt.plot(real, imag)
    plt.xlim(xlim)
    plt.ylim(ylim)


def scatter_complex(numbers: list, xlim=(-2, 2), ylim=(-2, 2)):
    real = [number.real for number in numbers]
    imag = [number.imag for number in numbers]

    f = plt.figure()
    plt.scatter(real, imag)
    plt.xlim(xlim)
    plt.ylim(ylim)
