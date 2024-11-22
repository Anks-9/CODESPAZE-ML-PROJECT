from fastai.vision.all import *
import gradio as gr

def get_full_label(file_path):
    return f"{file_path.parts[-2]}/{file_path.parts[-3]}"

Lrn = load_learner('MODEL.pkl')

labels = Lrn.dls.vocab

def classify_waste(im):
    pred,idx,probs = Lrn.predict(im)
    return {labels[i]: float(probs[i]) for i in range(len(labels))}

title = "Waste Classifier"
description = "A Waste Classifier trained on the Waste Segregation Image dataset from Kaggle with Fastai. Developed as a demo for Gradio and Hugging Face Spaces to automatically classify waste and categories such as biodegradable and non-biodegradable"

image = gr.Image(type = "pil")
label = gr.Label(num_top_classes=3)
examples = ['e-waste.jpeg', 'leaf waste.jpeg', 'food waste.jpeg', 'metal waste.jpeg', 'plastic.jpeg']

intf = gr.Interface(fn=classify_waste, inputs=image, outputs=label, examples=examples,title=title,description=description)
intf.launch(inline=True)


