# Agent AI SDK:
## Q1. Why is the Agent class defined as a dataclass?
The Agent class is defined as a dataclass because it primarily holds data such as the name, instructions (system prompt), and possibly other configuration values. Using Python’s @dataclass decorator:
Automatically generates methods like __init__(), __repr__(), and __eq__().
Makes the code cleaner and avoids writing repetitive boilerplate code.

#### Example:
Imagine you’re storing recipe details in a class:

from dataclasses import dataclass

@dataclass
class Recipe:
    name: str
    ingredients: list
    
Now you can just create an instance like:

cake = Recipe("Chocolate Cake", ["Flour", "Sugar", "Cocoa"])
No need to define an __init__() manually.

## 2a. Why is the system prompt stored in the Agent class as instructions and made callable?
The system prompt (instructions) in the Agent class is often the AI’s background context — like telling the assistant "You are a helpful bot."
By making the Agent class callable (using the __call__ method), it becomes easier to use the agent like a function:

response = agent("What's the weather?")
This improves usability by allowing the agent object to behave like a callable tool, abstracting away the internal complexity of how messages are constructed and processed.

Think of it like a blender: whether you're blending fruits or milk, you just press one button (call the agent) and it does the rest internally.

## 2b. Why is the user prompt passed to Runner.run() and why is run() a @classmethod?
The user prompt is dynamic input — meaning it changes every time the agent is called. So instead of hardcoding it in the class, it's passed as a parameter to run().

The run() method is a @classmethod so that it can be used without needing an instance of Runner. This is useful when you want to run agents in a stateless or utility-like way, managing the full agent lifecycle without creating a Runner object manually.

Why not an instance method?
Because run() is mostly used as a high-level entry point and not tied to a specific Runner instance.

## 3. What is the purpose of the Runner class?
The Runner class is responsible for executing the agent logic. It acts like the engine that:
1. Accepts user input (prompt)
2. Manages the flow of conversation or task
3. Runs the agent with all necessary context
4. Returns the response from the model

In simple terms, if the Agent is your smart assistant, the Runner is the one pressing the buttons and handling the tools to get things done.

You can think of it like a chef (Runner) who knows how to use the recipe (Agent) to prepare a dish (final output).

## 4. What are Generics in Python and why use TContext?
Generics in Python (using TypeVar) allow you to write flexible and reusable code by not locking you into one specific data type.

TContext is a placeholder type that lets you customize what type of context your agent might expect (e.g., user session, settings, history). You define it once and reuse it wherever needed, while still getting type hints and checks from tools like mypy.

Example:

from typing import TypeVar, Generic

TContext = TypeVar("TContext")

class MyAgent(Generic[TContext]):
    def __init__(self, context: TContext):
        self.context = context
This allows different developers to pass any context (like a dictionary, a class, or config) and still maintain type safety.

Real-life analogy:
It’s like writing a recipe that works for any ingredients you give (instead of forcing chocolate every time). You can reuse the recipe for banana, vanilla, etc., while still knowing what to expect.
