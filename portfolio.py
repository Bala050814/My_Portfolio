import streamlit as st

st.set_page_config(page_title="My Portfolio")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a page:", ["Computer Guessing Game", "About The Creator", "Projects"])

if page == "About The Creator":
    st.markdown("<h1 style='color:#77E7FB'>I am</h1><h1 style='color:#FDD665'>Balamurugan R</h1>", unsafe_allow_html=True)
    st.subheader("Aspiring Learner | KGISL Institute of Technology | Electronics and Communication Engineering Student")
    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.image("C:\\Users\\Balamurugan\\Documents\\streamlit prg\\1000015961-01.jpeg", width=290)

    with col2:
        st.markdown("<h1 style='color:#77E7FB'>About Me</h1>", unsafe_allow_html=True)

        st.write("""
        Hello! I am Balamurugan R, a student at KGISL Institute of Technology pursuing a degree in Electronics and Communication Engineering. 
        Originally from Thoothukudi, I have a strong passion for electronics and circuit design. My interests lie in exploring the latest technologies in communication systems and understanding their practical applications. 
        I am eager to expand my knowledge and skills in this exciting field, with a commitment to engaging in hands-on projects and internships that will enhance my learning experience. 
        I look forward to contributing to advancements in electronics and communication.
        """)
    
        st.markdown("---")

    st.markdown("<h1 style='color:#77E7FB'>Interests</h1>", unsafe_allow_html=True)

    st.markdown(""" 
    - <span style='color:teal'>🚀 Embedded Systems 🕹️</span>
    - <span style='color:green'>🚀 Programming 🤖</span>
    - <span style='color:orange'>🚀 Playing Chess ♟️</span>
    - <span style='color:red'>🚀 Playing Basketball 🏀</span>
    """, unsafe_allow_html=True)
    
    st.markdown("---")

    st.markdown("<h1 style='color:#77E7FB'>My Short-Term Goals</h1>", unsafe_allow_html=True)
    st.markdown(""" 
    - <span style='color:orange'>To gain knowledge in Python and its frameworks.</span><br>
    - <span style='color:orange'>To win the PYEXPO2025.</span><br>
    - <span style='color:orange'>To gain knowledge in IoT.</span>
    """, unsafe_allow_html=True)

    st.markdown("<h1 style='color:#77E7FB'>My Long-Term Goals</h1>", unsafe_allow_html=True)
    st.markdown(""" 
    - <span style='color:orange'>To travel around the world.</span><br>
    - <span style='color:orange'>To buy a cliff villa in Goa.</span>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("<h1 style='color:#77E7FB'>Contact Me</h1>", unsafe_allow_html=True)
    st.write("If you'd like to get in touch, please reach out via email: [balamurugan.r050814@gmail.com](mailto:balamurugan.r050814@gmail.com)")
    st.write("[LinkedIn](https://www.linkedin.com/in/balamurugan-r-70a459301) | [GitHub](https://github.com/Bala050814)")
    st.markdown("---")

    st.write("© 2024 Balamurugan R. All rights reserved.")

elif page == "Computer Guessing Game":
    # Your Computer Guessing Game logic here
    st.markdown("<h1 style=color:#77E7FB>Computer Guessing Game</h1>",unsafe_allow_html=True)
    st.write("This section is under development.")
    st.image("https://th.bing.com/th/id/R.afe1465e67bad888eb3858b11a20c470?rik=FF89FttF05et6Q&riu=http%3a%2f%2fpageunderconstruction.weebly.com%2fuploads%2f1%2f1%2f4%2f1%2f11410642%2fpage-under-construction_orig.jpg&ehk=28ZwWQzUal0CCQxYtJylJSW8tX%2fFdK3yx1ATs2pUPWw%3d&risl=&pid=ImgRaw&r=0")  # Placeholder for the actual game

else:
    st.markdown("<h1 style='color:#77E7FB'>PROJECTS</h1>", unsafe_allow_html=True)
    st.write("""
    While I am currently in the early stages of my learning journey in Electronics and Communication Engineering, I am actively exploring various concepts and skills. 
    Although I do not have many notable projects to showcase at this time, I am eager to apply what I learn through hands-on experiences and future projects. 
    I am committed to engaging in practical applications and internships that will enhance my knowledge and help me build a solid portfolio.
    """)

    # Project: Smart Blind Stick
    st.markdown("<h2 style='color: teal;'>PROJECT: Smart Blind Stick</h2>", unsafe_allow_html=True)
    st.image("20240804_200052.jpg", width=300)

    st.write("**Objective**: The Smart Blind Stick is designed to assist visually impaired individuals in navigating their surroundings safely and independently.")
    st.write("**Components Used**:")
    st.write("- **Raspberry Pi Pico**")
    st.write("- **Ultrasonic Sensor**")
    st.write("- **Breadboard**")

    st.write("**Functionality**:")
    st.write("1. **Obstacle Detection**")
    st.write("2. **Feedback Mechanism**")
    st.write("3. **User-Friendly Design**")

    st.write("**Future Improvements**:")
    st.write("- **Bluetooth Connectivity**")
    st.write("- **GPS Module**")
    st.write("- **Light Sensor**")

    st.write("**Conclusion**: The Smart Blind Stick enhances mobility for visually impaired individuals.")

    st.markdown("<h2 style='color: teal;'>PROJECT: Mini Satellite</h2>", unsafe_allow_html=True)
    st.write("**Status**: This project is currently under development. Stay tuned for updates!")
