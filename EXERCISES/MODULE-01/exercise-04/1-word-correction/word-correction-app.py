import streamlit as st
from levenshtein_distance import levenshtein_distance
from vocabs import vocabs

def main():
    st.title("Word Correction using Levenshtein Distance")
    word = st.text_input('Word:')

    if st.button("Compute"):
        # Compute levenshtein distance
        leven_distances = dict()
        for vocab in vocabs:
            leven_distances[vocab] = levenshtein_distance(word, vocab)

        # Sorted by distance
        sorted_distances = dict(
            sorted(leven_distances.items(), key=lambda item: item[1]))
        correct_word = list(sorted_distances.keys())[0]
        st.write('Correct word:', correct_word)

        col1, col2 = st.columns(2)
        col1.write('Vocabulary:')
        col1.write(vocabs)
        col2.write('Distances:')
        col2.write(sorted_distances)

if __name__ == "__main__":
    main()

# streamlit run EXERCISES\MODULE-01\exercise-04\1-word-correction\word-correction-app.py
