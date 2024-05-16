## Decision Tree

### Baseline(s)

#### Original dataset

![](DT/baseline.png)
```
Classification report:
              precision    recall  f1-score   support

           0       0.99      0.99      0.99     26841
           1       0.31      0.38      0.34       382

    accuracy                           0.98     27223
   macro avg       0.65      0.68      0.66     27223
weighted avg       0.98      0.98      0.98     27223

Best parameters:
	ccp_alpha: 0.0
	class_weight: None
	criterion: gini
	max_depth: None
	max_features: None
	max_leaf_nodes: None
	min_impurity_decrease: 0.0
	min_samples_leaf: 1
	min_samples_split: 2
	min_weight_fraction_leaf: 0.0
	random_state: 69420
	splitter: best

Feature importances:
	id: 0.188
	Air temperature [K]: 0.150
	Process temperature [K]: 0.121
	Rotational speed [rpm]: 0.162
	Torque [Nm]: 0.231
	Tool wear [min]: 0.149
```

#### Resampled dataset

![](DT/resampled.png)
```
Classification report:
              precision    recall  f1-score   support

           0       0.99      0.96      0.98     26841
           1       0.15      0.44      0.22       382

    accuracy                           0.96     27223
   macro avg       0.57      0.70      0.60     27223
weighted avg       0.98      0.96      0.97     27223

Best parameters:
	ccp_alpha: 0.0
	class_weight: None
	criterion: gini
	max_depth: None
	max_features: None
	max_leaf_nodes: None
	min_impurity_decrease: 0.0
	min_samples_leaf: 1
	min_samples_split: 2
	min_weight_fraction_leaf: 0.0
	random_state: 69420
	splitter: best

Feature importances:
	id: 0.117
	Air temperature [K]: 0.175
	Process temperature [K]: 0.143
	Rotational speed [rpm]: 0.156
	Torque [Nm]: 0.294
	Tool wear [min]: 0.115
```

### GridSearch

#### `Precision_macro`
![](DT/pmacro_gridsearch.png)
```
--------------------
Score: precision_macro
Classification report:
              precision    recall  f1-score   support

           0       0.99      0.99      0.99     26841
           1       0.32      0.49      0.39       382

    accuracy                           0.98     27223
   macro avg       0.66      0.74      0.69     27223
weighted avg       0.98      0.98      0.98     27223

Best parameters:
	ccp_alpha: 0.0
	class_weight: None
	criterion: gini
	max_depth: 10
	max_features: None
	max_leaf_nodes: None
	min_impurity_decrease: 0.0
	min_samples_leaf: 1
	min_samples_split: 2
	min_weight_fraction_leaf: 0.0
	random_state: 69420
	splitter: best

Feature importances:
	id: 0.029
	Air temperature [K]: 0.190
	Process temperature [K]: 0.094
	Rotational speed [rpm]: 0.157
	Torque [Nm]: 0.433
	Tool wear [min]: 0.098
```
#### `Recall_macro`
![](DT/rmacro_gridsearch.png)
```
--------------------
Score: recall_macro
Classification report:
              precision    recall  f1-score   support

           0       1.00      0.89      0.94     26841
           1       0.08      0.72      0.15       382

    accuracy                           0.88     27223
   macro avg       0.54      0.80      0.54     27223
weighted avg       0.98      0.88      0.93     27223

Best parameters:
	ccp_alpha: 0.0
	class_weight: balanced
	criterion: gini
	max_depth: 10
	max_features: None
	max_leaf_nodes: None
	min_impurity_decrease: 0.0
	min_samples_leaf: 1
	min_samples_split: 2
	min_weight_fraction_leaf: 0.0
	random_state: 69420
	splitter: best

Feature importances:
	id: 0.026
	Air temperature [K]: 0.085
	Process temperature [K]: 0.059
	Rotational speed [rpm]: 0.194
	Torque [Nm]: 0.520
	Tool wear [min]: 0.115
```
#### `F1_macro`
![](DT/f1macro_gridsearch.png)
```
--------------------
Score: f1_macro
Classification report:
              precision    recall  f1-score   support

           0       0.99      0.98      0.98     26841
           1       0.19      0.41      0.26       382

    accuracy                           0.97     27223
   macro avg       0.59      0.69      0.62     27223
weighted avg       0.98      0.97      0.97     27223

Best parameters:
	ccp_alpha: 0.0
	class_weight: None
	criterion: entropy
	max_depth: 23
	max_features: None
	max_leaf_nodes: None
	min_impurity_decrease: 0.0
	min_samples_leaf: 1
	min_samples_split: 2
	min_weight_fraction_leaf: 0.0
	random_state: 69420
	splitter: best

Feature importances:
	id: 0.097
	Air temperature [K]: 0.171
	Process temperature [K]: 0.137
	Rotational speed [rpm]: 0.161
	Torque [Nm]: 0.313
	Tool wear [min]: 0.121
```
#### `Accuracy`
![](DT/accuracy_gridsearch.png)
```
--------------------
Score: accuracy
Classification report:
              precision    recall  f1-score   support

           0       0.99      0.98      0.99     26841
           1       0.24      0.43      0.30       382

    accuracy                           0.97     27223
   macro avg       0.61      0.70      0.65     27223
weighted avg       0.98      0.97      0.98     27223

Best parameters:
	ccp_alpha: 0.0
	class_weight: None
	criterion: entropy
	max_depth: 16
	max_features: None
	max_leaf_nodes: None
	min_impurity_decrease: 0.0
	min_samples_leaf: 1
	min_samples_split: 2
	min_weight_fraction_leaf: 0.0
	random_state: 69420
	splitter: best

Feature importances:
	id: 0.080
	Air temperature [K]: 0.162
	Process temperature [K]: 0.123
	Rotational speed [rpm]: 0.164
	Torque [Nm]: 0.351
	Tool wear [min]: 0.119
```