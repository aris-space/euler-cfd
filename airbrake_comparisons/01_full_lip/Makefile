NPROCS = 48
LOGDIR = log

.PHONY: mesh shm check clean

#mesh:
#	mkdir -p $(LOGDIR)
#	blockMesh 2>&1 | tee $(LOGDIR)/blockMesh.log
#	surfaceFeatureExtract 2>&1 | tee $(LOGDIR)/surfaceFeatureExtract.log
#	decomposePar 2>&1 | tee $(LOGDIR)/decomposePar.log
#	make shm
#	reconstructParMesh -constant 2>&1 | tee $(LOGDIR)/reconstructParMesh.log

mesh:
	mkdir -p $(LOGDIR)
	blockMesh 2>&1 | tee $(LOGDIR)/blockMesh.log
	surfaceFeatureExtract 2>&1 | tee $(LOGDIR)/surfaceFeatureExtract.log
	snappyHexMesh -overwrite 2>&1 | tee $(LOGDIR)/snappyHexMesh.log

solve:
	mkdir -p $(LOGDIR)
	#rm -rf processor*
	decomposePar -force 2>&1 | tee $(LOGDIR)/decomposePar.log
	export MPI_BUFFER_SIZE=1000000 && mpirun -np $(NPROCS) rhoSimpleFoam -parallel 2>&1 | tee $(LOGDIR)/rhoSimpleFoam.log
	#reconstructPar -latestTime 2>&1 | tee $(LOGDIR)/reconstructPar.log
	#rm -rf processor*

check:
	mkdir -p $(LOGDIR)
	export MPI_BUFFER_SIZE=1000000 && mpirun -np $(NPROCS) checkMesh -parallel 2>&1 | tee $(LOGDIR)/checkMesh.log

clean:
	rm -rf processor*
	rm -rf constant/extendedFeatureEdgeMesh
	rm -rf constant/polyMesh
	rm -rf constant/triSurface/*.eMesh
