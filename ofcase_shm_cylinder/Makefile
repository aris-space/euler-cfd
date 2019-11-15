
NPROCS = 8
LOGDIR = log
BUFSIZE = 1000000
MPI = export MPI_BUFFER_SIZE=$(BUFSIZE) && mpirun


.PHONY: mesh
mesh: blockMesh constant/extendedFeatureEdgeMesh
	mkdir -p $(LOGDIR)
	decomposePar 2>&1 | tee $(LOGDIR)/decomposePar_mesh.log
	$(MPI) -np $(NPROCS) snappyHexMesh -overwrite -parallel 2>&1 | tee $(LOGDIR)/snappyHexMesh.log
	reconstructParMesh -constant 2>&1 | tee $(LOGDIR)/reconstructParMesh.log
#	rm -rf processor*

.PHONY: blockMesh
blockMesh: constant/polyMesh

constant/extendedFeatureEdgeMesh: constant/triSurface/rocket.stl
	surfaceFeatureExtract 2>&1 | tee $(LOGDIR)/surfaceFeatureExtract.log

constant/polyMesh: system/blockMeshDict $(LOGDIR)
	blockMesh 2>&1 | tee $(LOGDIR)/blockMesh.log

system/blockMeshDict: blockMeshDict.m4
	m4 blockMeshDict.m4 > system/blockMeshDict

$(LOGDIR):
	mkdir -p $(LOGDIR)

.PHONY: clean
clean:
	rm -rf system/blockMeshDict
	rm -rf 0.*/
	rm -rf processor*
	rm -rf constant/extendedFeatureEdgeMesh
	rm -rf constant/polyMesh
	rm -rf constant/triSurface/*.eMesh
