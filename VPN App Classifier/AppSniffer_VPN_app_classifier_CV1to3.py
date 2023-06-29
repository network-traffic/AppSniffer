from autogluon.tabular import TabularDataset, TabularPredictor
from sklearn.metrics import classification_report
import pandas as pd

"""# **2. CV 1 to 3**"""

### Change dataset (e.g., Normal, SuperVPN, NordVPN, TurboVPN, or Surfshark)
dataset = "TurboVPN"

result_txt = open(f"result_{dataset}.txt", 'w')

### each number in [] is average packet length in train set ### 
#for cv_count, cutting_size in zip(range(1, 4), [96, 96, 96]): #normal
#for cv_count, cutting_size in zip(range(1, 4), [2621, 2605, 2670]) #NordVPN:
#for cv_count, cutting_size in zip(range(1, 4), [3438, 3433, 3410]) #SuperVPN:
#for cv_count, cutting_size in zip(range(1, 4), [1647, 1649, 1643]):#Surfshark
for cv_count, cutting_size in zip(range(1, 4), [4226, 4224, 4213]):#TurboVPN
  df_train = pd.read_csv(f'{dataset}_CV_{cv_count}_train_10000.csv', )
  df_test = pd.read_csv(f'{dataset}_CV_{cv_count}_test_10000.csv', )
  ### During CV 1 to 3, for the validation set, we use a fold of the validation set called CV4_test. ###
  ### This set is not certainly included in any set of train or test set in CV1 to CV3 ###
  df_valid = pd.read_csv(f'{dataset}_CV_4_test_10000.csv', )

  title_small = []

  for i in range(cutting_size):
    title_small.append(str(i))

  df_train[title_small] = (df_train['Packet_Length_Sequence'].str.split(' ', expand=True)).drop(list(range(cutting_size, 10000)), axis='columns')
  df_test[title_small] = (df_test['Packet_Length_Sequence'].str.split(' ', expand=True)).drop(list(range(cutting_size, 10000)), axis='columns')
  df_valid[title_small] = (df_valid['Packet_Length_Sequence'].str.split(' ', expand=True)).drop(list(range(cutting_size, 10000)), axis='columns')

  df_train = df_train.drop(labels=['Packet_Length_Sequence'], axis='columns')   
  df_test = df_test.drop(labels=['Packet_Length_Sequence'], axis='columns')   
  df_valid = df_valid.drop(labels=['Packet_Length_Sequence'], axis='columns')   

  print(df_train)

  save_path = './ag_models/'

  predictor = TabularPredictor(label="Label", problem_type='multiclass', eval_metric='f1_weighted', path=save_path).fit(df_train, tuning_data=df_valid, time_limit=600)

  results = predictor.fit_summary(show_plot=True)

  y_test = df_test['Label']    
  df_test = df_test.drop(labels=['Label'], axis=1)   
  y_pred = predictor.predict(df_test)
  y_pred_prob = predictor.predict_proba(df_test)
  print(y_pred_prob)
  perf = predictor.evaluate_predictions(y_true=y_test, y_pred=y_pred, auxiliary_metrics=True)
  labels_100 = [int(i) for i in range(150)]
  print(classification_report(y_test, y_pred, labels=labels_100, digits=4))

  result_txt.write(f"CV & Cutting_size : {cv_count} & {cutting_size}\n")
  result_txt.write(classification_report(y_test, y_pred, labels=labels_100, digits=4))
 
result_txt.close()

