import matplotlib.pyplot as plt
from pathlib import Path
import io


class Bar:
    colors = {'s1': None,
              's2': None,
              's3': None,
              's4': None,
              's5': None,
              'LT': 'red'}
    
    def __init__(self, title: str):
         self.fig, self.ax = plt.subplots()
         self.title = title

    def show(self):
        self.fig.show()
        plt.show(block=True)

    def save_to_file(self, file_path):
        self.fig.savefig(file_path)

    def save_to_buffer(self):
        buffer = io.BytesIO()
        self.fig.savefig(buffer, format='jpg')
        buffer.seek(0)
        return buffer

    def plot(self, Y):
        self._validate(Y)

        y_time_dec = [i / 60 for i in Y]
        X = self.colors.keys()
        bars = self.ax.bar(X, y_time_dec)

        self.ax.set_title(self.title)
        self._set_bar_colors(bars, X)
        self._set_Ymax_scale_value(y_time_dec)
        self._add_labels_time_above_bars(X, Y)
        self._setup_legend()        

    def _validate(self, Y):
        x_len = len(self.colors)
        y_len = len(Y)
        if y_len != x_len:
            raise ValueError(f'Wrong number of zones - X len: {x_len}, Y len: {y_len}')
    
    def _set_bar_colors(self, bars, X):
        length = len(X)
        for i, color in enumerate(self.colors.values()):
            if i >= length:
                break
            if isinstance(color, str) and len(color):
                bars[i].set_color(color)

    def _set_Ymax_scale_value(self, y_time_dec):
        y_max = self.__calc_max_scale(y_time_dec)
        self.ax.set_ylim([0, y_max])

    @staticmethod
    def __calc_max_scale(Y):
        max_scale_value  = (int(max(Y) / 5) + 1) * 5
        if max_scale_value < 35:
            max_scale_value = 35
        return max_scale_value

    def _add_labels_time_above_bars(self, x,y):
        for i in range(len(x)):
            min = str(int(y[i] / 60))
            sec = str(y[i] % 60)
            if len(sec) == 1:
                sec = '0' + sec
            time_str = min + ':' + sec
            self.ax.text(i, (y[i] / 60) + 0.5, time_str, ha='center')

    def _setup_legend(self):
        legend = {'s1-s5 - czas w strefach wysiłku': None, 'LT - czas powyżej progu mleczanowego': 'red'}
        labels = list(legend.keys())
        handles = [plt.Rectangle((0, 0), 1, 1, color=legend[label]) for label in labels]
        self.ax.legend(handles, labels, fontsize=7)
