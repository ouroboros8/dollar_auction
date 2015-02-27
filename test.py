import unittest
import auction

class GameTests(unittest.TestCase):

    def test_game_instantiation(self):
        opts = {
            'memory_length': 500,
            'genome_length': 500,
            'match_timeout': 1,
            'bid_timeout': 0.1
            }
        game = auction.Game(generations=100, pop_size=10, opts=opts)
        self.assertEqual(game.opts, opts)
        self.assertEqual(len(game.initial_gene_pool), 10)
        self.assertEqual(len(game.gene_pool), 10)
        self.assertEqual(game.generations, range(0, 100))
        self.assertIs(game.the_round, None)

    def test_game_instantiation_defaults(self):
        game = auction.Game()
        self.assertEqual(game.opts, auction.DEFAULT_OPTS)
        self.assertEqual(len(game.initial_gene_pool), 100)
        self.assertEqual(len(game.gene_pool), 100)
        self.assertEqual(game.generations, range(0, 1000))
        self.assertIsNone(game.the_round)
