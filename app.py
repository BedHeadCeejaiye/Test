import streamlit as st
import pandas as pd
import random

# title
st.title("Are you autistic??")

# list of funny captions
caption_lines = [
    "Why so serious??",
    "Because clearly this is the peak of human achievement.",
    "Homework made me do it, not passion.",
    "Warning: Goose content ahead.",
    "Outpizza the hut? Not today.",
    "Potatoes > everything else, obviously.",
    "Your GPA hinges on potato ratings.",
    "Because society depends on this nonsense.",
    "Because obviously you needed this in your life.",
    "Because the world was clearly waiting for this masterpiece",
    "Because your life wasn’t complete without rating potatoes",
    "Because homework said so, not common sense",
    "Because apparently nonsense is now science",
    "Because what else would you be doing right now?",
    "Because clearly society depends on this quiz",
    "What do you actually expect??",
    "Do not problem",
    "Bomba!1!!"
]

# Button to shuffle captions
if st.button("Does nothing useful really"):
    chosen_caption = random.choice(caption_lines)
    st.caption(chosen_caption)
else:
    st.caption("Why are you even here?")

# -------------------------------
# Quiz Section
# -------------------------------
st.header("Answer these questions seriously:")

q1 = st.radio("Do you eat pizza with a fork?", ["Yes, like a monster", "No, like a hero", "Sometimes, when nobody’s watching"])
q2 = st.checkbox("Do you scream when WiFi dies?")
q3 = st.slider("Rate your love for potatoes:", 0, 100, 42)
q4 = st.text_input("What’s the weirdest thing you’ve ever named?")
q5 = st.multiselect("Pick your spirit animal:", ["Duck", "Banana", "Laptop", "Arnel", "Invisible Unicorn"])
q6 = st.number_input("How many socks do you own?", min_value=0, max_value=999)
q7 = st.date_input("Pick the day you realized homework is pain")
q8 = st.time_input("Pick the time you usually question reality")
q9 = st.color_picker("Pick the color of your mood swings")
q10 = st.text_area("Describe how you would fight a goose")

submitted = st.button("Submit this or something")

# -------------------------------
# Results Section
# -------------------------------
if submitted:
    st.success("Wow time well spent. ")

    data = {
        "Question": ["Pizza fork?", "WiFi scream?", "Potato love", "Weird name", "Spirit animal", "Sock count", "Homework pain day", "Reality crisis time", "Mood swing color", "Goose battle plan"],
        "Answer": [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
    }
    df = pd.DataFrame(data)
    st.dataframe(df)

    st.download_button("Download your nonsense?", df.to_csv(index=False), "nonsense.csv")

    # Randomized nonsense outputs
    st.metric("Questions Answered", len(df))
    st.metric("Goose Threat Level", random.randint(1,10))
    st.progress(random.randint(1,100))

    st.info("Fun fact: bananas are berries, but strawberries are not.")
    st.warning("Warning: Goose detected nearby 🦆 (close enough).")
    st.error("Error: You failed to outpizza the hut.")
    st.success("Success: You are now 12% more autistic.")

    st.write("This is my school — RTU Pasig. If you want to find me and ask me if im autistic too, you can start here!")

    st.map(pd.DataFrame({"lat":[14.5703], "lon":[121.0851]}))

    # Goose video
    st.write("A very imporant video!! // MUST WATCH // LIFE CHANGING!!")
    st.video("https://www.youtube.com/watch?v=ygTa1mOTSo0")  # angy goose

    # how to fight goose
    with st.expander("Secret Goose Strategy Guide"):
        st.write("Step 1: Honk louder than the goose. Step 2: Run. Step 3: Pretend you won.")

# -------------------------------
# Summon Goose Button (always visible)
# -------------------------------
if st.button("Summon Goose"):
    goose_lines = [
        "HONK!",
        "Beware: Goose is now watching you.",
        "Goose says: Outpizza the hut? Not today.",
        "Your Goose Threat Level just doubled.",
        "The goose demands tribute in potatoes."
    ]
    st.write(random.choice(goose_lines))
    st.metric("Goose Threat Level", random.randint(1,10))

# -------------------------------
# About Section
# -------------------------------
st.header("About This App")
st.write("""
- **Use-case:** This app exists because my professor said so, not because humanity desperately needed another nonsense quiz.
- **Target users:** Anyone bored enough to click random buttons and wonder why they’re rating potatoes.
- **Inputs collected:** Your questionable life choices, goose battle strategies, and sock inventory.
- **Outputs shown:** Tables nobody asked for, progress bars that mean nothing, maps of my school, random goose videos, and messages that are basically inside jokes.
- **Final thought:** If you’re still reading this, congratulations — you’ve wasted your time exactly as intended.
""")
