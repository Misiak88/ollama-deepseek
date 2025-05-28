import gradio as gr
import requests
import time

# Define the API endpoint and headers
url = 'http://ollama:11434/api/generate'

def respond_to_query(query, model, max_tokens, temperature, top_p):
    # Prepare the payload for the API request, using the user query as the prompt
    payload = {
        "model": model,
        "prompt": query,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "top_p": top_p,
        "stream": False
    }

    # Record the start time
    start_time = time.time()

    # Make the POST request to the Ollama API
    response = requests.post(url, json=payload)

    # Record the end time
    end_time = time.time()

    # Calculate the processing time
    processing_time = end_time - start_time

    # Check if the request was successful
    if response.status_code == 200:
        response_data = response.json()
        
        # Clean up the response (remove <think> tags and empty lines)
        cleaned_response = '\n'.join(
            line for line in response_data.get('response', '').split('\n') if line.strip() != ''
        ).replace('<think>', '').replace('</think>', '')
        
        return f"{cleaned_response}\n\nProcessing time: {processing_time:.2f} seconds"
    else:
        return f"Error: Unable to get response from Ollama API. Status code {response.status_code}\nProcessing time: {processing_time:.2f} seconds"

# Create the Gradio interface with a panel on the right side
with gr.Blocks() as interface:
    with gr.Row():
        gr.Markdown("# Deepseek ChatBot\nEnter your query below and get responses from the Deepseek model.", elem_id="centered-markdown")
    
    with gr.Row():
        with gr.Column(scale=3):
            query_input = gr.Textbox(label="Enter your query")
            response_output = gr.Textbox(label="Response", interactive=False)
        with gr.Column(scale=1):
            model_dropdown = gr.Dropdown(
            choices=["deepseek-r1:1.5b", "deepseek-r1:7b"],
            value="deepseek-r1:1.5b",
            label="Model"
            )
            max_tokens_slider = gr.Slider(
            minimum=1, maximum=1500, value=50, step=1, label="Max Tokens"
            )
            temperature_slider = gr.Slider(
            minimum=0.0, maximum=1.0, value=0.7, step=0.1, label="Temperature"
            )
            top_p_slider = gr.Slider(
            minimum=0.0, maximum=1.0, value=0.9, step=0.1, label="Top P"
            )
            submit_button = gr.Button("Submit")

    submit_button.click(
        respond_to_query,
        inputs=[query_input, model_dropdown, max_tokens_slider, temperature_slider, top_p_slider],
        outputs=response_output
    )

# Launch the Gradio app
if __name__ == "__main__":
    interface.launch(server_name="0.0.0.0", server_port=7860)
