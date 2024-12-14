import unittest

from kruskal_algorithm import *

class TestUnionFind(unittest.TestCase):
    def test_find_single(self):
        # Проверка find на массиве где каждый элемент - свой родитель
        parent = [0, 1, 2, 3]
        self.assertEqual(find(parent, 0), 0)
        self.assertEqual(find(parent, 1), 1)
        self.assertEqual(find(parent, 2), 2)
        self.assertEqual(find(parent, 3), 3)

    def test_union_simple(self):
        parent = [0, 1, 2, 3]
        rank = [0, 0, 0, 0]

        # Объединяем множества {0} и {1}
        union(parent, rank, 0, 1)
        self.assertEqual(find(parent, 0), find(parent, 1))

        # Объединяем множества {2} и {3}
        union(parent, rank, 2, 3)
        self.assertEqual(find(parent, 2), find(parent, 3))

        # Объединяем {0,1} и {2,3}
        union(parent, rank, 1, 2)
        self.assertEqual(find(parent, 0), find(parent, 2))
        self.assertEqual(find(parent, 1), find(parent, 3))


class TestKruskal(unittest.TestCase):
    def test_kruskal_simple_line(self):
        n = 3
        edges = [
            (0, 1, 1),
            (1, 2, 2)
        ]
        mst = kruskal(n, edges)
        self.assertEqual(len(mst), 2)
        self.assertIn((0, 1, 1), mst)
        self.assertIn((1, 2, 2), mst)

    def test_kruskal_triangle(self):
        n = 3
        edges = [
            (0, 1, 10),
            (1, 2, 15),
            (0, 2, 5)
        ]
        mst = kruskal(n, edges)
        self.assertEqual(len(mst), 2)
        self.assertIn((0, 2, 5), mst)
        self.assertIn((0, 1, 10), mst)

    def test_kruskal_multiple_components(self):
        n = 4
        edges = [
            (0, 1, 1),
            (0, 2, 2),
            (2, 3, 2)
        ]
        mst = kruskal(n, edges)
        self.assertEqual(len(mst), 3)
        self.assertIn((0, 1, 1), mst)
        self.assertIn((0, 2, 2), mst)
        self.assertIn((2, 3, 2), mst)

    def test_kruskal_bigger_graph(self):
        n = 5
        edges = [
            (0, 1, 2),
            (1, 2, 3),
            (2, 3, 4),
            (1, 3, 4),
            (0, 4, 4),
            (2, 4, 3)
        ]
        mst = kruskal(n, edges)
        self.assertEqual(len(mst), 4)
        weights = [w for (_,_,w) in mst]
        self.assertTrue(sum(weights) <= 2+3+3+4)
if __name__ == '__main__':
    unittest.main()