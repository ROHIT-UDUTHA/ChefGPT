import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load .env variables
load_dotenv(override=True)
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE"),  # Important for OpenRouter
)

# Streamlit UI
st.set_page_config(page_title="ChefGPT", page_icon="🍛")
st.header("ChefGPT 🍜", divider="gray")

uploaded_image = None

detected_ingredients = ""

if uploaded_image is not None:
    with st.spinner("🔍 Detecting ingredients from image..."):
        try:
            image_bytes = uploaded_image.read()
            encoded_image = base64.b64encode(image_bytes).decode("utf-8")

            vision_response = client.chat.completions.create(
                model="meta-llama/llama-3.2-11b-vision-instruct",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": "List all food ingredients visible in this image. Return only ingredient names separated by commas."},
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{encoded_image}"
                                }
                            }
                        ]
                    }
                ],
                max_tokens=300
            )

            detected_ingredients = vision_response.choices[0].message.content
            st.success(f"🧠 Detected Ingredients: {detected_ingredients}")

        except Exception as e:
            st.error(f"Image processing failed: {e}")

# User inputs
cuisine = st.selectbox("🌍 What cuisine do you desire?", 
    ("American", "Chinese", "French", "Indian", "Italian", "Japanese", "Mexican", "Turkish"), 
    index=None, placeholder="Select cuisine")

dietary_preference = st.selectbox("🥗 Dietary preferences?", 
    ("Diabetes", "Gluten free", "Halal", "Keto", "Kosher", "Lactose Intolerance", "Paleo", "Vegan", "Vegetarian", "None"),
    index=None, placeholder="Select dietary preference")

allergy = st.text_input("⚠️ Enter your food allergy (if any):", value='')

default_ing = detected_ingredients.split(",") if detected_ingredients else ["", "", ""]

ingredient_1 = st.text_input("🧂 First ingredient:", value=default_ing[0] if len(default_ing) > 0 else "")
ingredient_2 = st.text_input("🥩 Second ingredient:", value=default_ing[1] if len(default_ing) > 1 else "")
ingredient_3 = st.text_input("🥬 Third ingredient:", value=default_ing[2] if len(default_ing) > 2 else "")
wine = st.radio("🍷 Wine preference?", ["Red", "White", "None"], index=None)

extra_context = f"Detected ingredients from image: {detected_ingredients}" if detected_ingredients else ""

prompt = f"""
You are a gourmet chef.

{extra_context}

Create a list of {cuisine} recipes tailored for a customer who follows a {dietary_preference} diet.
Avoid any ingredients that contain or relate to the customer's allergy: {allergy}.

Available key ingredients:
- {ingredient_1}
- {ingredient_2}
- {ingredient_3}

The customer prefers {wine} wine.

For each recipe, provide:
1. Recipe Title
2. Preparation Instructions
3. Estimated Time
4. Wine Pairing
5. Calories
6. Nutrition
"""

# Button
generate = st.button("🍳 Generate My Recipes")

if generate:
    if not all([cuisine, dietary_preference, wine]):
        st.warning("⚠️ Please fill all required fields.")
    else:
        with st.spinner("Generating your recipes..."):
            try:
                response = client.chat.completions.create(
                                        model="openrouter/auto",  # Or try: meta-llama/llama-3-8b-instruct
                    messages=[
                        {"role": "system", "content": "You are a helpful culinary assistant."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.5,
                    max_tokens=1500
                )
                output = response.choices[0].message.content
                tab1, tab2 = st.tabs(["🍽️ Recipes", "📄 Prompt"])
                with tab1:
                    st.markdown(output)
                with tab2:
                    st.code(prompt)

            except Exception as e:
                st.error(f"❌ Error generating recipes: {e}")
