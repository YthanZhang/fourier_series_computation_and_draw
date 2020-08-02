import scipy.integrate as integrate
import scipy


def complex_quad(func: callable, a: float, b: float):
    real_integrate = integrate.quad(lambda x: scipy.real(func(x)), a, b, limit=500)
    imag_integrate = integrate.quad(lambda x: scipy.imag(func(x)), a, b, limit=500)
    return complex(real_integrate[0], imag_integrate[0]), (real_integrate[1], imag_integrate[1])


def get_fourier_series(func_points: list, series_depth: int) -> list:
    c_n = []
    step_size = 1 / len(func_points)
    for n in range(-series_depth, series_depth + 1, 1):
        ray_sum = 0
        for step, ele in enumerate(func_points):
            ray_sum += ele * scipy.exp(-n * 2 * scipy.pi * 1j * step * step_size) * step_size
        c_n.append(ray_sum)
        print("c_" + str(n) + " calculation complete.")
    return c_n


def get_fourier_series_sin(series_depth: int) -> list:
    c_n = []
    for n in range(-series_depth, series_depth + 1, 1):
        def get_fourier(x):
            return scipy.sin(x) * scipy.exp(-n * 2 * scipy.pi * complex(0, 1) * x)
        c_n.append(complex_quad(get_fourier, 0, 1)[0])
        print("c_" + str(n))
    return c_n


def get_fourier_series_square(series_depth: int) -> list:
    c_n = []
    for n in range(-series_depth, series_depth + 1, 1):
        if n % 2 and n > 0:
            c_n.append(2 / (n * scipy.pi * 1j))
        else:
            c_n.append(0 + 0j)
    return c_n


def draw_fourier_series(c_n: list, resolution: int, period_count: int = 1):
    rslt = []
    for s in range(resolution * period_count):
        t = s / resolution
        fourier_sum = complex(0, 0)
        for i, n in enumerate(range(0 - int(len(c_n) / 2), len(c_n) - int(len(c_n) / 2))):
            fourier_sum += c_n[i] * scipy.exp(n * 2 * scipy.pi * complex(0, 1) * t)
        rslt.append(fourier_sum)
        print("draw step " + str(s) + " complete.")
    return rslt


if __name__ == "__main__":
    import plotting
    c1_n = get_fourier_series_square(20)
    r1 = draw_fourier_series(c1_n, 10000)
    print("r1 done")
    plotting.plot_complex(r1)

    c2_n = get_fourier_series(r1, 20)
    print("c_n calculation done.")
    r2 = draw_fourier_series(c2_n, 10000, 2)
    print("rslt drawing completed.")
    plotting.plot_complex(r2)
    plotting.plt.figure()
    plotting.plt.plot(r2)

