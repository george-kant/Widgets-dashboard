import json

def lambda_handler(event, context):
    body = json.loads(event["body"])

    weight_bmr = float(body.get("weight", 0.0))
    height_bmr = float(body.get("height", 0.0))
    age_bmr = int(body.get("age", 0))
    gender_bmr = body.get("gender", "")

    bmr_result = ""

    if weight_bmr <= 0 or height_bmr <= 0 or age_bmr <= 0 or gender_bmr not in ["Άνδρας", "Γυναίκα"]:
        bmr_result = ":loudspeaker: Παρακαλώ εισάγετε έγκυρες τιμές και δοκιμάστε ξανά."

    if gender_bmr == "Άνδρας":
        bmr = 10 * weight_bmr + 6.25 * height_bmr - 5 * age_bmr + 5
        bmr_result = f"H ενέργεια που καταναλώνει το σώμα σας σε ηρεμία: {bmr:.2f} θερμίδες."
    else:
        bmr = 10 * weight_bmr + 6.25 * height_bmr - 5 * age_bmr - 161
        bmr_result = f"H ενέργεια που καταναλώνει το σώμα σας σε ηρεμία: {bmr:.2f} θερμίδες."

    response = {
        "statusCode": 200,
        "body": json.dumps({
            "bmr_result": bmr_result
        })
    }

    return response