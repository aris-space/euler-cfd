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
| 13_validation | 20x20x50 | 80 m/s | 0.237 |


## Thermophysical properties

### 05-08_validation
U.S. standard atmosphere model at 2000ft (609.6m)
* Molecular weight: 28.96
* T = 284.188 K
* p = 94212.9 Pa
* Cp = 1005 J kg^-1 K^-1 (specific heat)
* As = 1.458e-6 (Sutherland coefficient)
* Ts = 110.4 (Sutherland temperature)

### 09-12_validation
Based on TELL windtunnel measurements
* Molecular weight: 28.96
* T = 20°C (292.15 K)
* p = 95540 Pa
* Cp = 1005 J kg^-1 K^-1 (specific heat)
* As = 1.458e-6 (Sutherland coefficient)
* Ts = 110.4 (Sutherland temperature)

## Results

Absolute total drag force, compared to results from HEIDI's CFD team and windtunnel results on HEIDI.

Case            | Source | Expected drag | Result | Error | Cd
|--|--|--|--|--|--|
| 05_validation | HEIDI CFD | 43.524 N |  |
| 06_validation | HEIDI CFD | 43.524 N |  |
| 07_validation | HEIDI CFD | 43.524 N |  |
| 08_validation | HEIDI CFD | 43.524 N |  |
| 09_validation | HEIDI windtunnel | 26 N | 26.28221 N | < 4% | 0.2539328
| 10_validation | HEIDI windtunnel | 26 N |  |
| 11_validation | HEIDI windtunnel | 26 N |  |
| 12_validation | HEIDI windtunnel | 26 N |  |
| 13_validation | HEIDI windtunnel | 26 N |  |

## References

* Moran, Shapiro - Fundamentals of Engineering Thermodynamics, eighth edition, p.961
* [U.S. Std Atmosphere calculator](http://www.luizmonteiro.com/StdAtm.aspx)
* [Sutherland's law](https://www.cfd-online.com/Wiki/Sutherland's_law)
* [OpenFOAM thermophysical properties](https://cfd.direct/openfoam/user-guide/v4-thermophysical/)

## Raw results

```cpp
$ cat 09_validation/log/rhoSimpleFoam.log
[...]
Time = 784

DILUPBiCGStab:  Solving for Ux, Initial residual = 4.582815e-05, Final residual = 1.228141e-06, No Iterations 1
DILUPBiCGStab:  Solving for Uy, Initial residual = 4.519319e-05, Final residual = 1.324306e-06, No Iterations 1
DILUPBiCGStab:  Solving for Uz, Initial residual = 2.221675e-05, Final residual = 6.683751e-07, No Iterations 1
DILUPBiCGStab:  Solving for e, Initial residual = 6.367175e-05, Final residual = 2.511247e-06, No Iterations 1
GAMG:  Solving for p, Initial residual = 9.741916e-05, Final residual = 5.241919e-07, No Iterations 5
time step continuity errors : sum local = 4.283349e-07, global = -1.418066e-08, cumulative = 0.07724025
rho max/min : 1.168162 1.106936
DILUPBiCGStab:  Solving for omega, Initial residual = 1.339964e-06, Final residual = 4.798907e-07, No Iterations 1
DILUPBiCGStab:  Solving for k, Initial residual = 7.527615e-06, Final residual = 2.133849e-07, No Iterations 1
ExecutionTime = 177.97 s  ClockTime = 178 s


SIMPLE solution converged in 784 iterations

    functionObjects::MachNo MachNo writing field: Ma
forces forces write:
    sum of forces:
        pressure : (4.377093 -0.9897348 -14.17924)
        viscous  : (-0.004016255 -3.044019e-05 -12.10281)
        porous   : (0 0 0)
    sum of moments:
        pressure : (0.1328855 0.5530255 0.03593551)
        viscous  : (0.0003781409 0.0001624526 -0.0003840373)
        porous   : (0 0 0)

forceCoeffs forceCoeffs write:
    Cm    = 0.008470867
    Cd    = -0.2539328
    Cl    = -0.009562949
    Cl(f) = 0.003689393
    Cl(r) = -0.01325234
[...]
```

