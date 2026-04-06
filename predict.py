{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "78a25036-2389-4aa6-9860-b55215d1dbbf",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
import pandas as pd
from decrypt_model import load_encrypted_model

def main():

    # 🔹 모든 모델 로드
    models = {
        "PHQ-9": load_encrypted_model("models/encrypted/catboost_PHQ_final.pkl.enc"),
        "GAD-7": load_encrypted_model("models/encrypted/catboost_GAD_final.pkl.enc"),
        "PCL-5": load_encrypted_model("models/encrypted/catboost_PCL_final.pkl.enc"),
        "PDSS": load_encrypted_model("models/encrypted/catboost_PDSS_final.pkl.enc"),
        "AUDIT": load_encrypted_model("models/encrypted/catboost_AUDIT_final.pkl.enc"),
        "DSI-SS": load_encrypted_model("models/encrypted/catboost_DSI_final.pkl.enc"),
    }

    # 🔹 입력 (cross-diagnostic input)
    X = pd.DataFrame([{
        "age": 30,
        "sex": 1,
        "PHQ5": 2,
        "GAD2": 1,
        "PCL2": 0,
        "PDSS2": 1,
        "AUDIT3": 2,
        "DSI2": 0
    }])

    # 🔹 모든 disorder 예측
    results = {}

    for name, model in models.items():
        pred = model.predict_proba(X)[:, 1]  # 확률 (binary classifier 기준)
        results[name] = float(pred[0])

    print("🔹 Cross-diagnostic risk profile:")
    for k, v in results.items():
        print(f"{k}: {v:.3f}")

if __name__ == "__main__":
    main()