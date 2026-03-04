import streamlit as st
import matplotlib.pyplot as plt
import math

st.set_page_config(page_title="DSA For Everyone", layout="wide")

# ================= GLOBAL STYLE =================
st.markdown("""
<style>

/* Hide Streamlit UI */
header {visibility: hidden;}
footer {visibility: hidden;}
#MainMenu {visibility: hidden;}

html {
    scroll-behavior: smooth;
}



/* Animated Background */
.stApp {
    background: radial-gradient(circle at 20% 20%, #1a002e, #000000);
    color: white !important;
    overflow-x: hidden;
}

/* Floating Glow */
.stApp::before {
    content: "";
    position: fixed;
    width: 600px;
    height: 600px;
    background: radial-gradient(circle, rgba(155,89,255,0.3), transparent 70%);
    top: -200px;
    left: -200px;
    animation: floatGlow 15s infinite alternate ease-in-out;
    z-index: 0;
}

@keyframes floatGlow {
    from {transform: translate(0px,0px);}
    to {transform: translate(200px,200px);}
}

/* Page Fade */
.block-container {
    animation: pageFade 1.2s ease;
    position: relative;
    z-index: 1;
}

/* Center Content */
section.main > div {
    max-width: 1100px;
    margin: auto;
}

/* Cinematic Titles */
h1, h2, h3 {
    text-align: center;
    color: white !important;
    font-weight: 700;
    letter-spacing: -1px;
    text-shadow: 0 0 20px #9b59ff;
    animation: glowPulse 3s infinite alternate;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(45deg,#9b59ff,#6c5ce7);
    color: white;
    border-radius: 16px;
    transition: all 0.3s ease;
    border: none;
}

.stButton>button:hover {
    box-shadow: 0 0 35px #9b59ff;
    transform: scale(1.1);
}

/* Smooth tab transition */
div[data-testid="stTabs"] {
    animation: tabFade 0.5s ease;
}

@keyframes tabFade {
    from {opacity:0; transform: translateY(10px);}
    to {opacity:1; transform: translateY(0);}
}

/* 3D Tilt Cards */
div[style*="box-shadow"] {
    transition: transform 0.4s ease, box-shadow 0.4s ease;
    transform-style: preserve-3d;
}

div[style*="box-shadow"]:hover {
    transform: rotateY(8deg) rotateX(8deg) scale(1.08);
    box-shadow: 0 20px 40px rgba(155,89,255,0.4);
}

/* Stack Animation */
div[style*="#ff6b6b"] {
    animation: dropStack 0.4s ease;
}

/* Queue Animation */
div[style*="#4ecdc4"] {
    animation: slideQueue 0.5s ease;
}

/* Array Animation */
div[style*="#9b59ff"] {
    animation: dropArray 0.5s ease;
}

/* Cursor Glow */
.glow-cursor {
    width: 14px;
    height: 14px;
    border-radius: 50%;
    position: fixed;
    background: rgba(155,89,255,0.9);
    pointer-events: none;
    mix-blend-mode: screen;
    box-shadow: 0 0 40px #9b59ff;
    z-index: 9999;
}

/* Animations */
@keyframes dropStack {
    from {opacity:0; transform: translateY(-60px);}
    to {opacity:1; transform: translateY(0);}
}

@keyframes slideQueue {
    from {opacity:0; transform: translateX(60px);}
    to {opacity:1; transform: translateX(0);}
}

@keyframes dropArray {
    from {opacity:0; transform: translateY(-30px);}
    to {opacity:1; transform: translateY(0);}
}

@keyframes glowPulse {
    from { text-shadow: 0 0 10px #9b59ff; }
    to { text-shadow: 0 0 35px #9b59ff; }
}

@keyframes pageFade {
    from {opacity: 0;}
    to {opacity: 1;}
}

</style>

<script>
const cursor = document.createElement("div");
cursor.classList.add("glow-cursor");
document.body.appendChild(cursor);

document.addEventListener("mousemove", (e) => {
    cursor.style.left = e.clientX + "px";
    cursor.style.top = e.clientY + "px";
});
</script>
""", unsafe_allow_html=True)

# ================= HEADER =================
st.markdown("""
<h1 style='font-size:50px;'>Learn DSA Visually</h1>
<p style='text-align:center; font-size:20px; opacity:0.8;'>
No technical jargon. Just real-life examples + interaction.
</p>
""", unsafe_allow_html=True)

st.markdown("---")

# ================= TABS =================
tab1, tab2, tab3 = st.tabs(["📦 Array", "📚 Stack", "🚍 Queue"])

# ================= ARRAY =================
with tab1:
    st.subheader("How Array Works")
    st.write("Think of lockers in a school. Each locker has a number.")
    st.write("If you know the number, you get your item instantly.")

    user_input = st.text_input("Enter numbers separated by comma", "10,20,30,40")

    if user_input:
        try:
            arr = list(map(int, user_input.split(",")))
            cols = st.columns(len(arr))

            for i, val in enumerate(arr):
                with cols[i]:
                    st.markdown(f"""
                    <div style="
                        background:#9b59ff;
                        padding:20px;
                        border-radius:10px;
                        text-align:center;
                        font-size:20px;
                        box-shadow:0 0 15px #9b59ff;">
                    {val}<br><small>Index {i}</small>
                    </div>
                    """, unsafe_allow_html=True)

            index = st.number_input("Enter index to access", 0, len(arr)-1)

            if st.button("Access Element"):
                st.success(f"Element at index {index} is {arr[index]}")

        except:
            st.error("Please enter valid comma-separated numbers.")

    st.info("Time Complexity:\nAccess → O(1)\nSearch → O(n)\nInsert/Delete → O(n)")
    st.info("Space Complexity → O(n)")

# ================= STACK =================
with tab2:
    st.subheader("How Stack Works")
    st.write("Think of stacking plates. Last plate added is first removed.")

    if "stack_data" not in st.session_state:
        st.session_state.stack_data = []

    value = st.number_input("Enter value to push", key="stack_input")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Push"):
            st.session_state.stack_data.append(value)

    with col2:
        if st.button("Pop"):
            if st.session_state.stack_data:
                st.session_state.stack_data.pop()

    st.markdown("### Visual Stack (Top is Bottom Block)")

    for val in reversed(st.session_state.stack_data):
        st.markdown(f"""
        <div style="
            background:#ff6b6b;
            padding:20px;
            margin:5px auto;
            width:200px;
            text-align:center;
            border-radius:10px;
            box-shadow:0 0 15px #ff6b6b;">
        {val}
        </div>
        """, unsafe_allow_html=True)

    st.info("Push → O(1)\nPop → O(1)")
    st.info("Space Complexity → O(n)")

# ================= QUEUE =================
with tab3:
    st.subheader("How Queue Works")
    st.write("Think of standing in a bus line.")

    if "queue_data" not in st.session_state:
        st.session_state.queue_data = []

    value = st.number_input("Enter value to enqueue", key="queue_input")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Enqueue"):
            st.session_state.queue_data.append(value)

    with col2:
        if st.button("Dequeue"):
            if st.session_state.queue_data:
                st.session_state.queue_data.pop(0)

    st.markdown("### Visual Queue (Front is Left)")

    if st.session_state.queue_data:
        cols = st.columns(len(st.session_state.queue_data))
        for i, val in enumerate(st.session_state.queue_data):
            with cols[i]:
                st.markdown(f"""
                <div style="
                    background:#4ecdc4;
                    padding:20px;
                    border-radius:10px;
                    text-align:center;
                    font-size:20px;
                    box-shadow:0 0 15px #4ecdc4;">
                {val}
                </div>
                """, unsafe_allow_html=True)
    else:
        st.write("Queue is empty.")

    st.info("Enqueue → O(1)\nDequeue → O(1)")
    st.info("Space Complexity → O(n)")

# ================= BIG O VISUALIZER =================

st.markdown("---")
st.header("Big-O Growth Visualizer")

size = st.slider("Increase Data Size (n)", 1, 100, 10)

# 🎛 Graph Size Controls
colA, colB = st.columns(2)

with colA:
    graph_width = st.slider("Graph Width", 4, 20, 8)

with colB:
    graph_height = st.slider("Graph Height", 4, 15, 5)

import math
import matplotlib.pyplot as plt

x = list(range(1, size + 1))
o1 = [1 for _ in x]
ologn = [math.log(i+1) for i in x]
on = x
on2 = [i*i for i in x]

# 👇 Apply user-selected size here
fig, ax = plt.subplots(figsize=(graph_width, graph_height))

ax.plot(x, o1)
ax.plot(x, ologn)
ax.plot(x, on)
ax.plot(x, on2)

ax.set_title("Growth Comparison")
ax.set_xlabel("Input Size (n)")
ax.set_ylabel("Operations")

st.pyplot(fig)

st.success("Now even a non-IT person can SEE how algorithms grow 🚀")