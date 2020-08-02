if __name__ == "__main__":
    import plotting
    import fourier
    import read_svg

    r1 = read_svg.get_points_from_str(read_svg.get_path_str("svgs/gelbe_Note.svg"))
    r1 = read_svg.scale_points(r1, (1, -1))
    print("r1 done")
    plotting.plot_complex(r1)

    c2_n = fourier.get_fourier_series(r1, 500)
    print("c_n calculation done.")
    r2 = fourier.draw_fourier_series(c2_n, 10000, 1)
    print("rslt drawing completed.")
    plotting.plot_complex(r2)
    plotting.plot_complex3d(r2)
    plotting.plot(r2)

    plotting.plt.show()
