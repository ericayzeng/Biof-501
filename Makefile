DOCKER_IMAGE=ericayzeng/nf-image:latest
WORKFLOW=workflow.nf
DOCKERFILE=./Dockerfile

run:
	@nextflow run $(WORKFLOW) -with-docker

.PHONY: build-image
build-image:
	@echo "Building Docker image: $(DOCKER_IMAGE)"
	@docker build -t $(DOCKER_IMAGE) -f $(DOCKERFILE) .

.PHONY: clean
clean:
	@echo "Removing generated files"
	@-rm -rf work/
	@-rm -f .nextflow.log*
	@-rm -rf .nextflow/