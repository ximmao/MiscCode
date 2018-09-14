import numpy as np

def F1ScorRandom(dataSet_X, dataSet_Y):
    TP = 0
    FP = 0
    FN = 0
    TN = 0
    for index in range(dataSet_X.shape[0]):
        predicted_class = np.random.randint(2) + 1
        true_class = dataSet_Y[index]
        if predicted_class == 0 and true_class == 0:
            TN += 1
        if predicted_class == 1 and true_class == 1:
            TP += 1
        if predicted_class == 0 and true_class == 1:
            FN += 1
        if predicted_class == 1 and true_class == 0:
            FP += 1
    precision = TP / (TP + FP)
    recall = TP / (TP + FN)
    F1_score = 2* precision * recall / (precision + recall)
    print(F1_score)
    return F1_score
