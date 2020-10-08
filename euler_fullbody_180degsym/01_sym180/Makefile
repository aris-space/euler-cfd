ifndef np
	np = 8
endif

LOGDIR = log
MPIRUN = export MPI_BUFFER_SIZE=10000000 && mpirun --oversubscribe -np $(np) 
# --oversubscribe 

mesh:
	mkdir -p $(LOGDIR)
	blockMesh 2>&1 | tee $(LOGDIR)/blockMesh.log
	surfaceFeatureExtract 2>&1 | tee $(LOGDIR)/surfaceFeatureExtract.log
	make decompose
	make shm
	reconstructParMesh -constant 2>&1 | tee $(LOGDIR)/reconstructParMesh.log
	#createPatch -overwrite 2>&1 | tee $(LOGDIR)/createPatch.log

decompose:
	mkdir -p $(LOGDIR)
	rm -rf processor*
	cp system/decomposeParDict_$(np) system/decomposeParDict
	decomposePar 2>&1 | tee $(LOGDIR)/decomposePar.log

shm:
	mkdir -p $(LOGDIR)
	$(MPIRUN) snappyHexMesh -overwrite -parallel 2>&1 | tee $(LOGDIR)/snappyHexMesh.log

check:
	mkdir -p $(LOGDIR)
	checkMesh 2>&1 | tee $(LOGDIR)/checkMesh.log

solve:
	rm -rf 0
	cp -r 0_org 0
	mkdir -p $(LOGDIR)
	#setFields
	make decompose
	$(MPIRUN) rhoPimpleFoam -parallel 2>&1 | tee $(LOGDIR)/rhoPimpleFoam.log
	reconstructPar -constant 2>&1 | tee $(LOGDIR)/reconstructPar.log

clean:
	rm -rf processor*
	rm -rf constant/extendedFeatureEdgeMesh
	rm -rf constant/polyMesh
	rm -rf constant/triSurface/*.eMesh
	rm -rf *.obj
	rm -rf 0 0.* 1.* 2.* 3.* 4.* 5.*
	cp -r 0_org 0
