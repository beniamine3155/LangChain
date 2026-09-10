# LangChain Comprehensive Learning Repository

Welcome! This repository is a **complete guide to mastering LangChain**, an open-source framework for building production-ready applications powered by Large Language Models (LLMs). It covers foundational concepts through advanced LangChain v1 features.

---

##  What is LangChain?

LangChain is a framework that simplifies building AI-powered applications by providing abstractions for:
- **Models**: Connect to LLMs, Chat Models, and Embedding Models from multiple providers
- **Prompts**: Create dynamic, reusable, and context-aware prompts
- **Chains**: Combine multiple components into workflows
- **Agents**: Build autonomous systems that decide which tools to use dynamically
- **Tools**: Enable agents to interact with external APIs and systems
- **Memory**: Maintain conversation context and state
- **Indexes & Retrievers**: Implement Retrieval-Augmented Generation (RAG)
- **Middleware**: Control, track, and transform agent behavior
- **Structured Output**: Return predictable, validated data formats

---

##  LangChain v1 Updates

This repository covers both **foundational concepts** and **LangChain v1 updates** including:
-  **New `create_agent()` API** - Simplified agent creation with built-in tool support
-  **Structured Output** - Return Pydantic models, JSON, and TypedDicts instead of raw text
-  **Streaming Improvements** - Enhanced `.stream()` and `.batch()` methods
-  **Middleware System** - Control agent behavior with Summarization, HumanInLoop, and custom middleware
-  **Message Integration** - Work with `HumanMessage`, `AIMessage`, `SystemMessage` objects
-  **Enhanced Model Integration** - Unified `init_chat_model()` for all providers
-  **Advanced Prompt Templates** - Support for dynamic prompt creation and variables

---

##  Repository Structure

```
LangChain/
├── 00_Updated_LangChain/          #  LangChain v1 Features
│   ├── 01_agent_overview.ipynb    # create_agent() API, tool binding
│   ├── 02_models_integration.ipynb # Unified model init, streaming, batch
│   ├── 04_structure_output.ipynb  # Pydantic, JSON, TypedDict outputs
│   └── 05_middleware.ipynb        # Summarization, HumanInLoop middleware
│
├── 01_Langchain_Models/            # Foundational: Model Integration
│   ├── 01_LLMS/
│   │   └── openai.py              # LLM Integration
│   ├── 02_ChatModels/             # Chat Models from various providers
│   │   ├── 01_openai_chatModel.py
│   │   ├── 02_groq_chatmodel.py
│   │   ├── 03_anthropic_chatmodel.py
│   │   ├── 04_google_chatmodel.py
│   │   ├── 05_hf_api_chatmodel.py
│   │   ├── 06_hf_local_chatmodel.py
│   │   ├── 07_chat_model_conversation.py
│   │   └── 08_chat_model_firebase.py
│   └── 03_Embedding_Models/       # Text-to-Vector conversions
│       ├── 01_openai_em.py
│       ├── 02_openai_em_doc.py
│       └── 03_hf_embedding.py
│
├── 02_Langchain_Prompts/           # Foundational: Prompt Engineering
│   ├── chatbot.py
│   ├── chatprompt_template.py
│   ├── message_template.py         # Message-based prompts
│   ├── messages.py
│   ├── prompt_generator.py
│   └── prompt_ui.py
│
├── 03_Langchain_Structured_Output/ # Foundational: Output Formats
│   ├── json_schema.py
│   ├── json_structured_output.py
│   ├── pydantic_demo.py
│   ├── pydantic_structure_output.py
│   ├── typeddict_demo.py
│   └── typeddict_structure_output.py
│
├── 04_Langchain_Ourput_Parser/     # Foundational: Parsing Outputs
│   ├── jsonoutput_parser.py
│   ├── pydanticoutput_parser.py
│   └── stroutput_parser.py
│
├── 05_Langchain_chain/             # Foundational: Chains
│   ├── conditional_chain.py        # Run chains based on conditions
│   ├── parallel_chain.py           # Run multiple chains simultaneously
│   ├── sequential_chain.py         # Sequential execution
│   └── simple_chain.py
│
├── 06_Langchain_Document_Loaders/  # Foundational: Loading Data
│   ├── csv_loader.py
│   ├── directory_loader.py
│   ├── pdf_loader.py
│   ├── text_loader.py
│   ├── webbase_loader.py
│   ├── fruit.txt
│   ├── Social_Network_Ads.csv
│   └── books/
│
├── 07_Langchain_TextSplitter/      # Foundational: Text Processing
│   ├── length_based.py
│   ├── markdown.py
│   ├── python_code.py
│   ├── semantic.py
│   └── text_structure_based.py
│
├── 08_Vector_Store/                # Foundational: Vector Databases
│   ├── chromadb.ipynb              # ChromaDB implementation
│   └── my_chroma_db/               # Vector storage
│
├── 09_Langchain_Retrievers/        # Foundational: RAG Retrievers
│   └── retrievers.ipynb
│
├── 10_Langchain_Tools/             # Foundational: Tool Integration
│   └── tools.ipynb
│
└── Langchain_Components.ipynb       # Overview of all components
```

---

##  Core Concepts & Components

### 1. **Models & Model Integration** 
**Folder**: `01_Langchain_Models/`  
**New in v1**: `00_Updated_LangChain/02_models_integration.ipynb`

Learn how to connect to different LLM providers:
- **LLMs**: Basic text generation models (OpenAI GPT, Claude, LLaMA)
- **Chat Models**: Conversation-optimized models from OpenAI, Groq, Anthropic, Google, HuggingFace
- **Embedding Models**: Convert text to vectors for similarity search
- **New `init_chat_model()`**: Unified API to instantiate any chat model with configuration
- **Streaming & Batch**: Process multiple requests efficiently with `.stream()` and `.batch()`

**Example**:
```python
from langchain.chat_models import init_chat_model

# LangChain v1: Unified model initialization
model = init_chat_model("gpt-4.1", temperature=0.7, max_tokens=100)
response = model.invoke("Your prompt here")
```

---

### 2. **Prompts & Messages**
**Folder**: `02_Langchain_Prompts/`  
**New in v1**: `00_Updated_LangChain/02_models_integration.ipynb` (Messages section)

Master prompt engineering:
- **ChatPromptTemplate**: Create reusable, dynamic prompts
- **Message Types**: `SystemMessage`, `HumanMessage`, `AIMessage` for conversation flow
- **Few-Shot Prompting**: Provide examples to guide model behavior
- **Role-Based Prompts**: Assign personas to customize responses
- **Prompt Serialization**: Save and load prompt configurations

**Example**:
```python
from langchain_core.prompts import ChatPromptTemplate
from langchain.messages import SystemMessage, HumanMessage

messages = [
    SystemMessage("You are a helpful assistant."),
    HumanMessage("Translate this to French: Hello")
]
response = model.invoke(messages)
```

---

### 3. **Chains**
**Folder**: `05_Langchain_chain/`

Build multi-step workflows:
- **Sequential Chains**: Execute steps one after another
- **Parallel Chains**: Run multiple chains simultaneously with `RunnableParallel`
- **Conditional Chains**: Branch execution based on conditions
- **Chain Composition**: Use the `|` (pipe) operator to connect components

**Example**:
```python
# LangChain's composition operator
chain = prompt | model | output_parser
result = chain.invoke({"topic": "AI"})
```

---

### 4. **Output Parsing**
**Folder**: `04_Langchain_Ourput_Parser/` & `03_Langchain_Structured_Output/`  
**New in v1**: `00_Updated_LangChain/04_structure_output.ipynb`

Get structured data from models:
- **StrOutputParser**: Extract plain text
- **JsonOutputParser**: Parse JSON responses
- **PydanticOutputParser**: Validate against Pydantic models
- **Structured Output (v1)**: Return Pydantic models, JSON, TypedDict directly from agents
- **Schema Definition**: Define expected output structure with Pydantic

**Example (LangChain v1)**:
```python
from pydantic import BaseModel, Field
from langchain.agents import create_agent

class ContactInfo(BaseModel):
    name: str = Field(description="Person's name")
    email: str = Field(description="Email address")
    phone: str = Field(description="Phone number")

agent = create_agent(
    model="gpt-4o",
    response_format=ContactInfo  # Auto-structured output
)
```

---

### 5. **Document Loaders & Text Splitters**
**Folders**: `06_Langchain_Document_Loaders/`, `07_Langchain_TextSplitter/`

Load and prepare data for RAG:
- **Document Loaders**: Load from PDF, CSV, Web, Directory, Text files
- **Text Splitters**: Split large documents while preserving meaning
  - `LengthBasedSplitter`: Split by character count
  - `MarkdownSplitter`: Respect markdown structure
  - `RecursiveCharacterSplitter`: Smart hierarchical splitting
  - `SemanticSplitter`: Split by semantic similarity

---

### 6. **Vector Stores & Retrievers**
**Folders**: `08_Vector_Store/`, `09_Langchain_Retrievers/`

Implement Retrieval-Augmented Generation (RAG):
- **ChromaDB**: Lightweight vector database for embeddings
- **Vector Storage**: Store document embeddings for similarity search
- **Retrievers**: Query vector stores to get relevant documents
- **Integration**: Connect retrievers with agents for knowledge-augmented responses

---

### 7. **Agents & Tool Calling**
**Folder**: `10_Langchain_Tools/`  
**New in v1**: `00_Updated_LangChain/01_agent_overview.ipynb`

Build autonomous AI systems:
- **create_agent() API (v1)**: Simplified agent creation
- **Tool Definition**: Bind Python functions as tools
- **Tool Calling**: Agents automatically select and call appropriate tools
- **System Prompts**: Guide agent behavior with instructions

**Example (LangChain v1)**:
```python
from langchain.agents import create_agent

def get_weather(city: str) -> str:
    """Get weather for a city"""
    return f"{city} is sunny"

agent = create_agent(
    model="gpt-4o",
    tools=[get_weather],
    system_prompt="You are a helpful assistant"
)

result = agent.invoke({"messages": [{"role": "user", "content": "What's the weather?"}]})
```

---

### 8. **Structured Output** (New in LangChain v1)
**Notebook**: `00_Updated_LangChain/04_structure_output.ipynb`

Return validated, structured data from agents:
- **Pydantic Models**: Rich type validation with field descriptions
- **JSON Schemas**: Define expected output structure
- **TypedDict**: Lightweight structured output
- **Agent Integration**: Combine structured output with agent tool calling

---

### 9. **Middleware** (New in LangChain v1)
**Notebook**: `00_Updated_LangChain/05_middleware.ipynb`

Control and enhance agent behavior:

**Summarization Middleware**:
- Automatically compress conversation history when approaching token limits
- Preserve recent messages while compressing older context
- Useful for long-running conversations

**HumanInLoop Middleware**:
- Pause agent execution for human approval
- Review tool calls before execution
- Allow editing or rejecting actions

**Custom Middleware**:
- Add logging and analytics
- Transform prompts and outputs
- Implement rate limiting and guardrails
- Add retry logic and fallbacks

**Example**:
```python
from langchain.agents import create_agent
from langchain.agents.middleware import SummarizationMiddleware
from langgraph.checkpoint.memory import InMemorySaver

agent = create_agent(
    model="gpt-4o",
    tools=[my_tool],
    checkpointer=InMemorySaver(),
    middleware=[
        SummarizationMiddleware(
            model="gpt-4o",
            trigger=("tokens", 550),
            keep=("tokens", 200)
        )
    ]
)
```

---

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.9+
- API keys for LLM providers (OpenAI, Groq, Anthropic, etc.)

### Install Dependencies

```bash
# Using pip
pip install --upgrade langchain langchain-openai langchain-groq langchain-anthropic
pip install python-dotenv pydantic

# Using uv (faster)
uv sync

# Using poetry
poetry install
```

### Environment Setup

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=sk-...
GROQ_API_KEY=gsk-...
ANTHROPIC_API_KEY=sk-ant-...
# Add other provider API keys as needed
```

---

##  Learning Path

### **Beginner** - Start Here
1. Read `Langchain_Components.ipynb` - Overview of all components
2. Explore `01_Langchain_Models/` - Understand different model types
3. Study `02_Langchain_Prompts/` - Create your first prompts
4. Practice `05_Langchain_chain/` - Build simple chains

### **Intermediate** - Build Skills
1. Master `06_Langchain_Document_Loaders/` - Load custom data
2. Implement `07_Langchain_TextSplitter/` - Chunk documents efficiently
3. Build `08_Vector_Store/` - Create semantic search
4. Study `10_Langchain_Tools/` - Create custom tools

### **Advanced** - Master v1 Features
1. Learn `00_Updated_LangChain/01_agent_overview.ipynb` - New agent API
2. Implement `00_Updated_LangChain/04_structure_output.ipynb` - Structured outputs
3. Master `00_Updated_LangChain/05_middleware.ipynb` - Control agent behavior
4. Build production systems with error handling and monitoring

---

##  Key Takeaways

| Concept | Purpose | Files |
|---------|---------|-------|
| **Models** | Connect to LLMs and generate responses | `01_Langchain_Models/` |
| **Prompts** | Create reusable, dynamic instructions | `02_Langchain_Prompts/` |
| **Chains** | Combine components into workflows | `05_Langchain_chain/` |
| **Output Parsers** | Extract structured data from responses | `04_Langchain_Ourput_Parser/` |
| **Document Loaders** | Load data from various sources | `06_Langchain_Document_Loaders/` |
| **Text Splitters** | Prepare documents for embeddings | `07_Langchain_TextSplitter/` |
| **Vector Stores** | Store embeddings for similarity search | `08_Vector_Store/` |
| **Retrievers** | Query vector stores for relevant docs | `09_Langchain_Retrievers/` |
| **Agents** (v1) | Build autonomous systems with tools | `00_Updated_LangChain/01_agent_overview.ipynb` |
| **Structured Output** (v1) | Return validated data formats | `00_Updated_LangChain/04_structure_output.ipynb` |
| **Middleware** (v1) | Control and monitor agent behavior | `00_Updated_LangChain/05_middleware.ipynb` |

---

##  Examples in This Repository

Every folder contains **runnable code examples** demonstrating:
-  How to instantiate each component
-  Different configuration options
-  Real-world use cases
-  Best practices and common patterns
-  Error handling and edge cases

Simply navigate to any folder and run:
```bash
python filename.py  # For Python scripts
# or open .ipynb in Jupyter/VS Code for notebooks
```

---

##  Additional Resources

- **Official Docs**: https://python.langchain.com/
- **LangChain GitHub**: https://github.com/langchain-ai/langchain
- **API Reference**: https://api.python.langchain.com/
- **Community**: https://discord.gg/langchain
- **Blog**: https://blog.langchain.dev/


