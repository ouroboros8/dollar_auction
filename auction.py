# pylint: disable=import-error
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

    def __init__(self, pop_size, mem_len, gen_len, initial_population=None):
        self.mem_len = mem_len
        self.gen_len = gen_len
        self.pop_size = pop_size
        self.initial_population = initial_population
        self.population = self.get_initial_population()

    def get_initial_population(self):
        '''
        Get the initial population, or create a random one if there is
        no initial population.
        '''
        if self.initial_population:
            genomes = self.initial_population
        else:
            genomes = [Individual(self.mem_len, self.random_genome())
                       for i in range(0, self.pop_size)]
        return genomes

    def random_genome(self):
        '''
        Generate a random genome
        '''
        genome = [None]*self.gen_len
        genome = [(random.choice(['i', 'd', 'e',
                                  random.randint(0, self.mem_len)
                                 ]
                                ),
                   random.randint(0, self.mem_len),
                   (random.randint(0, self.gen_len),
                    random.randint(0, self.gen_len))
                  ) for elem in genome]
        return genome

    def game(self):
        '''
        Entire runthrough.
        '''

    def round_robin(self):
        '''
        Each member of the current population plays a match against each
        other member. Too slow?
        '''
        for i in range(0, self.pop_size-1):
            for j in range(i+1, self.pop_size-1):
                self.match(self.population[i], self.population[j])

    def match(self, ind1, ind2):
        '''
        Play the two individuals against each other.
        '''

    def select_fittest(self):
        '''
        Select the fittest members of a population.
        '''
    
    def repopulate(self):
        '''
        Produce a new population from the fittest.
        '''

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
            ('i', n, (j, -)) increments the n^th integer in memory, then
                        jumps to instruction j, - ignored;
            ('d', n, (j, -)) decrements the n^th integer in memory, then
                        jumps to instruction j, - ignored;
            (n, m, (j, k)) jumps to instruction j if n >= m, jumps to
                        instruction k otherwise.
            (e, -, (-, -)) end (all later vars irrelevant)
        Obviously, n and m must be valid memory indices, and j and k
        must be valid instruction set indices.
        '''
        self.genome = genome
        self.memory = numpy.array([0]*mem_len, dtype='uint')
        self.money = 0

    def add_money(self, amount):
        '''
        Add amount of money to the Individual's bank. Amount may be
        negative.
        '''
        self.money = self.money + amount

    def play(self, bids):
        '''
        Make a bid, based on a list of previous bids.
        '''

    def reproduce(self):
        '''
        Produce offspring
        '''
