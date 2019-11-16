import logging

import azure.functions as func
import pandas as pd
import joblib
import json

clf = joblib.load('titanic_model_pipe.pkl')

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    data = req.get_json()
    data = json.loads(data)

    if data is not None:

        response = []
        for i in range(len(data)):

            data_row = data[i]
            pred_df = pd.DataFrame([data_row])
            pred_label = clf.predict(pred_df)[0]
            pred_probs = clf.predict_proba(pred_df)[0]

            results_dict = {
                'pred_label': int(pred_label),
                'pred_prob_0': pred_probs[0],
                'pred_prob_1': pred_probs[1]
            }

            response.append(results_dict)

        return json.dumps(response)

    else:
        return func.HttpResponse(
             "Please pass a properly formatted JSON object to the API",
             status_code=400
        )
