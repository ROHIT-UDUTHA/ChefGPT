# � ChefGPT - Your Personal AI Chef

Ever stared at a fridge full of ingredients with no idea what to make? ChefGPT is here to help! This little app is like having a personal chef in your pocket. It uses AI to whip up custom recipes based on your tastes, dietary needs, and whatever you've got on hand.

The coolest part? You can just snap a picture of your ingredients, and ChefGPT will figure out what you've got and suggest recipes for you.

## ✨ What it Can Do

- **Explore Cuisines**: Fancy some Italian, Mexican, or maybe Japanese tonight? Just pick a cuisine.
- **Handle Your Diet**: Whether you're vegan, keto, gluten-free, or have other needs, ChefGPT has you covered.
- **Dodge Allergies**: Got an allergy? Let the app know, and it'll keep those ingredients out.
- **Use What You Have**: Tell it a few key ingredients, and it'll build a recipe around them.
- **See-Food Diet**: Upload a photo of your food, and the app's AI vision will identify the ingredients for you.
- **Wine Pairing**: Get a simple red or white wine suggestion to go with your meal.
- **Full Recipe Details**: Every recipe comes with a title, instructions, prep time, wine pairing, calorie count, and nutritional facts.
- **Simple & Clean UI**: Built with Streamlit to be easy and fun to use.

## 🛠️ The Tech Behind It

- **Backend**: Python
- **Web App**: Streamlit
- **The Brains**:
    - OpenAI & OpenRouter for generating creative recipes.
    - LLaMA 3.2 Vision for the image recognition magic.
- **Setup**: Uses `venv` for a clean environment and a `requirements.txt` for dependencies.

## 🚀 Get Cooking!

### What You'll Need

- Python 3.8 or newer
- An [OpenRouter API Key](https://openrouter.ai/keys) (they have a free tier!)

### Let's Set It Up

1.  **Clone the project:**
    ```bash
    git clone <repository-url>
    cd "ai chef"
    ```

2.  **Set up a virtual environment:** This keeps all the project's packages tidy.
    ```bash
    # On Windows
    python -m venv .venv
    .\.venv\Scripts\Activate.ps1

    # On macOS or Linux
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install all the necessary packages:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Create a `.env` file** in the main project folder. This is where you'll put your secret API key. Add these two lines:
    ```
    OPENAI_API_KEY="your-openrouter-api-key"
    OPENAI_API_BASE="https://openrouter.ai/api/v1"
    ```

### Start the App

Fire up the Streamlit server with this command:

```bash
streamlit run chef.py
```

Your personal AI chef will be ready for you at `http://localhost:8501`. Enjoy!
