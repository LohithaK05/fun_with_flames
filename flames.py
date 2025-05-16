import streamlit as st
st.markdown(
    """
    <style>
    /* Fade-in animation */
    @keyframes fadeIn {
        from {
            opacity: 0;
        }
        to {
            opacity: 1;
        }
    }
    
    /* Bounce animation */
    @keyframes bounce {
        0%, 20%, 50%, 80%, 100% {
            transform: translateY(0);
        }
        40% {
            transform: translateY(-20px);
        }
        60% {
            transform: translateY(-10px);
        }
    }

    /* Scale-up animation */
    @keyframes scaleUp {
        from {
            transform: scale(0.8);
        }
        to {
            transform: scale(1);
        }
    }

    /* Apply animations to elements */
    .fade-in {
        animation: fadeIn 2s ease-in-out;
    }
    .bounce {
        animation: bounce 2s infinite;
    }
    .scale-up {
        animation: scaleUp 1s ease-in-out;
    }

    /* Button styling with animation */
    .stButton>button {
        background-color: #FF5733;
        color: white;
        border-radius: 12px;
        font-size: 18px;
        padding: 10px 20px;
        border: none;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
        animation: scaleUp 1s ease-in-out;
        transition: 0.3s ease-in-out;
    }
    .stButton>button:hover {
        background-color: #C70039;
        transform: scale(1.1);
    }

    /* Sidebar styling */
    .sidebar-content {
        color: white;
        background: linear-gradient(90deg, #FF5733, #FFC300);
        padding: 10px;
        border-radius: 10px;
        animation: fadeIn 3s ease-in-out;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown('<h1 class="fade-in">🔥 FLAMES Game 🔥</h1>', unsafe_allow_html=True)
st.sidebar.markdown('<div class="sidebar-content"><h1>WELCOME TO FLAMES GAME</h1></div>', unsafe_allow_html=True)
st.sidebar.button("Home")
st.sidebar.button("About")
st.subheader("Enter Names to Play")
a=list(st.text_input("Enter first name",placeholder="Type to play...").lower())
b=list(st.text_input("Enter second name",placeholder="Type to play...").lower())
for i in a.copy():
    if i in b:
        a.remove(i)
        b.remove(i)
n=len(a+b)
print(a,b,n)
s="flames"
while(len(s)!=1):
    i=n%len(s)-1
    if i==-1:
        s=s[:len(s)-1]
    else:
        s=s[i+1:]+s[:i]
d={ 'f':'Friends😎','l':'Lovers❤️','a':'Affection💗','m':'Marriage💍','e':'Enemies⚔️','s':'Siblings👨🏻‍👩🏻‍👧🏻‍👦🏻'}
if st.button("Get Results 🎉"):
    st.success(d[s])
st.slider("Rate the Flames game:", 1, 10)