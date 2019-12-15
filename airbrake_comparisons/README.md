# Airbrake design variants - comparison

<!-- vim-markdown-toc GFM -->

* [Cases](#cases)
* [Thermophysical properties](#thermophysical-properties)
* [Intermediate results](#intermediate-results)
    * [01_full_lip](#01_full_lip)
        * [U = 225m/s](#u--225ms)
        * [U = 250m/s](#u--250ms)
    * [02_side_lips](#02_side_lips)
* [Final results](#final-results)

<!-- vim-markdown-toc -->

## Cases

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

#### U = 225m/s

Pressure forces [N] at iteration 271800 (still not full convergence):
* Airbrake 1: (-8 10 -153)
* Airbrake 2: (9 9 -174)

#### U = 250m/s
Convergence issues due to oscillatory mode of the solver. Reporting average and min/max of oscillations:

| ab_1 | Min [N] | Avg [N] | Max [N] | Error margin +-%
|--|--|--|--|--|
| Fx | -17.420 | -15.772 | -12.795 | 18.878
| Fy | 10.815 | 14.159 | 15.92 | 12.499
| Fz | -194.10 | -191.84 | -189.27 | 1.3394


| ab_2 | Min [N] | Avg [N] | Max [N] | Error margin +-%
|--|--|--|--|--|
| Fx | 12.634 | 13.857 | 15.198 | 9.6815
| Fy | 13.859 | 15.121 | 16.267 | 7.5770
| Fz | -218.70 | -216.55 | -213.79 | 1.2717

`ab_1` is the lower airbrake (closest to the motor), `ab_2` is the upper one.

**Important:** these are min/max values of the solver oscillations at 250 m/s, **not** of the overall flight.

**Even more important:** this error margin is over the solver oscillations for the mesh quality used. It does **not** guarantee quality of the actual value in physical terms. That requires mesh refinement studies and experimental validation.

### 02_side_lips

None so far. Currently running with U = 250m/s.


## Final results

None so far. I am working on a way to combat solver oscillations. It will likely entail manually detecting the beginning of oscillations and reducing the relaxation factors in the solver to make it proceed more slowly.
