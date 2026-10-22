from preprocess_data.preprocess import Word_Vector,correct_text 
from preprocess_data.load import load_data


#clean -> label llm -> data val -> train-pipeline -> validation-analyst


#- batch predict-processing-train

def imports_data():

    data = load_data()
    data = correct_text(data)

    x = Word_Vector()




    












