
# Project Description:
 ## This project is the modification of the time series forecast of express shipping units from distribution centers. This project takes into consideration other features beside time to project the shipments.
 
# Objectives:
 ## 1. Getting the shipment prediction at warehouse, customer and carrier level. 
 ## 2. To refelct the demand, we include order information as a features.
 ## 3. To reflect, different uncertain economic events and customer specific days, we include different variables such covid period, way day and prime day.
 ## 4. In the time series forecast, we were getting around 85-87% accuracy. One of the major goal of this prediction is to get better accuracy

# Methodology:
 ## We used 9 features year,month,week,warehouse,customer, total orders, covid period, way day, prime day to predict the number of shipping units for our express department.We did exploratory analysis to understand the distribution of data, how the variables are associated and what features has major importance on explaining the shipping units.Based on our exploratory analysis, we decided that non-linear ensamble techniques will be better fit for our dataset. We tested both random forest and xgboost and chose random forest to use for the final prediction.We also tuned the parameters of Random Forest model to get better accuracy

