# Azure Machine Learning

## Getting Started

tutorials: <https://learn.microsoft.com/en-us/azure/machine-learning/?view=azureml-api-2>

## Notebooks

Use `%pip` and `%conda` magic commands to install against the current kernel.

Creating an environment:

see <https://learn.microsoft.com/en-us/azure/machine-learning/tutorial-cloud-workstation?view=azureml-api-2#set-up-a-new-environment-for-prototyping-optional>

* create a `.yml` conda env description
* open terminal
    * `conda env list`
    * `conda env create -f NAME.yml`
    * `conda activate ENV_NAME`
    * `python -m ipykernel install --user --name ENV_NAME --display-name "ENV NAME"`

## Using Git

<https://learn.microsoft.com/en-us/azure/machine-learning/concept-train-model-git-integration>

Need to set up git per compute instance.

Store git info in `/home/azureuser/.ssh` which is local to the compute instance (not shared).
