
# Entropy Calculation ->

entropy = sum([
    -count / len(x_ids) * math.log(count / len(x_ids), 2)
    if count else 0
    for count in label_count
])

# Information Gain Calculation ->
info_gain = self._get_entropy(x_ids) - sum([val_counts / len(x_ids) * self._get_entropy(val_ids)
                                     for val_counts, val_ids in zip(feature_vals_count, feature_vals_id)])

FEATURE_COLS = ["age","gender","ethnicity","education_level","income_level","employment_status","smoking_status","alcohol_consumption_per_week","physical_activity_minutes_per_week","diet_score","sleep_hours_per_day","screen_time_hours_per_day","family_history_diabetes","hypertension_history","cardiovascular_history","bmi","waist_to_hip_ratio","systolic_bp","diastolic_bp","heart_rate","cholesterol_total","hdl_cholesterol","ldl_cholesterol","triglycerides","glucose_fasting","glucose_postprandial","insulin_level","hba1c","diabetes_risk_score"]
class DecisionTree():

    def __init__(self, features, labels):
        # Information
        self.data= features
        self.results= lables         

        # Composed Information
        self.labelCatergories= list(set(labe_cols))
        self.labelCategoriesCount= [list(labels).count(x) for x in self.labelCategories]

        # We don't stablish any Parent Node (yet?)
        self.node= None

        self.entropy= self._get_entropy([x for x in range(len(self.labels))]) #There must be a better way
