import svg.path as svg_path
# noinspection PyUnresolvedReferences
from xml.dom import minidom


def get_points_from_str(string: str, resolution: int = 10000):
    path = svg_path.parse_path(string)
    return [path.point(i/resolution) for i in range(resolution)]


def scale_points(points: list, scale: tuple):
    pr, pj = [], []
    for ele in points:
        pr.append(ele.real * scale[0])
        pj.append(ele.imag * scale[1])

    return [complex(r, j) for r, j in zip(pr, pj)]


def get_path_str(directory: str):
    return minidom.parse(directory).getElementsByTagName("path")[0].attributes["d"].value


