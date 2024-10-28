import json

def lambda_handler(event, context):
    body = json.loads(event["body"])
    
    weight_tdee = float(body["weight"])
    height_tdee = float(body["height"])
    age_tdee = int(body["age"])
    gender_tdee = body["gender"]
    activity_level_tdee = body["activity_level"]

    activity_factors = {
        "Καθιστική ζωή": 1.2,
        "Ελαφριά δραστηριότητα": 1.375,
        "Μέτρια δραστηριότητα": 1.55,
        "Υψηλή δραστηριότητα": 1.725,
        "Πολύ υψηλή δραστηριότητα": 1.9
    }
    
    if gender_tdee == "Άνδρας":
        bmr_tdee = 10 * weight_tdee + 6.25 * height_tdee - 5 * age_tdee + 5
    else:
        bmr_tdee = 10 * weight_tdee + 6.25 * height_tdee - 5 * age_tdee - 161
    
    total_calories = bmr_tdee * activity_factors[activity_level_tdee]

    response = {
        "statusCode": 200,
        "body": json.dumps({
            "tdee_result": f"Πρέπει να καταναλώνετε περίπου {total_calories:.2f} θερμίδες την ημέρα."
        })
    }

    return response
