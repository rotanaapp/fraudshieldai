import joblib
import pandas as pd


def load_model_and_encoder():
    model = joblib.load("fraud_detection_model.jb")
    encoder = joblib.load("label_encoder.jb")
    return model, encoder


def predict_fraud(
    model, encoder, merchant, category, amt, distance, hour, day, month, gender, cc_num
):
    df = pd.DataFrame(
        [
            [
                merchant,
                category,
                amt,
                distance,
                hour,
                day,
                month,
                gender,
                cc_num,
            ]
        ],
        columns=[
            "merchant",
            "category",
            "amt",
            "distance",
            "hour",
            "day",
            "month",
            "gender",
            "cc_num",
        ],
    )
    for col in ["merchant", "category", "gender"]:
        try:
            df[col] = encoder[col].transform(df[col])
        except:
            df[col] = -1

    df["cc_num"] = df["cc_num"].apply(lambda x: hash(x) % 100)
    prediction = model.predict(df)[0]
    return (
        "🚨 Fraudulent Transaction" if prediction == 1 else "✅ Legitimate Transaction"
    )
