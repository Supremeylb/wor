# -*- coding:utf8 -*-
import os
import sys

import matplotlib
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from c_log import init_log

ani_plt = init_log("ani_plt")


class About_recursive(object):
    car = "BMW"

    def __init__(self):
        self.value = 3

    def trisum(self, n, csum=0):
        while True:
            if n == 0:
                return csum
            n, csum = n - 1, csum + n

    def bet(self, func):
        b = (lambda f: (lambda x: x(x))(lambda y:
                                        f(lambda *args: lambda: y(y)(*args))))(func)

        def wrapper(*args):
            out = b(*args)
            while callable(out):
                out = out()
            return out

        return wrapper


class Ani_plt(object):
    file_path = ""
    args = ["title", "xlabel", "ylabel", "fontsize"]
    NOT_LIST = []

    def __init__(self):
        self.all_args = {0: ("title", "Heroine"), 1: ("xlabel", "Year"), 2: ("fontsize", 20)}

    def set_args(self):
        print "\033[1;32m%s\033[0m" % ("%-4s%-30s%s" % ("ID", "Key", "Value"))
        ids = range(len(self.all_args))
        for i in ids:
            print "%-4s%-30s%s" % (i, self.all_args[i][1], self.all_args[i][2])

        select_id = raw_input("Please input the self.all_args ID which to be changed: ")
        try:
            select_id = int(select_id)
        except ValueError:
            print 'DoNOT test me!! I am NOT baby!'
            print 'I just need a number'
            os.abort()

        if select_id not in ids:
            print 'The number is out of my range!'
            os.abort()

        key = self.all_args[select_id][1]
        print "The old value of self.all_args(%s) is: %s." % (key, self.all_args[select_id][2])
        value = raw_input("Please input the new value: ")

    def get_data(self, file_path, rownum):
        docs = pd.read_excel(file_path, sheet_name="Online", skiprows=6)
        data = pd.DataFrame(docs.loc[rownum][2:]).astype(float)
        data.columns = {self.all_args["title"]}
        return data

    def get_ani(self, data, column):
        dose = pd.DataFrame(np.array(data[column]), np.array(data.index))
        dose.columns = {self.all_args["title"]}

    def create_plt(self, xmin, xmax, ymin, ymax):
        fig = plt.figure(figsize=[10, 6])
        plt.xlim(xmin, xmax)
        plt.ylim(ymin, ymax)
        plt.xlabel(self.all_args["xlabel"], fontsize=self.all_args["fontsize"])
        plt.ylabel(self.all_args["title"], fontsize=self.all_args["fontsize"])
        plt.title(self.all_args["title"], fontsize=self.all_args["fontsize"])
        return fig

    def animate(self, data, i):
        data_frame = data.iloc[:int(i + 1)]
        p = sns.lineplot(x=data_frame.index, y=data_frame[self.all_args["title"]], data=data_frame, color='r')
        p.tick_params(labelsize=17)
        plt.setp(p.lines, linewidth=7)

    def main(self, animate, title="My animation"):
        fig = self.create_plt()
        ani = matplotlib.animation.FuncAnimation(fig, animate, frames=20, repeat=True)
        Writer = animation.writers['ffmpeg']
        writer = Writer(fps=20, metadata=dict(artist='Me'), bitrate=1800)
        ani.save(title, writer=writer)

    def augment(self, xold, yold, numsteps):
        xnew, ynew = [], []
        for i in range(len(xold) - 1):
            difX = xold[i + 1] - xold[i]
            stepsX = difX / numsteps
            difY = yold[i + 1] - yold[i]
            stepsY = difY / numsteps
            for s in range(numsteps):
                xnew = np.append(xnew, xold[i] + s * stepsX)
                ynew = np.append(ynew, yold[i] + s * stepsY)
        return xnew, ynew

    def Gaosi(self):
        pass

    def add_background(self):
        sns.set(rc={'axes.facecolor': 'lightgrey', 'figure.facecolor': 'lightgrey',
                    'figure.edgecolor': 'black', 'axes.grid': False})


def arg_to_dict():
    """
    python program.py key1:val1 key2:val2 key3:val3
    dict = {'key3': 'val3', 'key2': 'val2', 'key1': 'val1'}
    :return:
    """
    dict = {}
    for arg in sys.argv[1:]:
        key, val = arg.split(':')[0], arg.split(':')[1]
        dict[key] = val
    return dict


def main():
    arg_dict = arg_to_dict()
    ani_plt = Ani_plt()
    if arg_dict == {}:
        pass
    else:
        func = arg_dict["func"]
        func_call = getattr(ani_plt, func, None)
        if func_call == "set_args":
            func_call()


if __name__ == "__main__":
    main()
