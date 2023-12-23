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

image_input = gr.inputs.Image(shape=(224,224))
label_output = gr.outputs.Label()

examples = [
   'test_images/bus.jpg',
    'test_images/car.jpg',
    'test_images/helicopter.jpg',
    'test_images/plane.jpg',
    'test_images/Norton_Motorcycle.jpg',
    'test_images/pexels-pixabay-163236.jpg',
    'test_images/imgpr405.jpg',
    'test_images/tractor-385681_1280.jpg',
    'test_images/pexels-donald-tong-50911.jpg',
    'test_images/360_F_99053872_JO23heKr9O5tmtgICEmEHKcp8N1Orog1.jpg',
    'test_images/EMS_Kayaking.jpg',
    'test_images/istockphoto-157186300-612x612.jpg',
    'test_images/GUEST_93eeb16a-ea58-46bf-bb46-092947a4dc1a.jpg',
    'test_images/istockphoto-104300620-612x612.jpg',
    'test_images/Watsonville_74595-2104F-Large.jpg'

]

iface = gr.Interface(fn=recognize_image, inputs=image_input, outputs=label_output, examples=examples)
iface.launch(inline=False)
