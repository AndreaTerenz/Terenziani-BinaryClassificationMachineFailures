# Terenziani-Binary classification of machine failures

Work done for the 2023/2024 Project Work in ML & Data Mining, using data from the [Kaggle challenge of the same name](https://www.kaggle.com/competitions/playground-series-s3e17).

The data consisted in a set of various industrial devices, each described through attributes like torque or operating temperature, that did or did not suffer some kind of failure (class 1 and 0, respectively). The task was therefore a binary classification, which was done through several different models, from decision trees to a support vector machine. In the end, there were actually two best performing estimators:
- a *random forest* model, with an average recall of 89% and a class 1 recall of 84%.
- a *support vector machine* model, with an average recall of 88% and a class 1 recall of 85%.
However, due to the latter being a few orders of magnitude slower to train, the former may be considered the best model. 

The main issue with the data is its extreme imbalance between majority and minority class. As shown in the notebook, this is solved by oversampling the minority class, and by choosing an appropriate metric for tuning (specifically, the recall macro average, which required good performance for both classes).
