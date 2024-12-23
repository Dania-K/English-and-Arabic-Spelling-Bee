import streamlit as st
import random

# Arabic word lists for each grade
arabic_word_lists = {
    "Grade1": ["الحمد", "لله", "رب", "العالمين", "الرحمن", "الرحيم", "مالك", "يوم", "الدين", "إياك", "نعبد", "وإياك", "نستعين", "اهدنا", "الصراط", "المستقيم", "صراط", "الذين", "أنعمت", "عليهم", "غير", "المغضوب", "عليهم", "ولا", "الضالين"],
    "Grade2": ["قل", "أعوذ", "برب", "الفلق", "من", "شر", "ما", "خلق", "ومن", "شر", "غاسق", "إذا", "وقب", "ومن", "شر", "النفاثات", "في", "العقد", "ومن", "شر", "حاسد", "إذا", "حسد", "قل", "أعوذ", "برب", "الناس", "ملك", "الناس", "إله", "الناس", "من", "شر", "الوسواس", "الخناس", "الذي", "يوسوس", "في", "صدور", "الناس", "من", "الجنة", "والناس"],
    "Grade3": ["تبت", "يدا", "أبي", "لهب", "وتب", "ما", "أغنى", "عنه", "ماله", "وما", "كسب", "سيصلى", "نارًا", "ذات", "لهب", "وامرأته", "حمالة", "الحطب", "في", "جيدها", "حبل", "من", "مسد", "قل", "هو", "الله", "أحد", "الله", "الصمد", "لم", "يلد", "ولم", "يولد", "ولم", "يكن", "له", "كفوًا", "أحد"],
}

# English word lists for each grade
english_word_lists = {
    "Grade1": ["apple", "ball", "cat", "dog", "egg", "fish", "goat", "hat", "ice", "jug"],
    "Grade2": ["kite", "lamp", "monkey", "nest", "orange", "pencil", "queen", "rabbit", "snake", "tiger"],
    "Grade3": ["umbrella", "vase", "whale", "xylophone", "yarn", "zebra", "yellow", "purple", "garden", "school"],
}

# Sidebar for toggling between Spelling Bee languages
st.sidebar.title("Spelling Bee")
language_toggle = st.sidebar.radio("Choose Spelling Bee Type", ["English Spelling Bee", "Arabic Spelling Bee"])

# Update word lists based on the toggle
if language_toggle == "Arabic Spelling Bee":
    word_lists = arabic_word_lists
    st.sidebar.write("You are in Arabic Spelling Bee mode.")
else:
    word_lists = english_word_lists
    st.sidebar.write("You are in English Spelling Bee mode.")

# Main page content
st.title("Spelling Bee Competition")
st.write(f"Current Mode: **{language_toggle}**")

# Grade and setup
st.header("Competition Setup")
grade = st.selectbox("Select Grade Level", options=list(word_lists.keys()))
num_contestants = st.slider("Number of Contestants", 1, 20, 5)

if st.button("Assign Words"):
    # Ensure the word list for the grade has enough words
    if len(word_lists[grade]) < num_contestants:
        st.error("Not enough words for the number of contestants in this grade.")
    else:
        contestants = [f"Contestant {i + 1}" for i in range(num_contestants)]
        assigned_words = random.sample(word_lists[grade], num_contestants)
        
        st.subheader("Assigned Words")
        for contestant, word in zip(contestants, assigned_words):
            st.write(f"{contestant}: {word}")

# Additional sections
st.sidebar.header("Navigation")
page = st.sidebar.radio("Navigate", ["Home", "History", "Reset"])

if page == "Home":
    st.subheader("Welcome to the Spelling Bee!")
    st.write("Use the setup options to start organizing your competition.")

elif page == "History":
    st.subheader("Competition History")
    st.write("This section will display past rounds and assigned words.")

elif page == "Reset":
    st.subheader("Reset Competition Data")
    if st.button("Reset Data"):
        st.success("Competition data has been reset.")
