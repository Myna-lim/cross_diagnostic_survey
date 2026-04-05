# cross_diagnostic_survey
# Reproducibility Files for Final Lockbox Evaluation

This repository provides the files required to reproduce the final lockbox performance of the trained CatBoost models for the paper, “One item per disorder: a cross-diagnostic optimization framework for simultaneous prediction of six psychiatric disorders.” The study introduces a cross-diagnostic survey reduction framework that enables accurate multi-disorder prediction using a minimal set of representative items.

---

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

This notebook loads the final selected features, trained CatBoost models, and lockbox evaluation data to reproduce the reported model performance.

The notebook generates a performance table containing:

- AUROC  
- AUPRC  
- Accuracy  

It also reports macro-averaged performance across all six disorder prediction models.

---

## File description

- `public_performance.ipynb`: Reproduces final lockbox performance using trained CatBoost models  
- `lockbox_X_final.csv`: Final lockbox feature matrix (selected items + covariates)  
- `lockbox_Y.csv`: Lockbox labels for six psychiatric outcomes  
- `final_selected_items.txt`: Final selected representative items (one per disorder)  
- `final_best_params.pkl`: Final hyperparameters used for model training  

### Trained models

- `catboost_DSI_final.pkl`: DSI-SS model  
- `catboost_PHQ_final.pkl`: PHQ-9 model  
- `catboost_GAD_final.pkl`: GAD-7 model  
- `catboost_PCL_final.pkl`: PCL-5 model  
- `catboost_PDSS_final.pkl`: PDSS model  
- `catboost_AUDIT_final.pkl`: AUDIT model  

---

## Label description (`lockbox_Y.csv`)

- `DSI_group`: Suicidality (DSI-SS)  
- `PHQ_group`: Depression (PHQ-9)  
- `GAD_group`: Anxiety (GAD-7)  
- `PCL_group`: PTSD (PCL-5)  
- `PDSS_group`: Panic disorder (PDSS)  
- `AUDIT_group`: Alcohol use (AUDIT)  

---

## Feature description (`lockbox_X_final.csv`)

This file contains:

- One selected representative item from each psychiatric instrument  
- Covariates: `Sex`, `Age`  

The exact selected items are listed in `final_selected_items.txt`.

---

## Required packages

This repository was developed using Python 3 and Jupyter Notebook.

Required packages:

- pandas  
- numpy  
- joblib  
- scikit-learn  
- catboost  

---

## Expected outcome and run time

`public_performance.ipynb` performs inference only and does not include model training.

It:

- Loads final data and models  
- Computes predicted probabilities  
- Reproduces AUROC, AUPRC, and Accuracy  

Execution time is minimal and depends on system specifications.

---

## Development-stage files (encrypted archive)

An encrypted archive containing development-stage materials is included in this repository:

- `development_final_survey.zip`

This archive is password-protected and is **not required** to reproduce the final results presented in this repository.

### Contents of the encrypted archive

The archive includes the files used during the development stage:

- `development_final_survey.ipynb`  
  → Full pipeline for survey item selection, bootstrap optimization, and hyperparameter tuning  

- `dev_train_folds1to3_data.csv`  
- `dev_train_folds1to3_labels.csv`  
  → Development training set used for item selection  

- `dev_val_fold4_data.csv`  
- `dev_val_fold4_labels.csv`  
  → Validation set used for hyperparameter tuning  

- `dev_test_fold5_data.csv`  
- `dev_test_fold5_labels.csv`  
  → Internal test set used for model selection  

### Access

The archive is encrypted and the password is not publicly distributed.

Access can be provided by the authors upon reasonable request.

---

## Notes

This repository is designed to reproduce the final model performance on the lockbox dataset only.

The development-stage pipeline is separated to:

- maintain clarity of the reproducibility workflow  
- prevent data leakage between development and evaluation stages  
- align with standard practices for machine learning reproducibility  

---

## Reference

[Authors]. *One item per disorder: a cross-diagnostic optimization framework for simultaneous prediction of six psychiatric disorders.* (Under review / In submission).

For questions regarding the development pipeline or access to encrypted materials, please contact the corresponding author.
