import streamlit as st
import random

# Arabic word lists for each grade
arabic_word_lists = {
    "Grade1": ["الحمد", "لله", "رب", "العالمين", "الرحمن", "الرحيم", "مالك", "يوم", "الدين", "إياك", "نعبد", "وإياك", "نستعين", "اهدنا", "الصراط", "المستقيم", "صراط", "الذين", "أنعمت", "عليهم", "غير", "المغضوب", "عليهم", "ولا", "الضالين"],
    "Grade2": ["قل", "أعوذ", "برب", "الفلق", "من", "شر", "ما", "خلق", "ومن", "شر", "غاسق", "إذا", "وقب", "ومن", "شر", "النفاثات", "في", "العقد", "ومن", "شر", "حاسد", "إذا", "حسد", "قل", "أعوذ", "برب", "الناس", "ملك", "الناس", "إله", "الناس", "من", "شر", "الوسواس", "الخناس", "الذي", "يوسوس", "في", "صدور", "الناس", "من", "الجنة", "والناس"],
    "Grade3": ["تبت", "يدا", "أبي", "لهب", "وتب", "ما", "أغنى", "عنه", "ماله", "وما", "كسب", "سيصلى", "نارًا", "ذات", "لهب", "وامرأته", "حمالة", "الحطب", "في", "جيدها", "حبل", "من", "مسد", "قل", "هو", "الله", "أحد", "الله", "الصمد", "لم", "يلد", "ولم", "يولد", "ولم", "يكن", "له", "كفوًا", "أحد"],
    # Add more grades as needed
}

# English word lists for each grade
english_word_lists = {
    "Grade1": ["apple", "ball", "cat", "dog", "egg", "fish", "goat", "hat", "ice", "jug"],
    "Grade2": ["kite", "lamp", "monkey", "nest", "orange", "pencil", "queen", "rabbit", "snake", "tiger"],
    "Grade3": ["umbrella", "vase", "whale", "xylophone", "yarn", "zebra", "yellow", "purple", "garden", "school"],
    # Add more grades as needed
}

# Combine all existing features with the sidebar navigation
st.sidebar.header("Navigation")
page = st.sidebar.radio("Select a Page", options=["Home", "Setup", "History", "Reset"])

# Add language selection
st.sidebar.header("Language")
language = st.sidebar.radio("Choose a language", options=["Arabic", "English"])

# Determine the word list based on language selection
if language == "Arabic":
    word_lists = arabic_word_lists
    st.sidebar.write("Arabic mode selected.")
else:
    word_lists = english_word_lists
    st.sidebar.write("English mode selected.")

if page == "Home":
    st.title("Welcome to the Spelling Bee!")
    st.write("Select 'Setup' from the sidebar to begin organizing your competition.")

elif page == "Setup":
    st.subheader("Competition Setup")

    # Select grade level
    grade = st.selectbox("Choose a grade level:", options=word_lists.keys())

    # Number of contestants
    num_contestants = st.slider("Number of contestants:", min_value=1, max_value=20, value=5)

    # Assign words
    if st.button("Assign Words"):
        contestants = [f"Contestant {i+1}" for i in range(num_contestants)]
        assigned_words = random.sample(word_lists[grade], k=min(num_contestants, len(word_lists[grade])))

        st.write("Words assigned to contestants:")
        for contestant, word in zip(contestants, assigned_words):
            st.write(f"{contestant}: {word}")

elif page == "History":
    st.subheader("Round History")
    st.write("Previous rounds and results will be displayed here.")

elif page == "Reset":
    st.subheader("Reset Competition")
    if st.button("Reset All Data"):
        st.write("Competition data has been reset.")
