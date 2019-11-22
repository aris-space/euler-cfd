# OpenFOAM case folder for validations with HEIDI

Simulation of HEIDI without airbrakes for comparison with CFD results (Mach 0.3) and wind tunnel measurements (80 m/s) from HEIDI's team.
Grid refinement study with four grid resolutions.

Case            | Mesh resolution | U | Ma | 
|--|--|--|--|
| 01_meshing |    30x30x75 | - | - |
| 02_meshing |   60x60x150 | - | - |
| 03_meshing |   90x90x225 | - | - |
| 04_meshing | 120x120x300 | - | - |
| 05_validation |    30x30x75 | 101.38 m/s | 0.3 |
| 06_validation |   60x60x150 | 101.38 m/s | 0.3 |
| 07_validation |   90x90x225 | 101.38 m/s | 0.3 |
| 08_validation | 120x120x300 | 101.38 m/s | 0.3 |
| 09_validation |    30x30x75 | 80 m/s | 0.237 |
| 10_validation |   60x60x150 | 80 m/s | 0.237 |
| 11_validation |   90x90x225 | 80 m/s | 0.237 |
| 12_validation | 120x120x300 | 80 m/s | 0.237 |


## Thermophysical properties

U.S. standard atmosphere model at 2000ft (609.6m)
* Molecular weight: 28.96
* T = 284.188 K
* p = 94212.9 Pa
* Cp = 1005 J kg^-1 K^-1 (specific heat)
* As = 1.458e-6 (Sutherland coefficient)
* Ts = 110.4 (Sutherland temperature)

## References

* Moran, Shapiro - Fundamentals of Engineering Thermodynamics, eighth edition, p.961
* [U.S. Std Atmosphere calculator](http://www.luizmonteiro.com/StdAtm.aspx)
* [Sutherland's law](https://www.cfd-online.com/Wiki/Sutherland's_law)
* [OpenFOAM thermophysical properties](https://cfd.direct/openfoam/user-guide/v4-thermophysical/)
