NAME = "Ahmed.Fouad.Hassan.Mousa"
HANDLE = "A7.Fo2ad"
LOCATION = "Alexandria, Egypt"
EMAIL = "a7medfo2ad2004@gmail.com"
GITHUB = "https://github.com/A7medF0uad"
LINKEDIN = "https://www.linkedin.com/in/ahmed-fouad-97329334a/"
GITHUB_USER = "A7medF0uad"
TAGLINE = "Data Science student — Machine Learning"

BIO = """
I'm a Data Science student based in Alexandria,
"""

SKILLS = {
    "Languages": ["Python", "R", "Java", "SQL"],
    "Data Science / ML": ["scikit-learn", "Pandas", "NumPy", "Jupyter", "Kaggle", "Google Colab"],
    "Deployment": ["Streamlit", "Streamlit Cloud"],
    "Classical AI": ["Minimax", "Alpha-Beta Pruning", "A*", "BFS/DFS", "CSP", "Genetic Algorithms"],
}

PROJECTS = [
    {
        "slug": "chess",
        "title": "Chess Opening Advisor",
        "one_liner": "A Tkinter chess GUI backed by a from-scratch Minimax engine with Alpha-Beta pruning.",
        "stack": ["Python", "Tkinter", "Minimax", "Alpha-Beta Pruning"],
        "page": "project_chess",
        "github": "https://github.com/A7medF0uad/Chess_Openin_Advisor",
        "details": """
Built a playable chess interface in Tkinter and paired it with a Minimax search
engine for move evaluation. Alpha-Beta pruning cuts the search tree so the
engine can look further ahead without the node count exploding the same
core algorithm used in the classical AI coursework, applied to a real,
interactive game instead of a toy example.
""",
        "highlights": [
            "Minimax game-tree search with Alpha-Beta pruning for move selection",
            "Tkinter GUI for board state, legal moves, and move history",
            "Adjustable search depth as a difficulty control",
        ],
    },
    {
        "slug": "food_delivery",
        "title": "Food Delivery Analysis",
        "one_liner": "An R + Shiny dashboard analyzing food delivery data, with a focus on RMSE-driven model evaluation.",
        "stack": ["R", "Shiny", "RMSE", "Predictive Modeling"],
        "page": "project_food_delivery",
        "github": "https://github.com/A7medF0uad/Food_Delivery_Analysis",
        "details": """
An interactive R Shiny dashboard exploring food delivery data — delivery times,
order patterns, and the factors that predict them. The core of the project was
evaluating predictive models honestly: understanding what RMSE actually
measures, why it penalizes large errors more than MAE does, and using it to
compare models rather than just reporting one number.
""",
        "highlights": [
            "Shiny dashboard for interactive exploration of delivery data",
            "Predictive modeling with RMSE-based evaluation and comparison",
            "Focus on interpreting evaluation metrics, not just computing them",
        ],
    },
    {
        "slug": "ds_salaries",
        "title": "DS Salaries Prediction",
        "one_liner": "A RandomForest salary predictor, deployed as a live Streamlit app.",
        "stack": ["Python", "scikit-learn", "RandomForest", "Streamlit", "Streamlit Cloud"],
        "page": "project_ds_salaries",
        "github": "https://github.com/A7medF0uad/ds-salaries-prediction",
        "deployed_url": "https://ds-salaries-prediction.streamlit.app/",
        "details": """
A full pipeline from raw data to deployed model: a RandomForest regressor
trained on data science salary data, wrapped in a Streamlit app, and shipped
to Streamlit Cloud. Getting the pipeline correct meant catching real bugs along
the way — an ordinal feature that was being one-hot encoded instead of
ordinally encoded, rare-category leakage from encoding before the train/test
split, and a stale kernel variable that made the notebook lie about its own
results.
""",
        "highlights": [
            "RandomForest regression pipeline built and debugged in Jupyter",
            "Fixed pre-split rare-category leakage and incorrect ordinal encoding",
            "Companion train_model.py + app.py, deployed live on Streamlit Cloud",
        ],
    },
]

RESUME_SECTIONS = {
    "education": [
        "Bachelor of Science in Data Science -- (2025 - 2029)"
    ],
    "certifications": ["..."],
    "experience": ["..."]
}
