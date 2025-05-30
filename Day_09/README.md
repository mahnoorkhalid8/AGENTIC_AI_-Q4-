# Tool Calling / Function Calling

This README explains the concept of **Tool Calling** and **Function Calling** in **Agentic AI**, using simplified examples.

---

## 📌 What is Function Calling?

**Function Calling** means:

> Manually calling a function in your code to perform a task.

### 🔹 Example:

```python
def add(a, b):
    return a + b

result = add(2, 3)  # ← This is function calling
```

* ✅ Simple
* ✅ Manual
* ❌ No AI involved

---

## 🔧 What is Tool Calling?

**Tool Calling** means:

> When an AI Agent or LLM (like ChatGPT) automatically calls a **registered tool/function** based on the user’s input.

### 🔹 Example:

```python
@tool
def get_weather(city):
    return f"Weather in {city} is sunny."
```

**User:** "Tell me the weather in Lahore"

**Agent:** Automatically calls:

```python
get_weather("Lahore")
```

And responds: "Weather in Lahore is sunny."

* ✅ AI involved
* ✅ Automatic decision-making
* ✅ Common in Agentic AI

---

## 🔁 Function Calling vs Tool Calling

| Feature               | Function Calling            | Tool Calling                                  |
| ----------------------| --------------------------- | --------------------------------------------- |
| What is it?           | Manually calling a function | Agent automatically calling a registered tool |
| Who calls it?         | Developer                   | AI Agent / LLM                                |
| Is AI involved?       | No                          | Yes                                           |
| Automatic decision?   | No, manual only             | Yes, AI decides when/how to call              |
| Used in               | Standard coding             | AI workflows / intelligent systems            |

---

## 🧠 What is a Registered Tool?

A **Registered Tool** is a function that you explicitly tell the AI Agent it is allowed to use.

### 🔹 Example:

```python
@tool
def get_weather(city):
    return f"Weather in {city} is sunny."
```

If you don’t register the function (i.e., no `@tool` decorator), the agent won’t know it exists and won’t be able to use it.

---

## 🧩 Behind-the-Scenes: How Tool Calling Works

1. **User says:** "Convert 100 USD to PKR"
2. **Agent thinks:** "I should use a function like `convert_currency()`"
3. **Agent calls:**

```python
convert_currency("USD", "PKR", 100)
```

4. **Tool returns result:** `27,500 PKR`
5. **Agent replies:** "100 USD is approximately 27,500 PKR"

All of this happens automatically behind the scenes.

---

## 🔍 Final Summary

| Term                 | Meaning                                  |
| -------------------- | ---------------------------------------- |
| **Function**         | A normal function in your code           |
| **Function Calling** | Manually invoking a function             |
| **Tool**             | A function exposed to the AI agent       |
| **Tool Calling**     | AI automatically using a registered tool |
| **Registered Tool**  | A function declared for Agent use        |

---

## ✅ Final Verdict

> Every **Tool Calling involves Function Calling**,
> but not every **Function Calling is Tool Calling**.

Tool Calling is a feature of **Agentic AI** where the system decides when and how to call tools to complete tasks intelligently.

---

**🎉 DONE — This README fully explains Tool Calling vs Function Calling.**
