NPROCS = 16
LOGDIR = log

.PHONY: sim mesh check clean

.PHONY: list
list:
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

sim:
	rm -rf processor*
	decomposePar 2>&1 | tee $(LOGDIR)/decomposePar_sim.log
	mpirun -np $(NPROCS) renumberMesh -overwrite -parallel 2>&1 | tee $(LOGDIR)/renumberMesh.log
	mpirun -np $(NPROCS) sonicFoam -parallel 2>&1 | tee $(LOGDIR)/sonicFoam.log
	reconstructPar -latestTime 2>&1 | tee $(LOGDIR)/reconstructPar.log

mesh:
	mkdir -p $(LOGDIR)
	blockMesh 2>&1 | tee $(LOGDIR)/blockMesh.log
	surfaceFeatureExtract 2>&1 | tee $(LOGDIR)/surfaceFeatureExtract.log
	decomposePar 2>&1 | tee $(LOGDIR)/decomposePar_mesh.log
	mpirun -np $(NPROCS) snappyHexMesh -overwrite -parallel 2>&1 | tee $(LOGDIR)/snappyHexMesh.log
	reconstructParMesh -constant 2>&1 | tee $(LOGDIR)/reconstructParMesh.log

check:
	mkdir -p $(LOGDIR)
	checkMesh 2>&1 | tee $(LOGDIR)/checkMesh.log

clean:
	rm -rf 0.*/
	rm -rf processor*
	rm -rf constant/extendedFeatureEdgeMesh
	rm -rf constant/polyMesh
	rm -rf constant/triSurface/*.eMesh
