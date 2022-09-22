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

## **EDA**

<img src = "https://github.com/Jesus-Vazquez-A/Car-Evaluation-Proyect/blob/main/img/matrix_barplot.png">

Most of the classes have a good proportion, except for the variable to be predicted, there is a clear disproportion between both classes. It can cause the classification model to have preference in the class with the most presence, for this reason it is convenient to make a balance adjustment.

## **SMOTE**
<img src = "https://github.com/Jesus-Vazquez-A/Car-Evaluation-Proyect/blob/main/img/SMOTE.png">

Applying the SMOTE algorithm, a perfect match between the variables to be predicted is achieved, generating new examples from the data set, allowing the algorithm to have more data to learn.


## **Random Forest**



<img src = "https://ecosistemas.ovacen.com/wp-content/uploads/2018/01/bosque.jpg">


I decided to apply this algorithm, because it is not a complex problem and it is based on logical decisions, in addition to not requiring a data standardization process.

It works in a similar way to its smaller brother the decision tree, with the difference that you only use one tree you can use many more.

The prediction system for a classification problem works as follows: Each Random Forest estimator will generate its prediction and the final value will be the most voted category, solving the decision tree overfitting problem.

![cm](https://user-images.githubusercontent.com/85312561/191783771-8f660ce7-8fdd-4dca-8489-44a68b5770c3.png)

![metrics](https://user-images.githubusercontent.com/85312561/191783785-697f9ac8-278c-41e4-b640-9f2b15f5952e.png)

Most of the categories are classified correctly, in addition to relentless cprecision per category, which gives us a robust model without the risk of overfitting.


Finally we save the model, with the purpose of using it to generate a web application using Shiny, which allows users to enter new data in a comfortable way and generate predictions in real time.

<img src = "https://media.giphy.com/media/Xsi8TISeEbDd8cPDI2/giphy.gif">
