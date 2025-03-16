# LangChain Chatbot (Model: llama3.2)

A simple chatbot application built with LangChain that processes user questions and returns helpful responses.

## Application Flow

The chatbot follows this processing flow:

1. **Prompt Template**: Structures the conversation with:

   - System message: Sets the AI's behavior as a helpful assistant
   - User message: Contains the user's question

2. **Language Model (LLM)**: Processes the formatted prompt and generates a response

3. **Output Parser**: Converts the LLM's response into a clean string format

4. **Chain**: Connects all components using the pipe operator (`|`):
   ```python
   chain = prompt_template | llm | output_parser
   ```

## Environment Setup

The application uses LangChain's tracing functionality for monitoring:

```python
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
```

## Getting Started

1. Create a virtual environment:

   ```
   python -m venv venv
   ```

2. Activate the virtual environment:

   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```
   - On Windows:
     ```
     venv\Scripts\activate
     ```

3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file with your LangChain API key:

   ```
   LANGCHAIN_API_KEY=your_api_key_here
   ```

5. Run the application:
   ```
   python chatbot/app.py
   ```
