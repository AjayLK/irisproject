import pickle
import json
import pandas as pd
import numpy as np
import config


class IrisDataset():
    def __init__(self,SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm):
        self.SepalLengthCm = SepalLengthCm
        self.SepalWidthCm = SepalWidthCm
        self.PetalLengthCm = PetalLengthCm
        self.PetalWidthCm = PetalWidthCm

    def load_file(self):
        with open(config.MODEL_FILE_PATH, "rb") as f:
            self.iris_model = pickle.load(f)

        with open(config.JSON_FILE_PATH, "r") as f:
            self.json_data = json.load(f)


    def get_predicted_species(self):
        self.load_file()  # calling load_file method to get

        array = np.zeros(len(self.json_data['columns']))

        array[0] = self.SepalLengthCm
        array[1] = self.SepalWidthCm
        array[2] = self.PetalLengthCm
        array[3] = self.PetalWidthCm

        print("Test Array -->\n",array)
        predicted_species = self.iris_model.predict([array])[0]
        return predicted_species
        
if __name__ == "__main__":
    SepalLengthCm = 4
    SepalWidthCm = 3
    PetalLengthCm = 2.5
    PetalWidthCm = 1.5

    id = IrisDataset(SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm)
    species = id.get_predicted_species()
    print()
    print(f"predicted species is {species}")
    
