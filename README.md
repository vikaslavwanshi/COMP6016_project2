# COMP6015_project
SWAT testbed project 

# Run this command to run the backend code:
gunicorn --bind 0.0.0.0:8000 --timeout 300 wsgi:app

Abstract:

Building a framework using various aspects of technologies using development of UI using React, developing of a robust ML model which can classify the attacks based on the discrepancies introduced in the system, then pass it to the UI to show our observations. We have worked on multiple parts of the project in this milestone, including testing of several types of attacks on Mininet, and then observed their behavior in Wireshark and captured these changes in a csv file to compare and show the results on UI.
The objective in this milestone is to create a security testbed and test different attacks on a secure water treatment (SWAT) system, and how well we can test different attacks on the existing system. We will be building a framework by performing regress testing and by implementation of ML models, to establish a more secure and robust framework, which could deal with heavy traffic of data and multiple attacks.

Introduction:
The dataset used in this project is tested with different types of attacks on Mininet, and we have developed a python topology script to create a network on Mininet.
We have introduced these attacks and recorded logs and observation using Wireshark, established connectivity between different network elements, hosts and nodes.
Later, we used this SWAT dataset to create a ML model after performing data preprocessing and data engineering on the chosen dataset. We have scaled the data to fit into the model and performed classification tasks using Random Forest classification model. This model captures the discrepancy between the changes that occurred in datasets (before and after file). We have also created a user interface where we upload these two files (raw dataset files and tested file). After uploading the files, we need to click on the upload and predict button to use the model functionality of predicting the outcome that whether there is any discrepancy in the system or not.
To give more highlights on the tasks we have performed earlier, we have worked on the creation of a security testbed for a project which can be used to implement our knowledge on ICS and set up an environment which is useful for simulating an ICS security testbed environment. It is a framework for building ICS security testbeds. It is extensible and reproducible in nature, and it can be integrated with modern technologies such as Container, dockers which provides a realistic network emulation. This framework will be an open-source framework for examination of several types of attacks.
This project aims to build and test security features in an ICS system (SWAT) and enhance the security prospects on the existing system by doing research and implementation. We will be creating ML models and python scripts which will deal with SWAT network topology. We are going to create network in Mininet and test several types of attacks, we have installed the dependencies and started learning SWAT datasets which are available in public domain and how we can utilize these datasets for our simulation, we need to create a model to implement and test the model by performing operation with different attacks.
