from fastai.vision.all import *
import gradio as gr

# import pathlib
# temp = pathlib.PosixPath
# pathlib.PosixPath = pathlib.WindowsPath




# Provide the full path to the model file
model_path = 'models/vehicle-recognizer-v2.pkl'
model = load_learner(model_path)

cap_labels = model.dls.vocab

def recognize_image(image):
    pred, idx, probs = model.predict(image)
    return dict(zip(cap_labels, map(float, probs)))

image_input = gr.Image()
label_output = gr.Label()

examples = [
    'test_images/bus.jpg',
    'test_images/car.jpg',
    'test_images/helicopter.jpg',
    'test_images/plane.jpg',
    'test_images/ambulence.jpg',
    'test_images/boat.jpg',
    'test_images/bycle.jpg',
    'test_images/fire_truck.jpg',
    'test_images/hovercraft.jpg',
    'test_images/jet_ski.jpg',
    'test_images/kayak.jpg',
    'test_images/motorcycle.jpg',
    'test_images/rickshaw.jpg',
    'test_images/scateboard.jpg',
    'test_images/scooter.jpg',
    'test_images/tractor.jpg',
    'test_images/van.jpg'
]

iface = gr.Interface(fn=recognize_image, inputs=image_input, outputs=label_output, examples=examples)
iface.launch(inline=False)
