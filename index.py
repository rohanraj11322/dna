import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image


# Page Title

image = Image.open('dna.jpg')

st.image(image, use_column_width=True)

st.write("""
# Welcome to DNA Nucleotide Count Web app
***
This app counts the nucleotide composition of query DNA!
***
""")


######################
# Input Text Box
######################

st.header('Enter Your DNA sequence')

sequence_input = ">DNA Query 2\nTGATGACGTGCAGTAACGTGACGTGACGTGACGTGACGTGCGTGACGATGAC\nTGACGTGACGTATAGCGATGACGTGAACTCTAAATTGCCCCCTCTGAGGTCAAGGATTTGGAAATGC\nATGATGATGATCACCAGCATCGTGCCTGAAGCCATG"

sequence = st.text_area("Sequence input", sequence_input, height=240)
sequence = sequence.splitlines()
sequence = sequence[1:] # Skips the sequence name (first line)
sequence = ''.join(sequence) # Concatenates list to string

st.write("""
***
""")

## Prints the input DNA sequence
st.header('INPUT (DNA Query)')
sequence


## DNA nucleotide count
st.header('OUTPUT (DNA Nucleotide Count)')

### 1. Print nucleotide count
st.subheader('1. Print Nucleotide count')
def DNA_nucleotide_count(seq):
  d = dict([
            ('A',seq.count('A')),
            ('T',seq.count('T')),
            ('G',seq.count('G')),
            ('C',seq.count('C')),
            
            ])
  return d

Y = DNA_nucleotide_count(sequence)

#X_label = list(X)
#X_values = list(X.values())

Y

### 2. Print text
st.subheader('2. Print text')
st.write('The number of Adenine (A) in your Dna sequence is :\t' + str(Y['A']) )
st.write('The number of Thymine (T) in your Dna sequence is :\t' + str(Y['T']) )
st.write('The number of Guanine (G) in your Dna sequence is :\t ' + str(Y['G']) )
st.write('The number of Cytosine (C) in your Dna sequence is :\t' + str(Y['C']) )



### 3. Display DataFrame
st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(Y, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'nucleotide'})
st.write(df)

### 4. Display Bar Chart using Altair
st.subheader('4. Display Bar chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count',
    color=alt.value("red")
    
)

p = p.properties(
    width=alt.Step(80) # controls width of bar.
)
st.write(p)