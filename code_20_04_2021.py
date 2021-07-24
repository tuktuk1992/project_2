
import json
#read data while runtime
#f=str(int[argv[0])
# Reading  JSON file
f = open('C:/Users/ashis/PycharmProjects/VamStar/venv/resources/input.json' ,)
import pandas as pd
patients_df = pd.read_json('C:/Users/ashis/PycharmProjects/VamStar/venv/resources/input.json')

#Calculating BMI
patients_df["BMI"]=patients_df["WeightKg"]/(patients_df["HeightCm"]/100)
# print(patients_df)
#Calculating BMI_CATEGORY
patients_df['BMI_CATEGORY'] = patients_df['BMI'].apply(lambda x: 'Underweight' if x < 18.4
                                else( "Normal Weight" if x>18.5 and x<24.9 else
                                      ("Overweight" if x>25 and x<29.9 else
                                       ("Moderately Obese" if x>30 and x<34.9 else
                                        "Obese" if x>35 and x<39.9 else
                                        "Severely Obese" if  x>40 else "Very Severely Obese" ))))

#Calculating Health Risk
patients_df['Health_Risk'] = patients_df['BMI'].apply(lambda x: 'Malnutrition Risk' if x < 18.4
                                else( "Low risk" if x>18.5 and x<24.9 else
                                      ("Enhanced risk" if x>25 and x<29.9 else
                                       ("Medium risk" if x>30 and x<34.9 else
                                        "High risk" if x>35 and x<39.9 else
                                        "Risk" if  x>40 else "Very high Risk" ))))




#Printing dataframe
print(patients_df)


