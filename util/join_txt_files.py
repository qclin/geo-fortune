from os import listdir
from os.path import isfile, join

samples_path = './samples'
filenames = [f for f in listdir(samples_path) if isfile(join(samples_path, f))]

print filenames

with open('compiled_source/samples.txt', 'w') as outfile:
    for fname in filenames:
        with open('./samples/'+fname) as infile:
            for line in infile:
                outfile.write(line)
