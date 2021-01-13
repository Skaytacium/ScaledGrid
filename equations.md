# Grid calculations
## Variables needed for calculating grid size:
* Nk = Number of cells in a row/column (square grid only, yet)
* DL = Desired radius/length of each cell
* BL = Side of the square grid (Total)
---
## Link for desmos calculations [here](https://www.desmos.com/calculator/qk4fmwbszp) (just input the variables in the Variables folder)
---
## Text-based formulas
### Padding
	PA = (((BL / DL) - Nk) * DL) / (Nk * 2)
---
### Coordinates
*n = Coordinate number (for each cell)*

	(PA * (n + 1)) + ((DL + PA) * n) + (DL / 2)

## LaTeX based formulas (Desmos/Wolfram/Geogebra)
### Padding
	P_{A}=\frac{\left(\frac{B_{L}}{D_{L}}-N_{k}\right)\cdot D_{L}}{N_{k}\cdot2}
---
### Coordinates
*n = Coordinate number (for each cell)*

	\left(P_{A}\right)n+\left(D_{L}+P_{A}\right)\left(n-1\right)+\left(\frac{D_{L}}{2}\right)
