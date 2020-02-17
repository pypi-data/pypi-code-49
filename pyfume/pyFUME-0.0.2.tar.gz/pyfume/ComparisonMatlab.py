from pyfume import *
import numpy as np

number_of_runs=20

RMSE_FCM=np.zeros([number_of_runs,1])
RMSE_PSO=np.zeros([number_of_runs,1])
RMSE_FCM_norm=np.zeros([number_of_runs,1])
RMSE_PSO_norm=np.zeros([number_of_runs,1])

for i in range(0,number_of_runs): 
    FIS = pyFUME(datapath='IPMU2020/NASA.csv', nr_clus=3, method='Takagi-Sugeno', cluster_method='fcm' )
    RMSE_FCM[i]=FIS.calculate_error().get('OUTPUT')
    
    FIS = pyFUME(datapath='IPMU2020/NASA.csv', nr_clus=3, method='Takagi-Sugeno', cluster_method='fstpso')
    RMSE_PSO[i]=FIS.calculate_error().get('OUTPUT')
    
    FIS = pyFUME(datapath='IPMU2020/NASA.csv', nr_clus=3, method='Takagi-Sugeno', cluster_method='fcm', normalize=True)
    RMSE_FCM_norm[i]=FIS.calculate_error().get('OUTPUT')
    
    FIS = pyFUME(datapath='IPMU2020/NASA.csv', nr_clus=3, method='Takagi-Sugeno', cluster_method='fstpso', normalize=True)
    RMSE_PSO_norm[i]=FIS.calculate_error().get('OUTPUT')
    
RMSE_FCM_and=np.zeros([number_of_runs,1])
RMSE_PSO_and=np.zeros([number_of_runs,1])
RMSE_FCM_norm_and=np.zeros([number_of_runs,1])
RMSE_PSO_norm_and=np.zeros([number_of_runs,1])    
    
for i in range(0,number_of_runs): 
    FIS = pyFUME(datapath='IPMU2020/NASA.csv', nr_clus=3, method='Takagi-Sugeno', cluster_method='fcm', operators='AND_PRODUCT')
    RMSE_FCM_and[i]=FIS.calculate_error().get('OUTPUT')
    
    FIS = pyFUME(datapath='IPMU2020/NASA.csv', nr_clus=3, method='Takagi-Sugeno', cluster_method='fstpso', operators='AND_PRODUCT')
    RMSE_PSO_and[i]=FIS.calculate_error().get('OUTPUT')
    
    FIS = pyFUME(datapath='IPMU2020/NASA.csv', nr_clus=3, method='Takagi-Sugeno', cluster_method='fcm', normalize=True, operators='AND_PRODUCT')
    RMSE_FCM_norm_and[i]=FIS.calculate_error().get('OUTPUT')
    
    FIS = pyFUME(datapath='IPMU2020/NASA.csv', nr_clus=3, method='Takagi-Sugeno', cluster_method='fstpso', normalize=True, operators='AND_PRODUCT')
    RMSE_PSO_norm_and[i]=FIS.calculate_error().get('OUTPUT')
    
    

#print(RMSE)
#print('The mean RMSE of', number_of_runs, 'runs is', np.round(np.mean(RMSE),2), 'with standard deviation', np.round(np.std(RMSE),2))
