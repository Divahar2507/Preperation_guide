import json

# Load existing data
with open('src/data/interviewData.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Additional Core Java Questions
java_questions = [
    {
        "id": 6,
        "question": "What is the difference between Abstract Class and Interface?",
        "answer": "### Abstract Class\n- Can have abstract AND concrete methods\n- Supports constructors\n- Can have instance variables (state)\n- Use `extends` keyword (single inheritance)\n\n### Interface\n- Only abstract methods (before Java 8)\n- No constructors\n- Only constants (public static final)\n- Use `implements` keyword (multiple inheritance)\n\n**Java 8+ Changes**: Interfaces can now have default and static methods.\n\n**When to use?**\n- Use abstract class when you have common code to share\n- Use interface when you want to define a contract",
        "difficulty": "Medium",
        "tags": ["OOPs", "Interfaces"]
    },
    {
        "id": 7,
        "question": "Explain final, finally, and finalize.",
        "answer": "### final\n- **Keyword** - Variables become constants, methods can't be overridden, classes can't be extended\n- Example: `final int MAX = 100;`\n\n### finally  \n- **Block** in try-catch - Always executes (even if exception occurs)\n- Used for cleanup (close files, DB connections)\n\n### finalize\n- **Method** called by Garbage Collector before destroying object\n- Deprecated in Java 9+\n- Syntax: `protected void finalize() throws Throwable`",
        "difficulty": "Easy",
        "tags": ["Keywords", "Basics"]
    },
    {
        "id": 8,
        "question": "ArrayList vs LinkedList - When to use which?",
        "answer": "### ArrayList\n- **Internal**: Dynamic array\n- **Access**: O(1) - Fast random access by index\n- **Insert/Delete**: O(n) - Slow (shifting needed)\n- **Use when**: More reads, less modifications\n\n### LinkedList\n- **Internal**: Doubly linked list\n- **Access**: O(n) - Sequential traversal needed  \n- **Insert/Delete**: O(1) - Fast (just pointer change)\n- **Use when**: Frequent insertions/deletions\n\n**Memory**: ArrayList uses less memory than LinkedList (no node overhead)",
        "difficulty": "Medium",
        "tags": ["Collections"]
    }
]

# Additional Spring Boot Questions  
spring_questions = [
    {
        "id": 105,
        "question": "What is @Controller vs @RestController?",
        "answer": "### @Controller\n- Returns **View** (HTML pages)\n- Used in MVC pattern with Thymeleaf/JSP\n- Need `@ResponseBody` to return data\n\n### @RestController\n- `@Controller` + `@ResponseBody` combined\n- Returns **JSON/XML** data directly\n- Used for REST APIs\n\n**Example**:\n```java\n@RestController\npublic class UserAPI {\n    @GetMapping(\"/users\")\n    public List<User> getUsers() {\n        return userService.findAll(); // Returns JSON\n    }\n}\n```",
        "difficulty": "Easy",
        "tags": ["Annotations", "REST"]
    },
    {
        "id": 106,
        "question": "Explain Spring Boot Starters.",
        "answer": "Starters are dependency descriptors that simplify Maven/Gradle configuration.\n\n**Common Starters**:\n- `spring-boot-starter-web`: Web + REST (includes Tomcat, Spring MVC, Jackson)\n- `spring-boot-starter-data-jpa`: JPA + Hibernate\n- `spring-boot-starter-security`: Spring Security\n- `spring-boot-starter-test`: JUnit, Mockito, etc.\n\n**Benefits**:\n- One dependency = All required jars\n- Version compatibility managed\n- No dependency hell",
        "difficulty": "Easy",
        "tags": ["Configuration"]
    }
]

# Additional SQL Questions
sql_questions = [
    {
        "id": 204,
        "question": "Explain all types of JOINs with examples.",
        "answer": "### INNER JOIN\nReturns only matching rows from both tables.\n```sql\nSELECT * FROM Orders O \nINNER JOIN Customers C ON O.customer_id = C.id;\n```\n\n### LEFT JOIN\nAll rows from LEFT table + matching from RIGHT (NULL if no match).\n\n### RIGHT JOIN\nAll rows from RIGHT table + matching from LEFT.\n\n### FULL OUTER JOIN\nAll rows from both tables (NULL where no match).\n\n### CROSS JOIN\nCartesian product (every row of table1 × every row of table2).",
        "difficulty": "Medium",
        "tags": ["Joins"]
    },
    {
        "id": 205,
        "question": "What is Normalization? Explain 1NF, 2NF, 3NF.",
        "answer": "Normalization = Organizing data to reduce redundancy.\n\n### 1NF (First Normal Form)\n- Each column has atomic (single) values\n- No repeating groups\n\n### 2NF\n- Must be in 1NF\n- No partial dependency (all non-key attributes fully depend on primary key)\n\n### 3NF\n- Must be in 2NF\n- No transitive dependency (non-key attributes don't depend on other non-key attributes)\n\n**Example**: Student(ID, Name, Course, Instructor, Instructor_Phone)\n- Violates 3NF: Instructor_Phone depends on Instructor, not ID",
        "difficulty": "Hard",
        "tags": ["Database Design"]
    }
]

# Additional React Questions
react_questions = [
    {
        "id": 303,
        "question": "What is Props vs State in React?",
        "answer": "### Props\n- **Passed** from parent to child\n- **Immutable** (read-only in child)\n- Used for component configuration\n\n### State\n- **Internal** to component\n- **Mutable** (can be changed with setState/useState)\n- Triggers re-render when changed\n\n**Analogy**: Props = Function parameters, State = Local variables",
        "difficulty": "Easy",
        "tags": ["Basics"]
    },
    {
        "id": 304,
        "question": "Explain useEffect dependency array.",
        "answer": "The dependency array controls **when** useEffect runs:\n\n### No array (omitted)\n```js\nuseEffect(() => { /* runs on every render */ });\n```\n\n### Empty array `[]`\n```js\nuseEffect(() => { /* runs once on mount */ }, []);\n```\n\n### With dependencies\n```js\nuseEffect(() => { /* runs when count changes */ }, [count]);\n```\n\n**Cleanup**: Return function runs on unmount\n```js\nuseEffect(() => {\n    const timer = setInterval(...);\n    return () => clearInterval(timer); // cleanup\n}, []);\n```",
        "difficulty": "Medium",
        "tags": ["Hooks"]
    }
]

# Additional DSA Questions
dsa_questions = [
    {
        "id": 403,
        "question": "Explain Two Pointer Technique with example.",
        "answer": "Two pointers move through array/string to solve problems efficiently.\n\n**Use Cases**:\n- Finding pairs with target sum\n- Removing duplicates\n- Reversing array\n\n**Example** (Find pair with sum = target):\n```java\nint left = 0, right = arr.length - 1;\nwhile (left < right) {\n    int sum = arr[left] + arr[right];\n    if (sum == target) return true;\n    else if (sum < target) left++;\n    else right--;\n}\n```\n\n**Time**: O(n) instead of O(n²) with nested loops",
        "difficulty": "Medium",
        "tags": ["Techniques"]
    },
    {
        "id": 404,
        "question": "Compare Sorting Algorithms.",
        "answer": "| Algorithm | Best | Average | Worst | Space | Stable |\n|-----------|------|---------|-------|-------|--------|\n| Bubble | O(n) | O(n²) | O(n²) | O(1) | Yes |\n| Quick | O(n log n) | O(n log n) | O(n²) | O(log n) | No |\n| Merge | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |\n| Heap | O(n log n) | O(n log n) | O(n log n) | O(1) | No |\n\n**Use QuickSort** for average cases (fastest in practice)\n**Use MergeSort** when stability needed or guaranteed O(n log n)",
        "difficulty": "Hard",
        "tags": ["Sorting"]
    }
]

# Add questions to respective topics
for topic in data['topics']:
    if topic['id'] == 'java-core':
        topic['questions'].extend(java_questions)
    elif topic['id'] == 'spring-boot':
        topic['questions'].extend(spring_questions)
    elif topic['id'] == 'database':
        topic['questions'].extend(sql_questions)
    elif topic['id'] == 'react':
        topic['questions'].extend(react_questions)
    elif topic['id'] == 'dsa':
        topic['questions'].extend(dsa_questions)

# Update total count
all_q = sum(len(t['questions']) for t in data['topics'])
data['stats']['totalQuestions'] = all_q

# Save
with open('src/data/interviewData.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print(f"✅ Added questions! New total: {all_q}")
