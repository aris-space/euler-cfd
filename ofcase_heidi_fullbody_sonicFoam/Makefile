NPROCS = 16
LOGDIR = log
BUFSIZE = 1000000
MPI = export MPI_BUFFER_SIZE=$(BUFSIZE) && mpirun

.PHONY: sim mesh check clean

.PHONY: list
list:
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

sim:
	decomposePar 2>&1 | tee $(LOGDIR)/decomposePar_sim.log
	$(MPI) -np $(NPROCS) renumberMesh -overwrite -parallel 2>&1 | tee $(LOGDIR)/renumberMesh.log
	$(MPI) -np $(NPROCS) sonicFoam -parallel 2>&1 | tee $(LOGDIR)/sonicFoam.log
	reconstructPar -latestTime 2>&1 | tee $(LOGDIR)/reconstructPar.log

mesh:
	mkdir -p $(LOGDIR)
	blockMesh 2>&1 | tee $(LOGDIR)/blockMesh.log
	surfaceFeatureExtract 2>&1 | tee $(LOGDIR)/surfaceFeatureExtract.log
	decomposePar 2>&1 | tee $(LOGDIR)/decomposePar_mesh.log
	$(MPI) -np $(NPROCS) snappyHexMesh -overwrite -parallel 2>&1 | tee $(LOGDIR)/snappyHexMesh.log
	reconstructParMesh -constant 2>&1 | tee $(LOGDIR)/reconstructParMesh.log

check:
	mkdir -p $(LOGDIR)
	checkMesh 2>&1 | tee $(LOGDIR)/checkMesh.log

cleanprocs:
	rm -rf processor*

clean:
	rm -rf 0.*/
	rm -rf processor*
	rm -rf constant/extendedFeatureEdgeMesh
	rm -rf constant/polyMesh
	rm -rf constant/triSurface/*.eMesh
