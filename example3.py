#! /usr/bin/env python3
import argparse
from ctypes import cdll, c_double
import numpy as np
import matplotlib.pyplot as plt

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--rootfile', required=True)
    parser.add_argument('--plot-name', required=True)
    parser.add_argument('--outfile', required=True)
    parser.add_argument('--nxbins', default=100)
    parser.add_argument('--nybins', default=100)
    return parser.parse_args()

def get_2d_hist(root_file_name,hist_name,nx,ny):
    lib = cdll.LoadLibrary('libexample3.so') 
    n = (nx+2)*(ny+2)
    double_array = (c_double*n)(*([0.]*n))
    lib.get_2d_hist_content(root_file_name.encode('ascii'), 
            hist_name.encode('ascii'), n, double_array)
    array = np.array([v for v in double_array])
    array = array.reshape(nx+2, ny+2)
    return array[1:-1, 1:-1]

def plot(hist, outfile):
    fig = plt.figure()
    ax = fig.add_axes([0.17, 0.15, 0.77, 0.75])
    cmap = plt.get_cmap('jet')
    cmap.set_over('white')
    ax.imshow(hist, origin='lower', aspect='auto', vmin=32, vmax=40, cmap=cmap,
            interpolation='nearest')
    print(outfile)
    fig.savefig(outfile)

def main(rootfile, plot_name, nxbins, nybins, outfile):
    hist = get_2d_hist(rootfile, plot_name, nxbins, nybins)
    plot(hist, outfile)

if __name__ == '__main__':
    MAIN_OPTIONS = vars(parse_args())
    main(**MAIN_OPTIONS)
