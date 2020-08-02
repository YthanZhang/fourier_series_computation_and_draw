import matplotlib.pyplot as plt


def draw(x: list, y: list) -> None:
    plt.plot(x, y)
    plt.draw()


def plot_complex(numbers: list, xlim=(-2, 2), ylim=(-2, 2)):
    real = [number.real for number in numbers]
    imag = [number.imag for number in numbers]

    f = plt.figure()
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
