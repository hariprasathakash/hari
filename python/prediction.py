

#import requests 
from flask import Flask,request,jsonify
from sklearn import *
from math import sqrt
from sklearn.metrics import mean_squared_error
import numpy as np
import pandas as pd
from flask_cors import CORS
import statsmodels.api as sm
from datetime import datetime

app=Flask(__name__)
CORS(app)



@app.route("/getPredictions/", methods=["POST"])
def postPrediction():
    title = request.form.get('title')
    file = request.files['file']
    file.save('dataset/dataset.csv')
    predictColumn = request.form.get('predictColumn')
    periodicity = request.form.get('periodicity')
    numbericalValue = request.form.get('numbericalValue')
    print("sssssssssss",predictColumn,periodicity,numbericalValue)
 

    if (periodicity == 'Yearly'):
        freq = 'Y'
    elif (periodicity == 'Monthly'):
        freq = 'M'
    elif (periodicity == 'Weekly'):
        freq = 'W'
    else:
        freq = 'D'
    with open('dataset/sales.csv') as f1:

        data = pd.read_csv(f1 )
        data['date'] = pd.to_datetime(data['date'])
        data.sort_values(by=['date'], inplace=True)
        data.set_index('date', inplace=True)

        # Resampling the data according to the selected periodicity
        new_data = pd.DataFrame(data[predictColumn])
        new_data = pd.DataFrame(new_data[predictColumn].resample(freq).mean())
        new_data = new_data.interpolate(method='linear')

        # Splitting the data into train, test, and validation sets
        train, test, validation = np.split(new_data[predictColumn].sample(frac=1), [int(.6 * len(new_data[predictColumn])), int(.8 * len(new_data[predictColumn]))])
        # SARIMA MODEL
        mod = sm.tsa.statespace.SARIMAX(new_data,
                                        order=(1, 1, 1),
                                        seasonal_order=(1, 1, 1, 12),
                                        enforce_invertibility=False)
        results = mod.fit()
        pred = results.get_prediction()

        pred.conf_int()
        y_forecasted = pred.predicted_mean
        y_truth = new_data[predictColumn]

        mse = mean_squared_error(y_truth, y_forecasted)
        rmse = sqrt(mse)
        mae = metrics.mean_absolute_error(y_forecasted, y_truth)
        mape = metrics.mean_absolute_percentage_error(y_truth, y_forecasted)
        mape = round(mape * 100, 2)

        forecast = results.forecast(steps=int(numbericalValue))
        forecast = forecast.astype('int')
        forecast_df = forecast.to_frame()
        forecast_df.reset_index(level=0, inplace=True)
        forecast_df.columns = ['PredictionDate', 'PredictedColumn']

        frame = pd.DataFrame(forecast_df)
        frameDict = frame.to_dict('records')

        predicted_date = []
        predicted_column = []
        for i in range(0, len(frameDict)):
            predicted_column.append(frameDict[i]['PredictedColumn'])
            tempStr = str(frameDict[i]['PredictionDate'])
            dt = datetime.strptime(tempStr, '%Y-%m-%d %H:%M:%S')
            predicted_date.append(dt.strftime('%A')[0:3] + ', ' + str(dt.day) + ' ' + dt.strftime("%b")[0:3] + ' ' + str(dt.year))



        prediction = frame.to_csv('dataset/d1.csv', index=False)
        #print(type(frame))
        #print(predicted_date,predicted_column)
        response=[]
        for i in range(len(predicted_date)):
            response.append({"date":predicted_date[i],"coloum":predicted_column[i]})
        print(response)
        print(len(response))
        return jsonify(response)
        # dfd = pd.read_csv('dataset/d1.csv')
        # print(dfd)
        #print(prediction)
        #return jsonify(data="Predicted")

# postPrediction("HI")

if __name__=="__main__":
    app.run(debug=True)