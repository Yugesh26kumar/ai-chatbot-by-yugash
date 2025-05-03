
# 🧠 Intelligent Customer Support Chatbot with Gradio
# Step-by-step like Naan Mudhalvan project PDF

!pip install gradio pandas

import pandas as pd
import gradio as gr

# Load the FAQ dataset
faq_df = pd.read_csv("faq_data.csv")

# Chatbot response logic
def chatbot_response(user_input):
    user_input = user_input.lower()
    for _, row in faq_df.iterrows():
        if row['question_keywords'] in user_input:
            return row['response']
    return "Sorry, I couldn't understand that. Try typing 'help'."

# Gradio interface
gr.Interface(
    fn=chatbot_response,
    inputs=gr.Textbox(lines=2, placeholder="Type your customer support query..."),
    outputs="text",
    title="🤖 Customer Support Chatbot",
    description="Ask about refunds, order status, returns, cancellations, etc."
).launch(share=True)
