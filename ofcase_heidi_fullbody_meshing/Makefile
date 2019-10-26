NPROCS = 16
LOGDIR = log

.PHONY: mesh shm check clean

mesh:
	mkdir -p $(LOGDIR)
	blockMesh | tee $(LOGDIR)/blockMesh.log
	surfaceFeatureExtract | tee $(LOGDIR)/surfaceFeatureExtract.log
	decomposePar | tee $(LOGDIR)/decomposePar.log
	make shm
	reconstructParMesh -constant | tee $(LOGDIR)/reconstructParMesh.log

shm:
	mkdir -p $(LOGDIR)
	mpirun -np $(NPROCS) snappyHexMesh -overwrite -parallel | tee $(LOGDIR)/snappyHexMesh.log

check:
	mkdir -p $(LOGDIR)
	checkMesh | tee $(LOGDIR)/checkMesh.log

clean:
	rm -rf processor*
	rm -rf constant/extendedFeatureEdgeMesh
	rm -rf constant/polyMesh
	rm -rf constant/triSurface/*.eMesh
