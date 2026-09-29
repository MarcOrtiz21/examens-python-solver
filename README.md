# Adaptador i exemples per a `Algebra.py`

Aquest repositori conté un petit adaptador executable per provar algunes
funcionalitats d’àlgebra lineal de la biblioteca `Algebra.py`. La contribució
pròpia del repositori és `monster_solver.py`, amb exemples de geometria afí,
Gram–Schmidt, regressió lineal, diagonalització de matrius i classificació de
quàdriques.

L’abast és deliberadament modest i verificable: aquest repositori no és un
generador d’exàmens, no incorpora models o serveis d’intel·ligència artificial,
i no té cap integració amb Jutge.org.

## Contingut

- `Algebra.py`: còpia de la biblioteca matemàtica d’**Rafel Amer**.
- `monster_solver.py`: adaptador i exemples creats per **Marc Ortiz**.
- `test_monster_solver.py`: proves de regressió de les funcionalitats de
  l’adaptador.
- `requirements.txt`: dependència Python necessària.
- `LICENSE`: text de la GNU General Public License, versió 3.

L’adaptador imprimeix resultats quan s’executa com a programa, però els seus
mètodes també retornen els objectes calculats per facilitar-ne la reutilització
i les proves.

## Relació amb el projecte original

La biblioteca `Algebra.py` prové del repositori
[`rafelamer/examens-python`](https://github.com/rafelamer/examens-python), una
utilitat per generar exàmens aleatoris amb models de preguntes, Python, SymPy i
LaTeX. En aquesta còpia es conserva la capçalera original, que identifica
Rafel Amer com a autor i declara la llicència GPL.

En la revisió local del 29/09/2026, el `Algebra.py` d’aquest repositori és
byte a byte idèntic a la versió actual del fitxer homònim del repositori
original (`9369` línies; SHA-256
`8ee4f58b2d6dce8773b7cbcf2339ead5f2c394b5bb338f2e33e8a79a11aab08a`). Per
tant, no s’ha de descriure aquesta biblioteca com un desenvolupament original
de Marc.

Aquest repositori només n’utilitza una selecció de classes. No inclou els
scripts de generació d’exàmens, les plantilles LaTeX, la gestió d’estudiants,
l’enviament de correus ni la resta d’eines del projecte original.

## Instal·lació i ús

Es necessita Python 3 i SymPy. Una instal·lació reproduïble en un entorn
virtual és:

```bash
git clone https://github.com/MarcOrtiz21/examens-python-solver.git
cd examens-python-solver
python3 -m venv .venv
source .venv/bin/activate       # macOS/Linux
python -m pip install -r requirements.txt
```

Per executar els exemples:

```bash
python monster_solver.py
```

Per executar les proves:

```bash
python -m unittest discover -s . -p 'test_*.py' -v
```

La revisió s’ha verificat amb Python 3.14.7 i SymPy 1.14.0. No hi ha encara
un paquet instal·lable ni una interfície de línia d’ordres amb arguments; per
provar altres casos cal modificar els exemples del bloc final de
`monster_solver.py` o importar `MonsterSolver` des d’un altre script.

## Autoria i llicència

- **Rafel Amer** és l’autor identificat al fitxer `Algebra.py` i del motor
  matemàtic original.
- **Marc Ortiz** és l’autor del `monster_solver.py` i de les proves i la
  documentació específiques d’aquest repositori, segons l’historial Git local.
- El codi es distribueix amb el text de la **GNU GPL v3** inclòs a `LICENSE`.
  Cal conservar els avisos i respectar la llicència del motor original en
  qualsevol redistribució.

## Descripció breu

Adaptador Python que reutilitza la biblioteca d’àlgebra lineal `Algebra.py`
d’Rafel Amer per executar i provar exemples de càlcul simbòlic —geometria afí,
Gram–Schmidt, regressió, diagonalització i quàdriques—. La contribució pròpia
és la capa d’exemples i proves; no és un generador d’exàmens ni una integració
amb Jutge.org.
