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

#### **Model Parameters**


* **max_depth**: Maximum depth of the tree.
* **random_state**: Random tree state


<img src = "https://www.zigya.com/blog/wp-content/uploads/2021/01/dig10.png"  height="600">


It works very similar to human logic. Use mathematical inequalities instead of questions. Since it is easier for algorithms to handle numbers than words.


#### **Selection of Max Depth Ideal**

![max_depth](https://user-images.githubusercontent.com/85312561/185457072-2b34eeaa-69bc-4e5d-ba8e-9c2892b8e0b8.png)


### **Random Forest**


Share several in common parameters. Except for a few:

#### **Model Parameters**

* **n_estimators**: Number of decision trees.
* **n_jobs**: Number of working cores of the CPU.

<img src = "https://concepto.de/wp-content/uploads/2018/10/bosque2-e1539893598295.jpg" >

The Random Forest algorithm works in a similar way to the decision tree. While decision tree you can only use one tree. With Random Forest you can use a maximum amount of 1000 estimators.


#### **Number of Estimators Ideal**


![n_estimators](https://user-images.githubusercontent.com/85312561/185458090-4f320a5f-96de-4781-88e2-5106ece3ee7b.png)



### **Support Vector Machine**

#### **Model Parameters**

* **kernel**: SVC core.
* **degree**:  Degree of the polynomial.

![svc](https://user-images.githubusercontent.com/85312561/185458595-c176c1f6-d980-4777-9ba7-501723df27d8.png)


It consists of finding the best hyperplane that fits the data set. According to the kernel provided by the user. It works quite well for relatively small data sets.

It has the disadvantage of requiring a scalar setting for variables. In order to make them comparable to each other. Since these algorithms are very sensitive.


## **Selection of the Best Model**


### **Criteria**


* The model must have **balanced accuracy**. For each case.
* The model must **not only** be **adapted** to the set of training deals.
* The algorithm must have **good performance**. For data you've never seen.
* Must have a **high percentage** of **generalization**.

![best_model](https://user-images.githubusercontent.com/85312561/185460722-c744a911-419c-42ca-b7c1-f180827dca87.png)


#### **Conclusion**

Although the Random Forest outperforms the other models. The Decesion Tree has a fairly **similar performance**. Also be less computationally heavy and easier to explain.

Therefore I consider it as the winning model. Which I will use to develop the application.



## **Opening the Black Box**

### **Decesion Tree Plot**

![decision_tree](https://user-images.githubusercontent.com/85312561/185462062-f7bbcd92-bf38-44d4-a643-c97d502feb55.png)


It is just a short form of the decision tree. Since it has more depth.


### **Plot Importance**

![plot_importance](https://user-images.githubusercontent.com/85312561/185462086-0ef8ad02-d315-471f-88ef-41547c0703d6.png)



