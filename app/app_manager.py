from pathlib import Path
import data_readers.gpx_reader as gpx_reader
from heart_zones.calc_heart_zones import HeartZones
from grafs.line_chart import LineChart
from grafs.bar_chart import Bar


def run_app(file, title):
    hr = gpx_reader.read_hr_from_gpx(file)

    zones = HeartZones(hr)

    hr_name = 'HR ' + title
    hr_chart = LineChart(hr_name)
    hr_chart.plot(hr)
    buf1 = hr_chart.save_to_buffer()
    fig1 = hr_chart.fig


    bar_name = title
    bar = Bar(bar_name)
    bar.plot(zones.get_results())
    buf2 = bar.save_to_buffer()
    fig2 = bar.fig
    return fig1, buf1, fig2, buf2
