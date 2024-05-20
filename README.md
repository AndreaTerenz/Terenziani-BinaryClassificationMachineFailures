# Terenziani-BinaryClassificationMachineFailures

Work done for the 2023/2024 Project Work in ML & Data Mining, using data from the [Kaggle challenge of the same name](https://www.kaggle.com/competitions/playground-series-s3e17)

## Project files

- `data.csv` is the dataset
- `BCMF.ipynb` is the notebook containing the code
- `cache/` is saved data that usually takes quite a long time to compute. All functions that access such data have arguments to manually regenerate such data. Specifically:
	- [pickle files](https://docs.python.org/3/library/pickle.html) storing the results of all grid searches, which are particularly slow to perform
	- pairplots

## Extra packages

The very strongly imbalanced dataset required performing oversampling, done using the [`imbalanced-learn`](https://imbalanced-learn.org/stable/) Python package. This has to be manually installed (see below).

## Before running

### Google Colab

1. Upload the `cache` folder and `data.csv` to Google Drive
	- If `cache` is omitted, it will be regenerated automatically
2. Uncomment the first three cells of the notebook to enable mounting a GDrive, remembering to put in the actual path to which you've uploaded the previous two folders
	- This will also install `imblearn`, the only required package not preinstalled in Colab

### On your PC

This project uses [pipenv](https://pipenv.pypa.io/en/latest/) to track its dependencies, listed in the included `Pipfile`, and at least Python 3.10 (though it hasn't been tested for lower versions - 3.10 is the one used by Colab but my laptop & desktop run 3.11).

1. Inside the project's root directory, run `pipenv install`
	- this will install the required packages and python version (if missing). Most importantly, it'll make sure to install scikit version *1.2.2*
	- this will output a name for the newly created environment (e.g., in my case "`BCMF-p3r9wMLm`")
2. Open the notebook with VSCode and click "Select kernel" > "Python environments", where you'll see (among others) the pipenv environment. Once selected, it'll be used automatically the next time you run the notebook.

