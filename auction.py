'''
Genetic approach to dollar auction problem. Individuals compete against
each other, and the individuals who make the lowest loss win.
'''
import numpy
import random

class Run():
    '''
    Object representing a run of the problem
    '''

    def __init__(self, pop_size, mem_len, gen_len):
        self.mem_len = mem_len
        self.gen_len = gen_len
        self.initial_population = [Individual(mem_len,
                                              self.random_genome())
                                   for i in range(0, pop_size)]

    def random_genome(self):
        '''
        Generate a random genome
        '''
        genome = [None]*self.gen_len
        genome = [(random.choice(['i', 'd',
                                  random.randint(0, self.mem_len)
                                 ]
                                ),
                   random.randint(0, self.mem_len),
                   (random.randint(0, self.gen_len),
                    random.randint(0, self.gen_len))
                  ) for elem in genome]
        return genome

class Individual():
    '''
    A competing individual in the dollar auction tournament.
    '''

    def __init__(self, mem_len, genome):
        '''
        Initialise an Individual with a certain genome. The genome
        consists of the "instruction set" of the individual, and is a
        list of instructions, in the form of tuples. The first element
        of each tuple denotes an operation, and the second the index in
        the Individual's memory array to operate on. The possible tuples
        are as follows:
            ('i', n, (j, k)) increments the n^th integer in memory, then
                        jumps to instruction j, k ignored;
            ('d', n, (j, k)) decrements the n^th integer in memory, then
                        jumps to instruction j, k ignored;
            (n, m, (j, k)) jumps to instruction j if n >= m, jumps to
                        instruction k otherwise.
        Obviously, n and m must be valid memory indices, and j and k
        must be valid instruction set indices.
        '''
        self.genome = genome
        self.memory = numpy.array([0]*mem_len, dtype='uint')

    def play(self, bids):
        '''
        Make a bid, based on a list of previous bids.
        '''
