import pandas as pd 
import numpy as np 
import typing

import math


# Information Gain Calculation ->

FEATURE_COLS= ["age","gender","ethnicity","education_level","income_level","employment_status","smoking_status","alcohol_consumption_per_week","physical_activity_minutes_per_week","diet_score","sleep_hours_per_day","screen_time_hours_per_day","family_history_diabetes","hypertension_history","cardiovascular_history","bmi","waist_to_hip_ratio","systolic_bp","diastolic_bp","heart_rate","cholesterol_total","hdl_cholesterol","ldl_cholesterol","triglycerides","glucose_fasting","glucose_postprandial","insulin_level","hba1c"]
FEATURE_DICT= dict(enumerate(FEATURE_COLS))
LABEL_COLS= ["diabetes_risk_score"]

class Node():
    def __init__(self):
        self.value = None
        self.next = None
        self.childs = None

class DecisionTree():

    def __init__(self, database: pd.DataFrame):
        # Information
        self.data= np.array(database.drop(LABEL_COLS, axis=1).copy())
        self.results= np.array(database[FEATURE_COLS].copy())
        self.length= np.shape(self.results)[0]         

        # Patterns
        uniques, counts= np.unique(results, return_counts= True)
        self.frequency= dict(zip(uniques, counts))

        # We don't stablish any Parent Node (yet?)
        self.node= None

        self.entropy= self._get_entropy() #There must be a better way

    def _calculate_entropy(self, indices: list, value: str= None) -> float:
 
        if indices:
            # Acotamos Nuestros Datos - Indices Totales
            newdata= self.data[indices]
            newresults= self.results[indices]
        else:
            newdata= self.data
            newresults= self.results

        if value:
            # Conseguimos lineas con el valor - Indices Relativos
            indices_value= np.where(np.any(predata== value, axis=1))[0]
            
            # Conseguimos los datos con los que trabajamos
            newdata= predata[indices_value]
            newresults= preresults[indices_value]

        newlength= np.shape(newresults)[0]

        uniques, counts= np.unique(newresults, return_counts= True)
        newfrequency= dict(zip(uniques, counts))

        return sum([
            -count/ newlength* math.log(count/ newlength, 2)
            if count else 0
            for count in newfrequency.values
        ])


    def _info_gain(self, indices: list, feature: str):
        initial_entropy= _calculate_entropy(indices)
        data= self.data[indices]

        uniques, counts= np.unique(data[feature], return_counts=True)
        feature_frequencies= dict(zip(uniques, counts))

        return initial_entropy - sum([
            value_freq/ self.length* self._get_entropy(indices, value)
            for value, value_freq in feature_frequencies.items()
        ])

    def _get_max_info(self, indices: list, features: list):


        gain_per_feature= [self._info_gain(indices, feature_col) for feature_col in features]

        max_feature = gain_per_feature.index(max(gain_per_feature))

        return (FEATURE_DICT[max_feature], max_feature)

    def _entrenamiento(self, indices, features, node):
        node= Node() if node==None else ...

        newdata= self.data[indices]
        newresults= self.results[indices]

        if len(set(newresults)) == 1:
            node.value = newresults[0]
            return node
        
        if len(feature_ids) == 0:
            node.value = max(set(newresults), key=newresults.count)  # compute mode
            return node


        best_name, best_col= self._get_max_info(indices, features)
        node.value= best_name
        node.childs= []

        # value of the chosen feature for each instance
        feature_values = list(set(
                [self.data[i][best_col]
                 for i in indices
                 ]))

        for value in feature_values:
            child = Node()
            child.value = value  # add a branch from the node to each feature value in our feature
            node.childs.append(child)  # append new child node to current node
            
            childs_indices = [i 
            for i in indices 
            if self.data[i][best_col] == value]

            if not childs_indices:
                child.next = max(set(newresults), key=newresults.count)
                print('')

            else:
                if features and best_col in features:
                    to_remove = features.index(best_col)
                    features.pop(to_remove)
                # recursively call the algorithm
                child.next = self._id3_recv(childs_indices, features, child.next)
        return node
                 