# 💬 Streamlit Chat App with A4F API

A beautiful and interactive chat application built with **Streamlit** that connects to the [A4F API](https://a4f.co) for AI-powered conversations. Chat with advanced language models through an intuitive web interface!

---

## ✨ Features

- 🎨 **Modern Streamlit Interface** - Clean, responsive chat UI
- 🤖 **AI-Powered Conversations** - Uses A4F's OpenAI-compatible API
- 💾 **Chat History** - Maintains conversation context throughout your session  
- 🧹 **Clear Chat** - Reset conversations with one click
- 📥 **Export Functionality** - Download your chat history as a text file
- ⚡ **Real-time Responses** - Stream responses with loading indicators
- 🔧 **Error Handling** - Graceful error management and user feedback

---

## 🛠️ Setup & Installation

### 1. Clone this repository
```bash
git clone https://github.com/yourusername/streamlit-chat-app.git
cd streamlit-chat-app
```

### 2. Install required packages
```bash
pip install streamlit openai
```

### 3. Configure your API key
Open `model.py` and replace the API key:
```python
api_key="Your_A4F_API_Key_Here"  # Insert your A4F API key here
```

### 4. (Optional) Customize the model
You can change the model in `model.py`:
```python
model="provider-6/gpt-4o"  # Replace with your preferred model from A4F
```

---

## 🚀 How to Run

Start the Streamlit application:
```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

---

## 📁 Project Structure

```
├── app.py          # Main Streamlit application
├── model.py        # A4F API integration and chat function
└── README.md       # This file
```

### 📄 File Descriptions

- **`model.py`** - Contains the `chat()` function that handles API communication with A4F
- **`app.py`** - Main Streamlit interface with chat UI, history management, and controls

---

## 🎯 Usage

1. **Start chatting** - Type your message in the input box at the bottom
2. **View responses** - AI responses appear in real-time with a loading spinner
3. **Manage history** - Use sidebar controls to clear chat or export conversations
4. **Export chats** - Download your conversation history as a text file

### Example Conversation:
```
👤 User: Hello, how are you?
🤖 Assistant: Hello! I'm doing well, thank you for asking. How can I assist you today?

👤 User: Can you explain quantum computing?
🤖 Assistant: Quantum computing is a revolutionary computing paradigm that...
```

---

## ⚙️ Configuration Options

### Model Settings (in `model.py`)
- **Temperature**: `0.7` (creativity level)
- **Max Tokens**: `50` (response length limit)
- **Stream**: `False` (set to `True` for streaming responses)

### Available Models (A4F)
You can use various models available on A4F:
- `provider-6/gpt-4o`
- `provider-2/gpt-3.5-turbo`
- And many more from the [A4F model list](https://www.a4f.co/models)

---

## 🎨 Customization

### Modify the Interface
Edit `app.py` to customize:
- Page title and icon
- Chat styling and colors
- Sidebar content
- Error messages

### Adjust API Behavior  
Edit `model.py` to modify:
- System prompts
- Response parameters
- Error handling
- Model selection

---

## 🐛 Troubleshooting

### Common Issues:

**API Key Error**
```
Error: Invalid API key
```
- Solution: Ensure your A4F API key is correctly set in `model.py`

**Connection Error**
```
Error: Connection failed
```
- Solution: Check your internet connection and A4F service status

**Module Import Error**
```
ModuleNotFoundError: No module named 'streamlit'
```
- Solution: Install dependencies with `pip install streamlit openai`

---

## 🧰 Technologies Used

- **[Streamlit](https://streamlit.io/)** - Web app framework for Python
- **[OpenAI Python SDK](https://github.com/openai/openai-python)** - API client for OpenAI-compatible endpoints
- **[A4F API](https://a4f.co)** - Language model provider with OpenAI compatibility

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. 🍴 **Fork** this repository
2. 🌿 **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. 💻 **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. 📤 **Push** to the branch (`git push origin feature/amazing-feature`)
5. 🎯 **Open** a Pull Request

### Ideas for Contributions:
- 🎨 UI/UX improvements
- 🔧 New features (voice input, image support, etc.)
- 🐛 Bug fixes and optimizations
- 📚 Documentation improvements

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

## 📩 Contact & Support

- 🐛 **Issues**: [GitHub Issues](https://github.com/yourusername/streamlit-chat-app/issues)
- 💡 **Feature Requests**: Open an issue with the `enhancement` label
- 📧 **Questions**: Feel free to reach out through GitHub discussions

---

## 🌟 Show Your Support

If you found this project helpful, please consider:
- ⭐ **Star** this repository
- 🍴 **Fork** it to create your own version  
- 📢 **Share** it with others

---

**Happy Chatting!** 🚀✨
