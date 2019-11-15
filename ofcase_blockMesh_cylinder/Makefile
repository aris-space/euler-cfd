
.PHONY: mesh
mesh: constant/polyMesh

constant/polyMesh: system/blockMeshDict
	blockMesh

system/blockMeshDict: blockMeshDict.m4
	m4 blockMeshDict.m4 > system/blockMeshDict

.PHONY: clean
clean:
	rm system/blockMeshDict
	rm -rf constant/polyMesh

