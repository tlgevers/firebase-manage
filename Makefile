
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

firebaseconfig: ## get firebase config, set project_id=<project id>
	echo "create firebase-config.json for ${project_id}"
	export PROJECT_ID=${project_id}
	pipenv shell
	pip install -r requirements.txt
	python main.py --action=getConfig

