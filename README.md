🍽️ AI Chef: Customized Recipe Creation

Introducing AI Chef, an intelligent meal generator that uses OpenRouter.ai's free large language models.This Streamlit app creates personalized recipes according to your wine preferences, dietary restrictions, and ingredient and allergy preferences.



🚀 Features

Select the type of cuisine and any dietary requirements.

Steer clear of certain food allergies.

🧂 List up to three ingredients that you prefer.

🍷 Choose your preferred wine pairing.

Utilizes OpenRouter to use free models such as Mixtral

Contains nutritional information and calories for each recipe.



The Tech Stack

Streamlit

The OpenRouter API

Python Dotenv



Installing

1. Make a clone of the repository

https://github.com/ROHIT-UDUTHA/AI-CHEF.gitcd AI-CHEF git clone

2. Make an environment file (.env).

OPENAI_API_KEY=your-openrouter-api-keyOPENAI_API_BASE=https://openrouter.ai/api/v1

Visit https://openrouter.ai/keys to obtain a free key.

3. Set up dependencies

pip install -r requirements.txt



Launch the application.

Chef.py is run in streamlit.

Your browser will launch the application at http://localhost:8501.


🌐 Optional live deployment

With Streamlit Cloud, you can install this app for free:

Link your GitHub repository.

Use Streamlit's "Secrets" user interface to set the.env variables.

Select "Deploy."



Screenshots



License 📄

The MIT License governs this project.Use, alter, and distribute without restriction!



Credits

Created by ROHIT-UDUTHA using ❤️

Powered by: Streamlit - OpenRouter.ai
