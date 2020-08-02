if __name__ == "__main__":
    import plotting
    import fourier
    import read_svg

    r1 = read_svg.get_points_from_str(read_svg.get_path_str("svgs/Pi-symbol.svg"))
    r1 = read_svg.scale_points(r1, (1, -1))
    plotting.plot_complex(r1)

    c_n = fourier.get_fourier_series(r1, 200)
    r2 = fourier.draw_fourier_series(c_n, 10000)

    plotting.plot_complex3d(r2)
    plotting.plot_complex(r2)
    plotting.plot(r2)

    plotting.plt.show()
