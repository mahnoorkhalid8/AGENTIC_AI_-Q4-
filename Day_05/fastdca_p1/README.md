# Dependency Injection:
Dependency Injection is a programming technique where required objects or values (called dependencies) are provided to a function or class from the outside, rather than being created inside it.

## Benefits of Dependency Injection:
1. Reusability – Dependencies can be reused across multiple parts of the app.
2. Modularity – Keeps code clean and separated; each part focuses on one task.
3. Testability – Makes it easier to test by injecting mock or fake dependencies.
4. Maintainability – Easier to update or change a dependency in one place.
5. Flexibility – You can easily switch between different versions of a dependency.

## 🔧 Features Explained
1. Simple Dependency
2. Dependency with Parameters
3. Login with Dependency
4. Multiple Dependencies in One Route
5. Class-Based Dependency with Error Handling

### Endpoints
/get-simple-goal → Returns a simple static message.

/get-goal?username=... → Dynamic goal message with username.

/signin?username=...&password=... → Simulated login system.

/main/{num} → Adds multiple dependency-returned values to num.

/blog/{id} → Fetch blog name by ID or raise 404.

/user/{id} → Fetch user name by ID or raise 404.
