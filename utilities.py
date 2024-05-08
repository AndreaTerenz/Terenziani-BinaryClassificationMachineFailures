import pandas as pd
from sklearn.model_selection import StratifiedKFold, GridSearchCV
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay, recall_score, accuracy_score

def grid_search(params, scores, base_model, Xtr, ytr, Xte, yte, n_splits=3, random_state=None):
    skf = StratifiedKFold(n_splits=n_splits, random_state=random_state, shuffle=True)
    results = {}

    if type(scores) == str:
        scores = [scores]

    for score in scores:
        print(f"Tuning hyperparameters for: AA{score}...")
        
        clf = GridSearchCV(estimator=base_model,
                        param_grid=params,
                        scoring=score,
                        return_train_score=False,
                        cv=skf, verbose=2)
        
        clf.fit(Xtr, ytr)
        
        best_model = clf.best_estimator_
        classes = best_model.classes_
        
        y_pred = best_model.predict(Xte)
        
        report = classification_report(yte,y_pred, zero_division=0)
        cm = confusion_matrix(yte, y_pred, labels=classes, normalize="true")

        results[score] = {
            "model": best_model,
            "report": report,
            "matrix": cm
        }

        print("done")

    return results

def print_model_results(model, report, conf_matrix, features, conf_matrix_title = ""):
    print("Classification report:")
    print(report)

    print(f"Best parameters:")
    print(*[f"\t{n}: {v}" for n, v in model.get_params().items()], sep="\n")

    print()

    print("Feature importances:")
    for i, imp in enumerate(model.feature_importances_):
        print(f"\t{features[i]}: {imp:.3f}")

    disp = ConfusionMatrixDisplay(conf_matrix, display_labels=model.classes_)
    disp.plot()
    
    if conf_matrix_title != "":
        disp.ax_.set_title(conf_matrix_title)
    disp.ax_.grid(False)

def print_gridsearch_results(results, features):
    for score, res in results.items():
        print("-" * 20)
        print(f"Score: {score}")

        print_model_results(res["model"], res["report"], res["matrix"], features, conf_matrix_title=f"Optimized for {score}")

def split_dataset(df: pd.DataFrame, target_col : str) -> tuple:
    """
    Split a dataset `df` into a dataframe of features `X` and a target column `y`, selecting it
    with `target_col`.

    Returns a tuple `(features dataframe, target column)`
    """

    X = df.drop(labels=target_col, axis=1)
    y = df[target_col]

    return X, y

def accu_recall_scorer(y_true, y_pred, min_accuracy):
    accuracy = accuracy_score(y_true, y_pred)
    recall_macro = recall_score(y_true, y_pred, average='macro')
    
    # Penalize if accuracy falls below 90%
    if accuracy < min_accuracy:
        return 0
    
    # Return recall_macro otherwise
    return recall_macro