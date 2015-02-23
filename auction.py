# pylint: disable=import-error
'''
Genetic approach to dollar auction problem. A Game begins with a random
or predefined population, and takes place over a fixed number of rounds.
The population plays a round. A round consists of a round-robin
tournament, and the fittest individuals (winners) are used as the basis
of a new, mutated population for the next round.
'''
import numpy
import random
import signal

from collections.abc import Sequence

DEFAULT_OPTS = {
    "memory_length": 1000,
    "genome_length": 100,
    "match_timeout": 5,
    "bid_timeout": 1,
}

class TimeoutException(Exception):
    '''
    Denotes an error where a process has elapsed for too long.
    '''
    pass

def timeout_handler():
    '''
    Raises a TimeoutException when too much time has passed on a
    process.
    '''
    raise TimeoutException()

def make_population(gene_pool):
    '''
    Produce the current population based on the current gene pool.
    '''
    return [Individual(genome)
            for genome in gene_pool]

class Game():
    '''
    Object representing a run of the problem
    '''

    def __init__(self, generations=1000, pop_size=100, opts=None):
        self.opts = self.__set_opts__(opts)

        self.pop_size = pop_size
        self.initial_gene_pool = self.get_initial_gene_pool()
        self.gene_pool = self.initial_gene_pool

        self.generations = range(0, generations)

        self.the_round = None

    def __set_opts__(self, opts):
        '''
        Set missing options from global DEFAULT_OPTS
        '''
        if not opts:
            opts = {}
        for key in DEFAULT_OPTS:
            if key not in opts:
                opts[key] = DEFAULT_OPTS[key]
        return opts

    def get_initial_gene_pool(self):
        '''
        Get the initial population, or create a random one if there is
        no initial population.
        '''
        if hasattr(self, 'initial_population'):
            genomes = self.initial_gene_pool
        else:
            genomes = [Genome(self.opts["genome_length"],
                              self.opts["memory_length"])
                       for i in range(0, self.pop_size)]
        return genomes


    def run(self):
        '''
        Run the game.
        '''
        for _ in self.generations:
            self.the_round = Round(make_population(self.gene_pool))
            ranking = self.the_round.run()
            # winners = top x percentile or something
            # self.population = reproduce winners
        # return winners

    def select_fittest(self):
        '''
        Select the fittest members of a population.
        '''

    def repopulate(self):
        '''
        Produce a new population from the fittest.
        '''

class Round():
    '''
    A round of the game: tracks scores and creates matches.
    '''

    def __init__(self, population):
        self.population = population

    def run(self):
        '''
        Run the round
        '''
        return self.rank(self.round_robin())

    def rank(self, population):
        '''
        Rank the population by money
        '''

    def round_robin(self):
        '''
        Each member of the current population plays a match against each
        other member. Too slow?
        '''
        pop_size = len(self.population)
        for i in range(0, pop_size-1):
            for j in range(i+1, pop_size-1):
                signal.signal(signal.SIGALRM, timeout_handler)
                signal.alarm(5) # Timeout the match in 5 seconds.
                try:
                    self.match(self.population[i], self.population[j])
                except TimeoutError():
                    pass
                signal.alarm(0)
        return self.population

    def match(self, ind1, ind2):
        '''
        Play the two individuals against each other.
        '''

class Genome(Sequence):
    '''
    The genome consists of the "instruction set" of the individual, and
    is a list of instructions, in the form of tuples. The first element
    of each tuple denotes an operation, and the second the index in the
    Individual's memory array to operate on. The possible tuples are as
    follows:
        ('i', n, (j, -)) increments the n^th integer in memory,
                         then jumps to instruction j, - ignored;
        ('d', n, (j, -)) decrements the n^th integer in memory, then
                         jumps to instruction j, - ignored;
        (n, m, (j, k))   jumps to instruction j if n >= m, or jumps to
                         instruction k otherwise.
        (e, -, (-, -)) end (all later vars irrelevant)
        Obviously, n and m must be valid memory indices, and j and k
        must be valid instruction set indices.
    '''

    def __init__(self, length, mem_len):
        self.__list__ = [None]*length
        self.mem_len = mem_len

        self.__list__ = self.random_genome()

    def __getitem__(self, i):
        return self.__list__[i]

    def __len__(self):
        return len(self.__list__)

    def __random_memory_index__(self):
        return random.randint(0, self.mem_len-1)

    def __random_genome_index__(self):
        return random.randint(0, self.__len__()-1)

    def random_genome(self):
        '''
        Generate a random genome
        '''
        genome = [(random.choice(['i', 'd', 'e',
                                  random.randint(
                                      0,
                                      self.__random_memory_index__()
                                  )]
                                ),
                   random.randint(0, self.__random_memory_index__()),
                   (random.randint(0, self.__random_genome_index__()),
                    random.randint(0, self.__random_genome_index__()))
                  ) for i in range(0, self.__random_genome_index__())]
        return genome

    def mutate(self):
        '''
        Produce a mutation of this genome
        '''
        

class Individual():
    '''
    A competing individual in the dollar auction tournament.
    '''

    def __init__(self, genome):
        '''
        Initialise an Individual with a certain genome.         '''
        self.memory = numpy.array([0]*genome.mem_len, dtype='uint')
        self.genome = genome
        self.money = 0

    def add_money(self, amount):
        '''
        Add amount of money to the Individual's bank. Amount may be
        negative.
        '''
        self.money = self.money + amount

    def play(self, bids):
        '''
        Make a bid, based on a list of previous bids, and amount of
        money left.
        '''
