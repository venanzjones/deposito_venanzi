import streamlit as st
from openai import AzureOpenAI
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

# Aggiungo il decorator alla funzione get_chat_completion
@retry(
    reraise=True,
    stop=stop_after_attempt(5),  # Retry up to n=5 times
    wait=wait_exponential(multiplier=1, min=2, max=10),  # Wait times between retries increase exponentially
    retry=retry_if_exception_type(Exception),  
)
def get_chat_completion(client, model_name, messages):
    return client.chat.completions.create(
        model=model_name,
        messages=messages,
        stream=True,
    )

st.title("AzureOpenAI chatbot ⌨️​")

tab1, tab2 = st.tabs(["⌨️​ Chatbot", "⚙️ Settings"])

if "custom_model" not in st.session_state:
    st.session_state.custom_model = ""
if "custom_key" not in st.session_state:
    st.session_state.custom_key = ""
if "custom_endpoint" not in st.session_state:
    st.session_state.custom_endpoint = ""

with tab2:
    st.subheader("Model Settings")
    st.session_state.custom_model = st.text_input(
        "Model Name", st.session_state.custom_model or "gpt-4o"
    )
    st.session_state.custom_key = st.text_input(
        "User API Key", st.session_state.custom_key, type="password"
    )
    st.session_state.custom_endpoint = st.text_input(
        "Endpoint", st.session_state.custom_endpoint
    )

with tab1:
    model_name = st.session_state.custom_model or "gpt-4o"
    api_key = st.session_state.custom_key or st.secrets["AZURE_OPENAI_API_KEY"]
    endpoint = st.session_state.custom_endpoint or st.secrets["AZURE_ENDPOINT"]
    api_version = "2024-12-01-preview"

    # Initialize AzureOpenAI client
    try:
        client = AzureOpenAI(
            api_key=api_key,
            api_version=api_version,
            azure_endpoint=endpoint,
        )
    except Exception as e:
        st.error(f"Failed to initialize client: {e}")
        st.stop()

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("What is up?"):
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            try:
                stream = get_chat_completion(
                    client,
                    model_name,
                    [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]                )
                response = st.write_stream(stream)
            except Exception as e:
                response = f"Error from Azure OpenAI after retries: {e}"
                st.error(response)

        st.session_state.messages.append({"role": "assistant", "content": response})
