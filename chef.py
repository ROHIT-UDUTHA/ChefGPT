import streamlit as st
import os
from dotenv import load_dotenv
import openai

# Load .env variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = os.getenv("OPENAI_API_BASE")  # Important for OpenRouter

# Streamlit UI
st.set_page_config(page_title="AI Chef", page_icon="🍽️")
st.header("🍽️ AI Chef - Free Meal Generator via OpenRouter", divider="gray")

st.write("Using a free GPT-like model via [OpenRouter.ai](https://openrouter.ai)")

# User inputs
cuisine = st.selectbox("🌍 What cuisine do you desire?", 
    ("American", "Chinese", "French", "Indian", "Italian", "Japanese", "Mexican", "Turkish"), 
    index=None, placeholder="Select cuisine")

dietary_preference = st.selectbox("🥗 Dietary preferences?", 
    ("Diabetes", "Gluten free", "Halal", "Keto", "Kosher", "Lactose Intolerance", "Paleo", "Vegan", "Vegetarian", "None"),
    index=None, placeholder="Select dietary preference")

allergy = st.text_input("⚠️ Enter your food allergy (if any):", value="peanuts")
ingredient_1 = st.text_input("🧂 First ingredient:", value="ahi tuna")
ingredient_2 = st.text_input("🥩 Second ingredient:", value="chicken breast")
ingredient_3 = st.text_input("🥬 Third ingredient:", value="tofu")
wine = st.radio("🍷 Wine preference?", ["Red", "White", "None"], index=None)

# Prompt
prompt = f"""
You are a gourmet chef.

Create a list of {cuisine} recipes tailored for a customer who follows a {dietary_preference} diet.
Avoid any ingredients that contain or relate to the customer's allergy: {allergy}.

Available key ingredients:
- {ingredient_1}
- {ingredient_2}
- {ingredient_3}

You may use other compatible ingredients as needed.

The customer prefers {wine} wine.

For each recipe, provide:
1. Recipe Title
2. Preparation Instructions
3. Estimated Time to Prepare
4. Recommended Wine Pairing
5. Estimated Calorie Count
6. Nutritional Facts
"""

# Button
generate = st.button("🍳 Generate My Recipes")

if generate:
    if not all([cuisine, dietary_preference, wine]):
        st.warning("⚠️ Please fill all required fields.")
    else:
        with st.spinner("Generating your recipes..."):
            try:
                response = openai.ChatCompletion.create(
                    model="openrouter/auto",  # Or try: meta-llama/llama-3-8b-instruct
                    messages=[
                        {"role": "system", "content": "You are a helpful culinary assistant."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7,
                    max_tokens=2048
                )
                output = response.choices[0].message.content
                tab1, tab2 = st.tabs(["🍽️ Recipes", "📄 Prompt"])
                with tab1:
                    st.markdown(output)
                with tab2:
                    st.code(prompt)

            except Exception as e:
                st.error(f"❌ Error generating recipes: {e}")
