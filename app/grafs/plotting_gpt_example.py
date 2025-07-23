import matplotlib.pyplot as plt
import io

def plot_elevation(elevations):
    fig, ax = plt.subplots()
    ax.plot(elevations)
    ax.set_title("Profil wysokości")
    ax.set_xlabel("Punkt")
    ax.set_ylabel("Wysokość [m]")

    buf = io.BytesIO()
    fig.savefig(buf, format="jpg")
    buf.seek(0)
    return fig, buf


def plot_route(lats, lons):
    fig, ax = plt.subplots()
    ax.plot(lons, lats, marker='o', markersize=2, linewidth=1)
    ax.set_title("Trasa GPS")
    ax.set_xlabel("Długość geograficzna")
    ax.set_ylabel("Szerokość geograficzna")

    buf = io.BytesIO()
    fig.savefig(buf, format="jpg")
    buf.seek(0)
    return fig, buf
