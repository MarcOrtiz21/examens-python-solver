#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Small command-line adapter around Rafel Amer's ``Algebra.py`` library.

This file contains the repository-specific contribution: a few reusable
examples that exercise selected parts of the upstream library.  It is not an
exam generator and does not connect to an external judge or an AI service.
"""

from sympy import Matrix

from Algebra import (
    Base,
    Matriu,
    PlaAfi,
    Punt,
    Quadrica,
    RectaAfi,
    RectaRegressio,
    SubespaiVectorial,
    Vector,
)


class MonsterSolver:
    """Convenience wrapper for selected linear-algebra demonstrations."""

    @staticmethod
    def _crear_objecte_afí(tipus, dades):
        """Build an affine object and report malformed input clearly."""
        if not isinstance(tipus, str):
            raise ValueError("El tipus ha de ser 'punt', 'recta' o 'pla'.")

        tipus = tipus.lower()
        try:
            if tipus == "punt":
                obj = Punt(dades)
            elif tipus == "recta":
                if len(dades) != 2:
                    raise ValueError("Una recta necessita un punt i un vector.")
                obj = RectaAfi(Punt(dades[0]), Vector(dades[1]))
            elif tipus == "pla":
                if len(dades) != 2:
                    raise ValueError("Un pla necessita un punt i un vector normal.")
                obj = PlaAfi.amb_associat(Vector(dades[1]), Punt(dades[0]))
            else:
                raise ValueError("Tipus d'objecte afí desconegut: %s" % tipus)
        except (IndexError, TypeError) as exc:
            raise ValueError("Dades no vàlides per a un %s." % tipus) from exc

        # Algebra.py uses None to signal invalid constructor arguments.
        if obj is None:
            raise ValueError("No s'ha pogut construir el %s amb aquestes dades." % tipus)
        return obj

    @staticmethod
    def _distancia(obj1, obj2):
        """Return the distance using whichever affine object supports it."""
        for actual, altre in ((obj1, obj2), (obj2, obj1)):
            metode = getattr(actual, "distancia", None)
            if metode is not None:
                distancia = metode(altre)
                if distancia is not None:
                    return distancia
        # This is the natural fallback for two points.
        return (obj1 - obj2).length()

    @staticmethod
    def _dimensio(obj):
        """Return the ambient dimension used by an Algebra.py affine object."""
        if hasattr(obj, "dimensio"):
            return obj.dimensio
        return obj.p.dimensio

    @staticmethod
    def _interseccio(obj1, obj2):
        """Return the available affine intersection, or ``None``."""
        for actual, altre in ((obj1, obj2), (obj2, obj1)):
            metode = getattr(actual, "interseccio", None)
            if metode is not None:
                resultat = metode(altre)
                if resultat is not None:
                    return resultat
        return None

    def ortonormalitzacio(self, llista_vectors):
        """Apply Gram–Schmidt and compute the orthogonal complement."""
        print("\n--- [1] GRAM-SCHMIDT I COMPLEMENT ORTOGONAL ---")
        vecs = [Vector(v) for v in llista_vectors]
        if not vecs or any(v is None for v in vecs):
            raise ValueError("Cal proporcionar una llista no buida de vectors.")

        base = Base(vecs, ortogonal=True)
        if base is None:
            raise ValueError("Els vectors han de ser linealment independents.")
        print(f"Base ortogonal calculada:\n{base}")

        sub = SubespaiVectorial(vecs)
        complement = sub.suplementari_ortogonal()
        if complement is None:
            print("El subespai ja és tot l'espai; no té suplementari ortogonal no trivial.")
        else:
            print(f"Suplementari ortogonal del subespai:\n{complement}")
        return base, complement

    def interseccio_i_distancia(self, tipus1, dades1, tipus2, dades2):
        """Analyse two points, lines or planes in the same affine space."""
        print(f"\n--- [2] GEOMETRIA AFÍ: {tipus1} vs {tipus2} ---")
        obj1 = self._crear_objecte_afí(tipus1, dades1)
        obj2 = self._crear_objecte_afí(tipus2, dades2)
        if self._dimensio(obj1) != self._dimensio(obj2):
            raise ValueError("Els dos objectes han de tenir la mateixa dimensió.")

        distancia = self._distancia(obj1, obj2)
        interseccio = self._interseccio(obj1, obj2)
        print(f"Distància: {distancia}")
        print(f"Intersecció: {interseccio}")
        return {
            "objecte1": obj1,
            "objecte2": obj2,
            "distancia": distancia,
            "interseccio": interseccio,
        }

    def regressio_lineal(self, llista_punts):
        """Fit a least-squares line to at least three two-dimensional points."""
        print("\n--- [3] REGRESSIÓ LINEAL (Ajust de punts) ---")
        punts = [Punt(p) for p in llista_punts]
        if len(punts) <= 2 or any(p is None or p.dimensio != 2 for p in punts):
            raise ValueError("Calen almenys tres punts de dues coordenades.")

        regressio = RectaRegressio(punts)
        if regressio is None:
            raise ValueError("No s'ha pogut construir la recta de regressió.")
        print(f"Punts analitzats: {llista_punts}")
        print(f"Recta de regressió: {regressio.equacio()}")
        return regressio

    def analitza_matriu_completa(self, llista_matriu):
        """Report rank, determinant and eigendata for a SymPy matrix."""
        print("\n--- [4] ANÀLISI COMPLETA DE MATRIU ---")
        try:
            matriu = Matrix(llista_matriu)
        except (TypeError, ValueError) as exc:
            raise ValueError("La matriu no té un format rectangular vàlid.") from exc
        if matriu.rows == 0 or matriu.cols == 0:
            raise ValueError("La matriu no pot ser buida.")

        resultat = Matriu(matriu)
        determinant = resultat.det() if resultat.files == resultat.columnes else "N/A"
        print(f"Rang: {resultat.rank()} | Det: {determinant}")
        resultat.diagonalitza()
        if resultat.diagonalitzable:
            print(f"VAPs: {resultat.vaps}")
            print(f"Matriu de pas (P):\n{Matriu.from_vectors_columna(resultat.veps)}")
        else:
            print("La matriu no és diagonalitzable amb una base completa de vectors propis.")
        return resultat

    def analitza_quadrica_completa(self, matriu_projectiva):
        """Classify a 4x4 symmetric projective matrix as a quadric."""
        print("\n--- [5] ANÀLISI DE QUÀDRICA ---")
        try:
            matriu = Matrix(matriu_projectiva)
        except (TypeError, ValueError) as exc:
            raise ValueError("La matriu de la quàdrica no és vàlida.") from exc
        if matriu.shape != (4, 4):
            raise ValueError("Una quàdrica d'aquest exemple necessita una matriu 4x4.")

        original = Quadrica(Matriu(matriu))
        if original is None:
            raise ValueError("La matriu de la quàdrica ha de ser simètrica.")
        quadrica = Quadrica.from_equacio(original.equacio())
        if quadrica is None:
            raise ValueError("No s'ha pogut classificar aquesta quàdrica.")

        print(f"Tipus: {quadrica.tipus()}")
        print(f"Equació reduïda: {quadrica.equacio_reduida()}")
        if quadrica.ref is not None:
            print(f"Origen del sistema: {quadrica.ref.origen}")
        return quadrica


if __name__ == "__main__":
    solver = MonsterSolver()

    # 1. Exemple Gram-Schmidt
    solver.ortonormalitzacio([[1, 1, 0], [1, 0, 1], [0, 1, 1]])

    # 2. Distància punt-pla (en R3): x + y + z = 1
    solver.interseccio_i_distancia(
        "pla", [[1, 0, 0], [1, 1, 1]], "punt", [5, 5, 5]
    )

    # 3. Regressió lineal (funcionalitat de la biblioteca Algebra.py)
    solver.regressio_lineal([(1, 2), (2, 4), (3, 6), (4, 8)])

    # 4. Exemple de matriu simètrica diagonalitzable
    matriu_exemple = [[2, 1], [1, 2]]
    solver.analitza_matriu_completa(matriu_exemple)
