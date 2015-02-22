'''
Genetic approach to dollar auction problem. Individuals compete against
each other, and the individuals who make the lowest loss win.
'''
import numpy

class Individual():
    '''
    A competing individual in the dollar auction tournament.
    '''

    def __init__(self, genome=None):
        '''
        Initialise an Individual with a certain genome. The genome
        consists of the "instruction set" of the individual, and is a
        list of tuples. The first element of each tuple denotes an
        instruction, and the second the index in the Individual's
        memory array to operate on. The possible tuples are as follows:
            ('i', n, j) increments the n^th integer in memory, then
                        jumps to instruction j;
            ('d', n, j) decrements the n^th integer in memory, then
                        jumps to instruction j;
            (n, m, (j, k)) jumps to instruction j if n >= m, jumps to
                        instruction k otherwise.
        Obviously, n and m must be valid memory indices, and j and k
        must be valid instruction set indices.
        '''
        if genome:
            self.genome = genome
        else:
            self.genome = random_genome()
        self.memory = numpy.array([0]*1000, dtype='uint')

    def play(self, bids):
        '''
        Make a bid, based on a list of previous bids.
        '''
