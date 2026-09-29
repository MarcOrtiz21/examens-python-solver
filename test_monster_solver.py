#!/usr/bin/env python3
"""Regression tests for the repository-specific solver adapter."""

import unittest

from sympy import Matrix, sqrt

from monster_solver import MonsterSolver


class MonsterSolverTests(unittest.TestCase):
    def setUp(self):
        self.solver = MonsterSolver()

    def test_gram_schmidt_and_full_space_complement(self):
        base, complement = self.solver.ortonormalitzacio(
            [[1, 1, 0], [1, 0, 1], [0, 1, 1]]
        )

        self.assertTrue(base.es_ortogonal())
        self.assertIsNone(complement)

    def test_affine_distance_and_intersection(self):
        resultat = self.solver.interseccio_i_distancia(
            "pla", [[1, 0, 0], [1, 1, 1]], "punt", [5, 5, 5]
        )

        self.assertEqual(resultat["distancia"], 14 * sqrt(3) / 3)
        self.assertIsNone(resultat["interseccio"])

    def test_linear_regression(self):
        regressio = self.solver.regressio_lineal(
            [(1, 2), (2, 4), (3, 6), (4, 8)]
        )

        self.assertEqual(regressio.equacio(), "y = 2 x")

    def test_matrix_analysis(self):
        matriu = self.solver.analitza_matriu_completa([[2, 1], [1, 2]])

        self.assertEqual(matriu.rank(), 2)
        self.assertEqual(matriu.det(), 3)
        self.assertTrue(matriu.diagonalitzable)
        self.assertEqual(set(matriu.vaps), {1, 3})

    def test_quadric_analysis(self):
        quadrica = self.solver.analitza_quadrica_completa(
            Matrix.diag(1, 1, 1, -1)
        )

        self.assertEqual(quadrica.tipus(), "El·lipsoide real")
        self.assertEqual(quadrica.equacio_reduida(), "x'^2 + y'^2 + z'^2 = 1")

    def test_invalid_affine_type_is_reported(self):
        with self.assertRaises(ValueError):
            self.solver.interseccio_i_distancia("nope", [1], "punt", [1])


if __name__ == "__main__":
    unittest.main()
