# cylindricalMesh.py
# A simple script to generate a blockMeshDict file for a cylindrical mesh
# STILL NOT FUNCTIONAL
# Generates bad meshes. Use m4 script instead.

from math import sqrt

innerRadius = 0.5
outerRadius = 10

zStart = -1
zEnd = 1

innerCells  = 30
radialCells = 30
zCells = 10

radialGrading = 1
zGrading = 1

fileName = "system/blockMeshDict"

def main():

    i = 0

    pos = outerRadius / sqrt(2)

    vertices = ""
    vertices += f"\t(-{innerRadius} -{innerRadius} {zStart})\t// {i}\n"; i += 1
    vertices += f"\t( {innerRadius} -{innerRadius} {zStart})\t// {i}\n"; i += 1
    vertices += f"\t( {innerRadius}  {innerRadius} {zStart})\t// {i}\n"; i += 1
    vertices += f"\t(-{innerRadius}  {innerRadius} {zStart})\t// {i}\n"; i += 1
    vertices += "\n"
    vertices += f"\t(-{innerRadius} -{innerRadius} {zEnd})\t// {i}\n"; i += 1
    vertices += f"\t( {innerRadius} -{innerRadius} {zEnd})\t// {i}\n"; i += 1
    vertices += f"\t( {innerRadius}  {innerRadius} {zEnd})\t// {i}\n"; i += 1
    vertices += f"\t(-{innerRadius}  {innerRadius} {zEnd})\t// {i}\n"; i += 1
    vertices += "\n"
    vertices += f"\t(-{pos}  {pos} {zStart})\t// {i}\n"; i += 1
    vertices += f"\t(-{pos}  {pos} {zEnd})\t// {i}\n"; i += 1
    vertices += "\n"
    vertices += f"\t(-{pos} -{pos} {zStart})\t// {i}\n"; i += 1
    vertices += f"\t(-{pos} -{pos} {zEnd})\t// {i}\n"; i += 1
    vertices += "\n"
    vertices += f"\t( {pos} -{pos} {zStart})\t// {i}\n"; i += 1
    vertices += f"\t( {pos} -{pos} {zEnd})\t// {i}\n"; i += 1
    vertices += "\n"
    vertices += f"\t( {pos}  {pos} {zStart})\t// {i}\n"; i += 1
    vertices += f"\t( {pos}  {pos} {zEnd})\t// {i}\n"; i += 1

    blocks = ""
    blocks += "\thex (1  0  3  2    5  4  7  6) "\
                + f"({innerCells} {innerCells} {zCells}) "\
                + f"simpleGrading (1 1 {zGrading})\n"

    cellsGradings = f" ({radialCells} {innerCells} {zCells}) "\
                  + f"simpleGrading ({radialGrading} 1 {zGrading})\n"
    blocks += f"\thex ( 0 10  8  3    4 11  9  7)" + cellsGradings
    blocks += f"\thex ( 3  8 14  2    7  9 15  6)" + cellsGradings

    edges = ""
    edges += f"\tarc  8 10 (-{outerRadius} 0 {zStart})\n"
    edges += f"\tarc  9 11 (-{outerRadius} 0 {zEnd})\n"
    edges += "\n"
    edges += f"\tarc  8 14 (0 {outerRadius} {zStart})\n"
    edges += f"\tarc  9 15 (0 {outerRadius} {zEnd})\n"
    

    blockMeshDict = getTemplate()
    blockMeshDict = blockMeshDict.replace("// __vertices__", vertices, 1)
    blockMeshDict = blockMeshDict.replace("// __blocks__", blocks, 1)
    blockMeshDict = blockMeshDict.replace("// __edges__", edges, 1)

    print(blockMeshDict)

    with open(fileName, "w") as f:
        f.write(blockMeshDict)


def getTemplate():
     return """
 /*--------------------------------*- C++ -*----------------------------------*\\
 | =========                 |                                                 |
 | \\\\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |
 |  \\\\    /   O peration     | Version:  4.x                                   |
 |   \\\\  /    A nd           | Web:      www.OpenFOAM.org                      |
 |    \\\\/     M anipulation  |                                                 |
 \*---------------------------------------------------------------------------*/
 FoamFile
 {
 	version		2.0;
 	format		ascii;
 	class		dictionary;
 	object		blockMeshDict;
 }
 // * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //
 
 convertToMeters 1;
 
 vertices
 (
 // __vertices__
 );
 
 blocks
 (
 // __blocks__
 );
 
 edges
 (
 // __edges__
 );
 
 boundary
 (
 // __boundary__
 );
 
 mergePatchPairs
 (
 // __mergePatchPairs__
 );
 
 // ************************************************************************* //
 """

if __name__ == "__main__":
    main()
