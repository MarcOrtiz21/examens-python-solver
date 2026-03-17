# Resolutor de Álgebra Lineal - ESEIAAT (UPC)

Este repositorio contiene un entorno de resolución avanzada de problemas de Álgebra Lineal, desarrollado mediante ingeniería inversa sobre la biblioteca matemática del profesor **Rafel Amer** (Departament de Matemàtiques, ESEIAAT - UPC).

## Descripción Técnica
El núcleo del proyecto, `monster_solver.py`, es un motor de cálculo simbólico que integra las capacidades de la biblioteca `Algebra.py` para proporcionar soluciones analíticas precisas a problemas complejos de grado universitario.

### Capacidades de Resolución
- **Sistemas de Ecuaciones Lineales:** Análisis exhaustivo de sistemas paramétricos y determinación de soluciones generales y particulares.
- **Diagonalización de Endomorfismos:** Cálculo de polinomios característicos, espectros (valores propios), subespacios propios (vectores propios) y matrices de paso.
- **Análisis de Formas Quadráticas:** Clasificación de cónicas y cuádricas, obtención de sus ecuaciones reducidas y determinación de las referencias principales.
- **Geometría Afín y Euclídea:** Cálculo de distancias métricas entre variedades lineales (puntos, rectas y planos), proyecciones ortogonales y aplicaciones de simetría.
- **Geometría Diferencial Básica:** Generación de superficies de revolución a partir de curvas paramétricas.
- **Representación Gráfica:** Generación de archivos vectoriales en formato **Asymptote** para la visualización técnica de cónicas.

## Requisitos del Sistema
- **Entorno:** Python 3.8 o superior.
- **Dependencias:** Biblioteca `sympy` para computación simbólica.
  ```bash
  pip install sympy
  ```

## Guía de Uso
Para ejecutar el resolutor con los casos de prueba incluidos, utilice el siguiente comando:
```bash
python3 monster_solver.py
```
Para la resolución de problemas específicos, se recomienda modificar la sección principal (`if __name__ == "__main__":`) del script `monster_solver.py`, introduciendo los coeficientes matriciales o vectoriales correspondientes.

## Reconocimientos y Autoría
Este trabajo se fundamenta en el motor matemático desarrollado originalmente por el profesor Rafel Amer. El propósito de este repositorio es puramente académico, orientado al estudio de la lógica computacional aplicada al álgebra lineal.
