import pandas as pd 
import numpy as np 
import typing

import math


# Information Gain Calculation ->

FEATURE_COLS= ["age","gender","ethnicity","education_level","income_level","employment_status","smoking_status","alcohol_consumption_per_week","physical_activity_minutes_per_week","diet_score","sleep_hours_per_day","screen_time_hours_per_day","family_history_diabetes","hypertension_history","cardiovascular_history","bmi","waist_to_hip_ratio","systolic_bp","diastolic_bp","heart_rate","cholesterol_total","hdl_cholesterol","ldl_cholesterol","triglycerides","glucose_fasting","glucose_postprandial","insulin_level","hba1c"]
LABEL_COLS= ["diabetes_risk_score"]

class DecisionTree():

    def __init__(self, database: pd.DataFrame):
        # Information
        self.database= database
        self.data= np.array(database.drop(LABEL_COLS, axis=1).copy())
        self.results= np.array(database[FEATURE_COLS].copy())
        self.length= np.shape(self.results)[0]         

        # Patterns
        uniques, counts= np.unique(results, return_counts= True)
        self.frequency= dict(zip(uniques, counts))

        # We don't stablish any Parent Node (yet?)
        self.node= None

        self.entropy= self._get_entropy() #There must be a better way

    def _calculate_entropy(self, value: str= None) -> float:
        if value== None:
            return sum([
                -count/ self.length* math.log(count/ self.length, 2)
                if count else 0
                for count in self.frequency.values
            ])
        else:
            indices= np.where(np.any(self.data== value, axis=1))[0]
            
            newdata= self.data[indices]
            newresults= self.results[indices]

            newlength= np.shape(newresults)[0]

            uniques, counts= np.unique(newresults, return_counts= True)
            newfrequency= dict(zip(uniques, counts))

            return sum([
                -count/ newlength* math.log(count/ newlength, 2)
                if count else 0
                for count in newfrequency.values
            ])


    def _info_gain(self, feature: str):
        initial_entropy= _calculate_entropy()

        uniques, counts= np.unique(results[feature], return_counts=True)
        feature_frequencies= dict(zip(uniques, counts))

        return initial_entropy - sum([
            value_freq/ self.length* self._get_entropy(value)
            for value, value_freq in feature_frequencies.items()
        ])