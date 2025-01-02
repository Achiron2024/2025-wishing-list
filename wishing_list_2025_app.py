import streamlit as st

def main():
    st.title("2025 Wishing List Planner")
    st.write("Answer a few questions to find the best wish for you!")

    # Define wishes and factors
    wishes = {
        "Adventure and travel": "Travel to Japan",
        "Creativity and self-expression": "Learn a new musical instrument",
        "Health and fitness": "Start a fitness program",
        "Personal growth": "Read 50 books",
        "Financial stability": "Save money for a big purchase",
        "Social connections": "Reconnect with old friends",
        "Practical skills": "Improve cooking skills",
    }

    # Collect user ratings
    st.write("Rate the importance of the following factors (1 = Not important, 5 = Very important):")
    user_scores = {}
    for factor in wishes.keys():
        user_scores[factor] = st.slider(factor, 1, 5, 3)

    # Recommend the best wish
    best_factor = max(user_scores, key=user_scores.get)
    best_wish = wishes[best_factor]

    # Display the recommendation
    st.write("### Based on your preferences, your best wish for 2025 is:")
    st.subheader(best_wish)

if __name__ == "__main__":
    main()
