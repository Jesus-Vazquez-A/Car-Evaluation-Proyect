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


#### **Balanced Class**


![balanced](https://user-images.githubusercontent.com/85312561/185450730-ef6fcb18-6e4e-4b61-a4e5-99264984ac56.png)


## **Model Interpration**


### **Decesion Tree**

<img src = "https://www.zigya.com/blog/wp-content/uploads/2021/01/dig10.png">


It works very similar to human logic. Use mathematical inequalities instead of questions. Since it is easier for algorithms to handle numbers than words.


#### **Selection of Max Depth Ideal**

![max_depth](https://user-images.githubusercontent.com/85312561/185457072-2b34eeaa-69bc-4e5d-ba8e-9c2892b8e0b8.png)


### **Random Forest**

<img src = "https://concepto.de/wp-content/uploads/2018/10/bosque2-e1539893598295.jpg">


