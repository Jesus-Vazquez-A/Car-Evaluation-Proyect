# **Car Evaluation**

<img src = "https://di-uploads-pod5.dealerinspire.com/autocitysd/uploads/2019/03/Used-Car-Evaluation-Checklist.jpg">


## **Definition of Problem**

### **Features of Dataset**


* **Buying** Degree of purchase of the vehicle.

* **Maint** Degree of vehicle maintenance.

* **Doors** Number of vehicle doors.

* **Persons** Number of people that fit in the car.

* **Lug Boot** Car trunk size.

* **Safety** Degree of vehicle safety.


<img src = "https://github.com/Jesus-Vazquez-A/Car-Evaluation-Proyect/blob/main/img/matrix_img.png">



Almost all variables are well balanced.

Except for the class tag which is the variable to predict. Therefore, our model can be biased and give the prediction preference to the class that is in greater proportion.


## **Proyect Summary**


### **Approach**

The class variable has a clear imbalance. Therefore we will use the **SMOTE** transformation. Which consists in creating new data similar values. According to the percentage of class that is in greater proportion.
