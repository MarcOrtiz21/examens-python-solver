#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from sympy import symbols, Matrix, solve, simplify
from Algebra import (Matriu, SistemaEquacions, Vector, Conica, Quadrica, 
                     TransformacioLineal, Punt, SubespaiVectorial, 
                     SuperficieRevolucio, Hiperbola, Base, RectaAfi, PlaAfi,
                     RectaRegressio)

class MonsterSolver:
    def __init__(self):
        print("===  MONSTER SOLVER V4.0 - THE ULTIMATE LOGIC REVERSE  ===")

    # =========================================================
    # 1. ESPAIS VECTORIALS AVANÇATS
    # =========================================================
    def ortonormalitzacio(self, llista_vectors):
        print("\n--- [1] GRAM-SCHMIDT I COMPLEMENT ORTOGONAL ---")
        vecs = [Vector(v) for v in llista_vectors]
        # Creem una base i apliquem ortogonalització
        B = Base(vecs, ortogonal=True)
        print(f"Base Ortogonal calculada:\n{B}")
        
        # Suplementari Ortogonal
        sub = SubespaiVectorial(vecs)
        comp = sub.suplementari_ortogonal()
        print(f"Suplementari Ortogonal del subespai:\n{comp}")

    # =========================================================
    # 2. GEOMETRIA AFÍ I DISTÀNCIES
    # =========================================================
    def interseccio_i_distancia(self, tipus1, dades1, tipus2, dades2):
        print(f"\n--- [2] GEOMETRIA AFÍ: {tipus1} vs {tipus2} ---")
        def crear_obj(t, d):
            if t == 'punt': return Punt(d)
            if t == 'recta': return RectaAfi(Punt(d[0]), Vector(d[1]))
            if t == 'pla': return PlaAfi.amb_associat(Vector(d[1]), Punt(d[0]))
        
        obj1 = crear_obj(tipus1, dades1)
        obj2 = crear_obj(tipus2, dades2)
        
        # Distància
        try:
            print(f"Distància: {obj1.distancia(obj2)}")
        except:
            print(f"Distància: {(obj1-obj2).length()}")
            
        # Intersecció (si existeix el mètode a la llibreria)
        try:
            inter = obj1.interseccio(obj2)
            print(f"Intersecció: {inter}")
        except:
            pass

    # =========================================================
    # 3. ESTADÍSTICA: REGRESSIÓ LINEAL
    # =========================================================
    def regressio_lineal(self, llista_punts):
        print("\n--- [3] REGRESSIÓ LINEAL (Ajust de punts) ---")
        try:
            # Convertim llista de tuples a llista de Punts
            punts = [Punt(p) for p in llista_punts]
            r = RectaRegressio(punts)
            print(f"Punts analitzats: {llista_punts}")
            print(f"Recta de regressio: {r.equacio()}")
        except Exception as e:
            print(f"Error en regressió: {e}")

    # =========================================================
    # 4. MÒDULS DE RESOLUCIÓ EXISTENTS (MILLORATS)
    # =========================================================
    def analitza_matriu_completa(self, llista_matriu):
        print("\n--- [4] ANÀLISI COMPLETA DE MATRIU ---")
        M = Matriu(Matrix(llista_matriu))
        print(f"Rang: {M.rank()} | Det: {M.det() if M.files == M.columnes else 'N/A'}")
        M.diagonalitza()
        if M.diagonalitzable:
            print(f"VAPs: {M.vaps}")
            print(f"Matriu de pas (P):\n{Matriu.from_vectors_columna(M.veps)}")
        return M

    def analitza_quadrica_completa(self, m_amp):
        print("\n--- [5] ANÀLISI DE QUÀDRICA ---")
        Q = Quadrica.from_equacio(Quadrica(Matriu(Matrix(m_amp))).equacio())
        print(f"Tipus: {Q.tipus()}")
        print(f"Equació reduïda: {Q.equacio_reduida()}")
        print(f"Origen del sistema: {Q.ref.origen}")

if __name__ == "__main__":
    solver = MonsterSolver()
    
    # 1. Exemple Gram-Schmidt
    solver.ortonormalitzacio([[1,1,0], [1,0,1], [0,1,1]])
    
    # 2. Distància Punt-Pla (en R3)
    # Pla: x + y + z = 1 -> punt [1,0,0], normal [1,1,1]
    solver.interseccio_i_distancia('pla', [[1,0,0], [1,1,1]], 'punt', [5,5,5])
    
    # 3. Regressió Lineal (Curiositat estadística de la llibreria)
    solver.regressio_lineal([(1, 2), (2, 4), (3, 6), (4, 8)])
    
    # 4. Una matriu aleatòria del professor per veure la seva estructura
    A_random = [[2, 1], [1, 2]]
    solver.analitza_matriu_completa(A_random)
