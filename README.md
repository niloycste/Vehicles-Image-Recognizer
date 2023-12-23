# Vehicles-recognizer

Welcome to the Vehicle Image Recognizer, a powerful system capable of classifying various vehicles. Below is a list of vehicles it can identify:<br/>

1. car
2. motorcycle
3. bicycle
4. truck
5. bus
6. van
7. rickshaw
8. scooter
9. skateboard
10. ambulance
11. fire truck
12. tractor
13. segway
14. unicycle
15. jet ski
16. helicopter
17. airplane
18. boat
19. kayak
20. hovercraft

# Dataset Preparation
**Data Collection:** Downloaded from DuckDuckGo using term name <br/>
**DataLoader:** Used fastai DataBlock API to set up the DataLoader.<br/>
**Data Augmentation:** fastai provides default data augmentation which operates in GPU.<br/>
Details can be found in `notebooks/Data_Prep.ipynb`

# Training and Data Cleaning

**Training:** Fine-tuned a resnet34 model for 5 epochs (3 times) and got upto ~96% accuracy.<br/>
**Data Cleaning:** This part took the highest time. Since I collected data from browser, there were many noises. Also, there were images that contained. I cleaned and updated data using fastai ImageClassifierCleaner. I cleaned the data each time after training or finetuning, except for the last time which was the final iteration of the model.<br/> 

# Model Deployment
I deployed to model to HuggingFace Spaces Gradio App. The implementation can be found in `deployment`folder or [here](https://huggingface.co/spaces/niloycste68/Vehicles-recognizer) <br/>
<img src = "deployment/hugging_face.png",width="400", height="300">

# API integration with GitHub Pages
The deployed model API is integrated [here](https://niloycste.github.io/Vehicles-Image-Recognizer/) in GitHub Pages Website. Implementation and other details can be found in `docs` folder.
