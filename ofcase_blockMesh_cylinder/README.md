# Cylindrical mesh generation with blockMesh

This OpenFOAM case is to experiment with a script for generating a blockMeshDict
file which will create a cylindrical mesh.

Credit for the original script to [Ehsan Mahdadi](https://www.ehsanmadadi.com/cylinder-mesh/).

Usage:
```bash
m4 blockMeshDict.m4 > system/blockMeshDict
blockMesh
```
