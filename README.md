# cross_diagnostic_survey
# Reproducibility Files for Final Lockbox Evaluation

This repository provides the files for reproducing the final lockbox performance of the trained CatBoost models for the paper, “One item per disorder: a cross-diagnostic optimization framework for simulatneous prediction of six psychiatric disorders” which presents a cross-diagnostic survey reduction framework for multi-disorder prediction.

## User guide

### Estimating cross-diagnostic outcomes with the trained CatBoost models

#### Download required files

Obtain the following files:

- `public_performance.ipynb`
- `lockbox_X_final.csv`
- `lockbox_Y.csv`
- `final_selected_items.txt`
- `final_best_params.pkl`
- `catboost_DSI_final.pkl`
- `catboost_PHQ_final.pkl`
- `catboost_GAD_final.pkl`
- `catboost_PCL_final.pkl`
- `catboost_PDSS_final.pkl`
- `catboost_AUDIT_final.pkl`

Place all of these files in the same directory.

#### Run Jupyter Notebook

Open the `public_performance.ipynb` file in Jupyter Notebook.

Execute each cell in sequence.

This notebook will load the final selected features, the saved CatBoost models, and the final lockbox input data, and will reproduce the performance of the trained models on the lockbox dataset.

The notebook will generate a performance table containing the following metrics for each disorder:

- AUROC
- AUPRC
- Accuracy

It will also report the macro-averaged performance across all six disorder prediction models.

---

## File description

- `public_performance.ipynb`: Jupyter notebook for reproducing the final lockbox performance using the trained CatBoost models
- `lockbox_X_final.csv`: final lockbox feature matrix used for model evaluation; this file includes only the selected survey items and covariates used in the final models
- `lockbox_Y.csv`: lockbox label file containing the binary outcome variables for the six target disorders
- `final_selected_items.txt`: text file listing the final selected survey items used in the final cross-diagnostic model
- `final_best_params.pkl`: saved hyperparameter set used for final model training
- `catboost_DSI_final.pkl`: trained CatBoost model for DSI-SS outcome prediction
- `catboost_PHQ_final.pkl`: trained CatBoost model for PHQ-9 outcome prediction
- `catboost_GAD_final.pkl`: trained CatBoost model for GAD-7 outcome prediction
- `catboost_PCL_final.pkl`: trained CatBoost model for PCL-5 outcome prediction
- `catboost_PDSS_final.pkl`: trained CatBoost model for PDSS outcome prediction
- `catboost_AUDIT_final.pkl`: trained CatBoost model for AUDIT outcome prediction

### Label description in `lockbox_Y.csv`

This file contains the following binary outcome columns:

- `DSI_group`: DSI-SS screening outcome
- `PHQ_group`: PHQ-9 screening outcome
- `GAD_group`: GAD-7 screening outcome
- `PCL_group`: PCL-5 screening outcome
- `PDSS_group`: PDSS screening outcome
- `AUDIT_group`: AUDIT screening outcome

### Feature description in `lockbox_X_final.csv`

This file contains the final selected survey items and covariates used in the trained models. These include:

- one selected representative item from each psychiatric instrument
- `Sex`
- `Age`

The exact selected item names are listed in `final_selected_items.txt`.

---

## Required packages

This repository was prepared using Python 3 and Jupyter Notebook.

Required Python packages:

- `pandas`
- `numpy`
- `joblib`
- `scikit-learn`
- `catboost`

All files can be executed if the user has installed Python 3, Jupyter Notebook, and the required Python packages listed above.

---

## Expected outcome and run time

`public_performance.ipynb` consists of a small number of cells for:

- loading the final lockbox data
- loading the trained CatBoost models
- calculating predicted probabilities
- reproducing AUROC, AUPRC, and Accuracy for each disorder

Run time depends on the user environment and hardware, but the notebook is expected to run quickly because it performs inference only and does not repeat model development or hyperparameter tuning.

---

## Notes on private development files

This public repository is intended only to reproduce the final model performance on the final prepared lockbox evaluation files.

The notebook used during the development stage for survey item reduction, bootstrap-based item selection, and hyperparameter selection is not included in the public repository.

The following files were used only during the development stage and are maintained privately:

- `development_final_survey.ipynb`
- `dev_train_folds1to3_data.csv`
- `dev_train_folds1to3_labels.csv`
- `dev_val_fold4_data.csv`
- `dev_val_fold4_labels.csv`
- `dev_test_fold5_data.csv`
- `dev_test_fold5_labels.csv`
- intermediate bootstrap and item-selection outputs, if applicable

These private development-stage files are not required to run the public notebook or reproduce the final reported lockbox performance.

---

## Reference

This repository contains the files necessary to reproduce the final performance of the trained models using the final prepared lockbox data and saved CatBoost models.

For questions regarding the development-stage item selection pipeline or access to private intermediate files, please contact the corresponding author.


