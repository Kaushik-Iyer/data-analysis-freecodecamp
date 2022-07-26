import numpy as np

def calculate(list):
  if len(list)!=9:
    print("List must contain nine numbers.")

  arr=np.array([[list[0],list[1],list[2]],
  [list[3],list[4],list[5]],
  [list[6],list[7],list[8]]])

  mean1=np.mean(arr,axis=0).tolist()
  mean2=np.mean(arr,axis=1).tolist()
  mean=np.mean(arr).tolist()
  var1=np.var(arr,axis=0).tolist()
  var2 = np.var(arr, axis=1).tolist()
  var=np.var(arr).tolist()
  std1=np.std(arr,axis=0).tolist()
  std2=np.std(arr,axis=1).tolist()
  std=np.std(arr).tolist()
  max1=np.max(arr,axis=0).tolist()
  max2 = np.max(arr, axis=1).tolist()
  max = np.max(arr).tolist()
  min1=np.min(arr,axis=0).tolist()
  min2 = np.min(arr, axis=1).tolist()
  min = np.min(arr).tolist()
  sum1=np.sum(arr,axis=0).tolist()
  sum2 = np.sum(arr, axis=1).tolist()
  sum = np.sum(arr).tolist()

  calculations = dict()
  calculations['mean']=[mean1,mean2,mean]
  calculations['variance']=[var1,var2,var]
  calculations['standard deviation']=[std1,std2,std]
  calculations['max']=[max1,max2,max]
  calculations['min']=[min1,min2,min]
  calculations['sum']=[sum1,sum2,sum]

  return calculations