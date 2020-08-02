if __name__ == "__main__":
    import plotting
    import fourier

    c1_n = fourier.get_fourier_series_square(20)
    r1 = fourier.draw_fourier_series(c1_n, 10000)
    print("r1 done")
    plotting.plot_complex(r1)

    c2_n = fourier.get_fourier_series(r1, 20)
    print("c_n calculation done.")
    r2 = fourier.draw_fourier_series(c2_n, 10000, 2)
    print("rslt drawing completed.")
    plotting.plot_complex(r2)
    plotting.plot_complex3d(r2)
    plotting.plot(r2)
