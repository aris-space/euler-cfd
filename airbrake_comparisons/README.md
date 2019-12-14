# Airbrake design variants - comparison

* Lip all around (`01_full_lip`)
* Lip only on sides (`02_side_lips`)

## Thermophysical properties

[U.S. standard atmosphere](http://www.luizmonteiro.com/StdAtm.aspx) model at 7500m ASL.
* Molecular weight: 28.96
* T = 239.457 K
* p = 38.2997 kPa = 38299.7 Pa
* Cp = 1005 J kg^-1 K^-1 (specific heat)
* As = 1.458e-6 (Sutherland coefficient)
* Ts = 110.4 (Sutherland temperature)
* (rho = 0.557192 km/m^3)

## Intermediate results

### 01_full_lip

Model with raised edge all around.

#### U = 225 m/s

Pressure forces [N] at iteration 271800 (still not full convergence):
* Airbrake 1: (-8 10 -153)
* Airbrake 2: (9 9 -174)

#### U = 250m/s
Currently running. Have been experiencing convergence issues in past days.

### 02_side_lips

None so far. Currently running with U = 15m/s.


## Final results

None so far.
