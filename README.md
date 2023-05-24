PROJECT OUTLINE

<h1>PROJECT NAME: Plant Disease Classification</h1>

## Contribution Guidelines
- Have a Look at the project structure and folder-overview below to understand where to store/upload your contribution
- If you're creating a task, Go to the task folder and create a new folder with the below naming convention and add a README.md with task details and goals to help other contributors understand
    - Task Folder Naming Convention : _task-n-taskname.(n is the task number)_  ex: task-1-data-analysis, task-2-model-deployment etc.
    - Create a README.md with a table containing information table about all contributions for the task.
- If you're contributing for a task, please make sure to store in relavant location and update the README.md information table with your contribution details.
- Make sure your File names(jupyter notebooks, python files, data sheet file names etc) has proper naming to help others in easily identifing them.
- Please restrict yourself from creating unnessesary folders other than in 'tasks' folder (as above mentioned naming convention) to avoid confusion. 

## Project Structure

    ├── LICENSE
    ├── README.md          <- The top-level README for developers/collaborators using this project.
    │ 
    │
    ├── reports            <- Folder containing the final reports/results of this project
    │   └── README.md      <- Details about final reports and analysis
    │ 
    │   
    ├── src                <- Source code folder for this project
        │
        ├── data           <- Datasets used and collected for this project
        │   
        ├── docs           <- Folder for Task documentations, Meeting Presentations and task Workflow Documents and Diagrams.
        │
        ├── references     <- Data dictionaries, manuals, and all other explanatory references used 
        │
        ├── tasks          <- Master folder for all individual task folders
        │
        └── results        <- Folder to store Final analysis and modelling results and code.
--------

## Folder Overview

- Reports           - Folder to store all Final Reports of this project
- Data              - Folder to Store all the data collected and used for this project 
- Docs              - Folder for Task documentations, Meeting Presentations and task Workflow Documents and Diagrams.
- References        - Folder to store any referneced code/research papers and other useful documents used for this project
- Tasks             - Master folder for all tasks
  - All Task Folder names should follow specific naming convention
  - All Task folder names should be in chronologial order (from 1 to n)
  - All Task folders should have a README.md file with task Details and task goals along with an info table containing all code/notebook files with their links and information
  - Update the [task-table](./src/tasks/README.md#task-table) whenever a task is created and explain the purpose and goals of the task to others.
- Results           - Folder to store final analysis modelling results for the project.
<h2>PROJECT DESCRIPTION</h2>
The project aims to develop a plant disease classification system using computer vision and deep learning techniques. The goal is to accurately identify and classify infected plant leaves based on images. The project will leverage image processing techniques, deep learning algorithms, and transfer learning to achieve accurate predictions.

<h2>PROJECT OBJECTIVE</h2>
The objective of this project is to develop a plant disease classification system that can accurately identify and classify different types of diseases affecting plants. The system will utilize machine learning techniques to analyze images of plant leaves and determine the presence of diseases such as fungal infections, viral infections, nutrient deficiencies, and other common plant ailments. By accurately identifying plant diseases, the project aims to assist farmers, gardeners, and agricultural experts in early detection and prompt treatment of plant diseases, ultimately leading to improved crop yield and reduced economic losses in the agricultural sector.
<h2>TECHNOLOGIES	</h2>
<ul>
<li>Transfer Learning: Transfer learning will be employed to leverage pre-trained models such as VGG16, ResNet, or Inception. By using these models as a starting point, the project can benefit from their learned features and significantly reduce training time.
<li>Deep Learning: TensorFlow and Keras will be utilized to build and train convolutional neural networks (CNNs) for plant disease classification. CNNs are well-suited for image classification tasks due to their ability to capture spatial dependencies in the data.
<li>Computer Vision: OpenCV will be used for image acquisition, enhancement, restoration, color image processing, and segmentation. It provides a comprehensive set of libraries and functions for working with images and extracting relevant features.
</ul>
<h2>DATASETS</h2>
The dataset used for this project is the "New Plant Diseases Dataset" available on Kaggle. It contains a large collection of images of plant leaves classified into various categories such as healthy, infected with different diseases, and seemingly infected. The dataset provides a diverse range of plant diseases, allowing for robust training and evaluation of the classification model.
<h2>PROJECT PIPELINE	</h2>
<ul>	
<li>DATA COLLECTION
<li>DATA PREPROCESSING
<li>IMAGE PROCESSING
<li>MODEL DEVELOPMENT
<li>MODEL TRAINING
<li>MODEL EVALUATION
<li>DEPLOYMENT
</ul>
