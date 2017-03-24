'''
movie2frames.py
==================================================
Writing all frames of the movie.
'''
from __future__ import print_function
import argparse
import glob
import os

import cv2


parser = argparse.ArgumentParser()
parser.add_argument('movies')
args = parser.parse_args()

movies = glob.glob(args.movies)
for movie_file in movies:
    print('Loading movie: {}'.format(movie_file))
    if not os.path.isfile(movie_file):
        raise FileNotFoundError('Not found the movie.')
    movie = cv2.VideoCapture(movie_file)
    if not movie.isOpened():
        raise IOError('Failed to open a movie file.')

    save_dir = os.path.splitext(movie_file)[0]
    if not os.path.isdir(save_dir):
        os.makedirs(save_dir)

    frame_counter = 0
    while True:
        retval, frame = movie.read()
        if retval is None:
            break
        print('# of frames: {}'.format(frame_counter + 1), end='\r')
        filename = os.path.join(save_dir, '{:08d}.jpg'.format(frame_counter))
        cv2.imwrite(filename, frame)
        frame_counter += 1
    movie.release()
print('\nDone')
