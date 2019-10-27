NPROCS = 16
LOGDIR = log

.PHONY: mesh shm check clean

mesh:
	mkdir -p $(LOGDIR)
	blockMesh 2>&1 | tee $(LOGDIR)/blockMesh.log
	surfaceFeatureExtract 2>&1 | tee $(LOGDIR)/surfaceFeatureExtract.log
	decomposePar 2>&1 | tee $(LOGDIR)/decomposePar.log
	make shm
	reconstructParMesh -constant 2>&1 | tee $(LOGDIR)/reconstructParMesh.log

shm:
	mkdir -p $(LOGDIR)
	mpirun -np $(NPROCS) snappyHexMesh -overwrite -parallel 2>&1 | tee $(LOGDIR)/snappyHexMesh.log

check:
	mkdir -p $(LOGDIR)
	checkMesh 2>&1 | tee $(LOGDIR)/checkMesh.log

clean:
	rm -rf processor*
	rm -rf constant/extendedFeatureEdgeMesh
	rm -rf constant/polyMesh
	rm -rf constant/triSurface/*.eMesh
