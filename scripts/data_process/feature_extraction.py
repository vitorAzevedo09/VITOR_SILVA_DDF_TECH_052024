import os
import json
import pandas as pd
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Request Gemini to extract features
def extract_features(description: str) -> str:
    # The Gemini 1.5 models are versatile and work with both text-only and multimodal prompts
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(f"extract the main features of the product using the description '{description}' returning only the json without inside json notation code")
    return json.loads(response.text.replace("```json","").replace("```",""))

dataset = pd.read_json("../../data/online_retail_II.json")

dataset["Features"] = dataset["Description"].apply(extract_features)

print(dataset)

