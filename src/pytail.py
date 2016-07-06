"""
pytail module. This is a simple tail command. PyTail supports -n option.
"""
from __future__ import print_function
import os
import os.path
from argparse import ArgumentParser

class PyTail(object):
    """
    Class to perform tail command.
    """
    def __init__(self, fname, nline):
        """
        Constructor of PyTail
        :param fname: file to open
        :param nline: line numbers to show
        """
        self.fname = fname
        self.nline = nline
        self.bufsize = 4092
        if not os.path.exists(self.fname):
            raise IOError("{0} does not exist.".format(self.fname))
        if not os.path.isfile(self.fname):
            raise IOError("{0} is not a file.".format(self.fname))
        if not os.access(self.fname, os.R_OK):
            raise IOError("No read access to {0}. Please check permission.".format(
                self.fname
            ))

    def read_lines(self):
        """
        Read the given number, self.nline, from the end of file. Return the list
        of lines.
        :return: list of lines
        """
        fsize = os.path.getsize(self.fname)
        data = []
        itr = 0
        if self.bufsize > fsize:
            self.bufsize = fsize - 1
        with open(self.fname) as f_to_read:
            while len(data) < self.nline or f_to_read.tell() == 0:
                itr += 1
                f_to_read.seek(-self.bufsize*itr, os.SEEK_END)
                lines = f_to_read.readlines()
                if len(lines) >= self.nline:
                    data.extend(lines)
        return data[-self.nline:]

    def print_lines(self):
        """
        Print the lines read from the file. strip lines for better print
        formatting.
        """
        print(*[line.strip() for line in self.read_lines()], sep='\n')


def main():
    """
    Main function of this application
    """
    parser = ArgumentParser(description='show tail of the file.')
    parser.add_argument('fname', metavar='filename', type=str,
                        help='file to open')
    parser.add_argument('-n', dest='nline', default=10, type=int,
                        help='number of line to show')

    args = parser.parse_args()
    pytail = PyTail(args.fname, args.nline)
    pytail.print_lines()

if __name__ == "__main__":
    main()

