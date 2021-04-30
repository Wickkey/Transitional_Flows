import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import SessionState

session_state = SessionState.get(checkboxed=False)

plt.style.use("fivethirtyeight")

st.title("Transitional Flow\n\n")
st.sidebar.header("y = a*sin(b*x +c)")
st.sidebar.subheader("Parameters")

a = st.sidebar.number_input("   A", min_value=- 100.0,
                            max_value=100.0, value=1.0, step=0.1)
b = st.sidebar.number_input("   B", min_value=- 100.0,
                            max_value=100.0, value=1.0, step=0.1)
c = st.sidebar.number_input("   C", min_value=- 1000.0,
                            max_value=1000.0, value=0.0, step=0.1)

bo = st.sidebar.checkbox(
    "degrees (radians by default)", value=False)
if bo:
    c = c*np.pi/180

# bo2 = st.sidebar.button("Plot")
if st.sidebar.button("Plot") or session_state.checkboxed:
    session_state.checkboxed = True
    count = 1
    x = np.arange(-10, 10, 0.001)
    y = a*np.sin(b*x + c)

    # plt.cla()
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title("Graph")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    st.pyplot(fig)
