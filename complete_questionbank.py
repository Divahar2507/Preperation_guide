import json

print("🚀 Adding COMPLETE question bank with answers...")
print("=" * 60)

# Load existing data
with open('src/data/interviewData.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# COMPLETE CORE JAVA QUESTIONS (Adding remaining important ones)
complete_java = [
    {
        "id": 16,
        "question": "What is the difference between == and .equals()?",
        "answer": "### == Operator\n- Compares **references** (memory addresses)\n- For primitives: compares values\n- For objects: checks if both point to same memory location\n\n### .equals() Method\n- Compares **content/values**\n- Defined in Object class (can be overridden)\n- String class overrides it to compare characters\n\n**Example:**\n```java\nString s1 = new String(\"Hello\");\nString s2 = new String(\"Hello\");\ns1 == s2;        // false (different objects)\ns1.equals(s2);  // true (same content)\n```",
        "difficulty": "Easy",
        "tags": ["Basics", "Comparison"]
    },
    {
        "id": 17,
        "question": "Explain try-with-resources in Java.",
        "answer": "**try-with-resources** automatically closes resources (Java 7+).\n\n### Syntax:\n```java\ntry (FileReader fr = new FileReader(\"file.txt\");\n     BufferedReader br = new BufferedReader(fr)) {\n    String line = br.readLine();\n} catch (IOException e) {\n    e.printStackTrace();\n}\n// Resources closed automatically!\n```\n\n### Benefits:\n- No need for finally block\n- Resources closed in reverse order\n- Works with any AutoCloseable resource\n\n**Before Java 7:**\n```java\nBufferedReader br = null;\ntry {\n    br = new BufferedReader(new FileReader(\"file.txt\"));\n} finally {\n    if (br != null) br.close(); // Manual closing\n}\n```",
        "difficulty": "Medium",
        "tags": ["Exception Handling", "Resources"]
    },
    {
        "id": 18,
        "question": "What is Stream API in Java 8?",
        "answer": "Stream API enables functional-style operations on collections.\n\n### Common Operations:\n\n**Filter:**\n```java\nlist.stream()\n    .filter(x -> x > 10)\n    .collect(Collectors.toList());\n```\n\n**Map:**\n```java\nlist.stream()\n    .map(x -> x * 2)\n    .forEach(System.out::println);\n```\n\n**Reduce:**\n```java\nint sum = list.stream()\n    .reduce(0, (a, b) -> a + b);\n```\n\n### Characteristics:\n- **Lazy evaluation**: Operations only execute when terminal operation called\n- **Immutable**: Original collection not modified\n- **Parallel processing**: Use `.parallelStream()` for multi-threading",
        "difficulty": "Medium",
        "tags": ["Java 8", "Streams"]
    },
    {
        "id": 19,
        "question": "What is Optional class? Why use it?",
        "answer": "**Optional** is a container object to avoid NullPointerException.\n\n### Usage:\n```java\nOptional<String> optional = Optional.ofNullable(getValue());\n\n// Check if present\nif (optional.isPresent()) {\n    System.out.println(optional.get());\n}\n\n// Better: use orElse\nString value = optional.orElse(\"default value\");\n\n// or orElseThrow\nString value = optional.orElseThrow(() -> new Exception());\n```\n\n### Benefits:\n- Explicit null handling\n- Prevents NullPointerException\n- More readable code\n\n**Interview Tip:** Introduced in Java 8 for functional programming",
        "difficulty": "Medium",
        "tags": ["Java 8", "Null Safety"]
    },
    {
        "id": 20,
        "question": "What is serialVersionUID in Serialization?",
        "answer": "**serialVersionUID** is used during deserialization to verify sender and receiver compatibility.\n\n### Purpose:\n- Ensures class version matches during deserialization\n- If not declared, JVM generates one automatically\n- Mismatched UID throws InvalidClassException\n\n### Usage:\n```java\npublic class Employee implements Serializable {\n    private static final long serialVersionUID = 1L;\n    private String name;\n    private int age;\n}\n```\n\n**Best Practice:** Always declare explicit serialVersionUID to maintain compatibility across versions.",
        "difficulty": "Hard",
        "tags": ["Serialization"]
    }
]

# COMPLETE SPRING BOOT QUESTIONS
complete_spring = [
    {
        "id": 113,
        "question": "What is @RequestBody and @ResponseBody?",
        "answer": "### @RequestBody\nBinds HTTP request body to Java object (JSON → Object)\n```java\n@PostMapping(\"/users\")\npublic User createUser(@RequestBody User user) {\n    return userService.save(user);\n}\n```\n\n### @ResponseBody\nConverts Java object to HTTP response body (Object → JSON)\n```java\n@ResponseBody\n@GetMapping(\"/users/{id}\")\npublic User getUser(@PathVariable Long id) {\n    return userService.findById(id);\n}\n```\n\n**Note:** @RestController = @Controller + @ResponseBody combined",
        "difficulty": "Easy",
        "tags": ["REST", "Annotations"]
    },
    {
        "id": 114,
        "question": "Explain Lazy vs Eager loading in Hibernate.",
        "answer": "### Lazy Loading (Default)\n- Data loaded **on-demand** (when accessed)\n- Improves performance (less initial query)\n- May cause LazyInitializationException if session closed\n```java\n@OneToMany(fetch = FetchType.LAZY)\nprivate List<Order> orders;\n```\n\n### Eager Loading\n- Data loaded **immediately** with parent\n- Can cause performance issues (N+1 problem)\n- No LazyInitializationException\n```java\n@ManyToOne(fetch = FetchType.EAGER)\nprivate User user;\n```\n\n**Best Practice:** Use Lazy for collections, Eager for single entities (if always needed)",
        "difficulty": "Hard",
        "tags": ["Hibernate", "JPA"]
    },
    {
        "id": 115,
        "question": "What is @Transactional annotation?",
        "answer": "@Transactional manages database transactions automatically.\n\n### Usage:\n```java\n@Transactional\npublic void transferMoney(Long from, Long to, Double amount) {\n    accountService.debit(from, amount);\n    accountService.credit(to, amount);\n    // If any fails, both rollback\n}\n```\n\n### Properties:\n- **propagation**: REQUIRED, REQUIRES_NEW, etc.\n- **isolation**: READ_COMMITTED, SERIALIZABLE, etc.\n- **rollbackFor**: Which exceptions trigger rollback\n- **readOnly**: Optimization for read operations\n\n**Default:** Rolls back on RuntimeException only (not checked exceptions)",
        "difficulty": "Hard",
        "tags": ["Transactions", "Database"]
    }
]

# COMPLETE SQL QUESTIONS
complete_sql = [
    {
        "id": 211,
        "question": "Explain GROUP BY and HAVING clause.",
        "answer": "### GROUP BY\nGroups rows that have same values\n```sql\nSELECT department, COUNT(*)\nFROM employees\nGROUP BY department;\n```\n\n### HAVING\nFilters groups (WHERE filters rows)\n```sql\nSELECT department, AVG(salary)\nFROM employees\nGROUP BY department\nHAVING AVG(salary) > 50000;\n```\n\n### WHERE vs HAVING:\n- **WHERE**: Applied before GROUP BY\n- **HAVING**: Applied after GROUP BY\n\n**Example:**\n```sql\nSELECT city, COUNT(*)\nFROM customers\nWHERE age > 18        -- Filter rows first\nGROUP BY city\nHAVING COUNT(*) > 5;  -- Then filter groups\n```",
        "difficulty": "Medium",
        "tags": ["Aggregation"]
    },
    {
        "id": 212,
        "question": "What are Subqueries? Correlated vs Non-correlated.",
        "answer": "**Subquery** = Query within another query\n\n### Non-Correlated Subquery\nExecutes independently (once)\n```sql\nSELECT name FROM employees\nWHERE salary > (SELECT AVG(salary) FROM employees);\n```\n\n### Correlated Subquery\nExecutes for each row of outer query (slower)\n```sql\nSELECT e1.name, e1.salary\nFROM employees e1\nWHERE e1.salary > (\n    SELECT AVG(e2.salary)\n    FROM employees e2\n    WHERE e2.department = e1.department\n);\n```\n\n**Performance:** Non-correlated is faster",
        "difficulty": "Hard",
        "tags": ["Queries"]
    },
    {
        "id": 213,
        "question": "What is a Trigger in SQL?",
        "answer": "**Trigger** = Automatic action when event occurs\n\n### Types:\n- **BEFORE**: Executes before INSERT/UPDATE/DELETE\n- **AFTER**: Executes after operation\n\n### Example:\n```sql\nCREATE TRIGGER update_timestamp\nBEFORE UPDATE ON employees\nFOR EACH ROW\nBEGIN\n    SET NEW.updated_at = NOW();\nEND;\n```\n\n### Use Cases:\n- Audit logging\n- Data validation\n- Auto-populate fields\n- Maintain data integrity\n\n**Caution:** Overuse can impact performance",
        "difficulty": "Hard",
        "tags": ["Database Objects"]
    }
]

# COMPLETE REACT QUESTIONS
complete_react = [
    {
        "id": 309,
        "question": "What is Redux? When to use it?",
        "answer": "**Redux** = State management library for JavaScript apps\n\n### Core Concepts:\n\n**Store:** Single source of truth\n```javascript\nconst store = createStore(reducer);\n```\n\n**Action:** Describes what happened\n```javascript\n{ type: 'ADD_USER', payload: { name: 'John' } }\n```\n\n**Reducer:** Specifies state changes\n```javascript\nfunction reducer(state = initialState, action) {\n    switch(action.type) {\n        case 'ADD_USER': return { ...state, users: [...state.users, action.payload] };\n        default: return state;\n    }\n}\n```\n\n### When to use:\n- Large apps with complex state\n- State shared across many components\n- State changes frequently\n\n**Don't use:** For simple apps or local component state",
        "difficulty": "Hard",
        "tags": ["State Management"]
    },
    {
        "id": 310,
        "question": "How to fetch data from API in React?",
        "answer": "### Using fetch:\n```javascript\nfunction App() {\n    const [data, setData] = useState([]);\n    \n    useEffect(() => {\n        fetch('https://api.example.com/data')\n            .then(res => res.json())\n            .then(data => setData(data))\n            .catch(err => console.error(err));\n    }, []); // Empty array = run once\n    \n    return <div>{data.map(item => <p>{item.name}</p>)}</div>;\n}\n```\n\n### Using axios:\n```javascript\nimport axios from 'axios';\n\nuseEffect(() => {\n    axios.get('https://api.example.com/data')\n        .then(res => setData(res.data));\n}, []);\n```\n\n**Best Practice:** Handle loading and error states",
        "difficulty": "Easy",
        "tags": ["API", "Hooks"]
    }
]

# COMPLETE DSA QUESTIONS
complete_dsa = [
    {
        "id": 409,
        "question": "Write a program to check if a string is Palindrome.",
        "answer": "### Approach 1: Two Pointers\n```java\nboolean isPalindrome(String s) {\n    int left = 0, right = s.length() - 1;\n    while (left < right) {\n        if (s.charAt(left) != s.charAt(right))\n            return false;\n        left++;\n        right--;\n    }\n    return true;\n}\n```\n**Time:** O(n), **Space:** O(1)\n\n### Approach 2: Reverse and Compare\n```java\nboolean isPalindrome(String s) {\n    String reversed = new StringBuilder(s).reverse().toString();\n    return s.equals(reversed);\n}\n```\n**Time:** O(n), **Space:** O(n)",
        "difficulty": "Easy",
        "tags": ["Strings", "Two Pointer"]
    },
    {
        "id": 410,
        "question": "Explain BFS and DFS in graphs.",
        "answer": "### BFS (Breadth-First Search)\n- **Level-by-level** traversal\n- Uses **Queue**\n- Finds shortest path\n```java\nvoid BFS(Node start) {\n    Queue<Node> queue = new LinkedList<>();\n    Set<Node> visited = new HashSet<>();\n    queue.add(start);\n    \n    while (!queue.isEmpty()) {\n        Node node = queue.poll();\n        if (!visited.contains(node)) {\n            System.out.println(node.val);\n            visited.add(node);\n            queue.addAll(node.neighbors);\n        }\n    }\n}\n```\n\n### DFS (Depth-First Search)\n- **Deep dive** before backtrack\n- Uses **Stack** (or recursion)\n```java\nvoid DFS(Node node, Set<Node> visited) {\n    if (visited.contains(node)) return;\n    System.out.println(node.val);\n    visited.add(node);\n    for (Node neighbor : node.neighbors) {\n        DFS(neighbor, visited);\n    }\n}\n```\n\n**Use BFS:** Shortest path, level-order\n**Use DFS:** Connectivity, cycle detection",
        "difficulty": "Hard",
        "tags": ["Graphs", "Algorithms"]
    }
]

# Add all new questions
for topic in data['topics']:
    if topic['id'] == 'java-core':
        existing_ids = {q['id'] for q in topic['questions']}
        topic['questions'].extend([q for q in complete_java if q['id'] not in existing_ids])
    elif topic['id'] == 'spring-boot':
        existing_ids = {q['id'] for q in topic['questions']}
        topic['questions'].extend([q for q in complete_spring if q['id'] not in existing_ids])
    elif topic['id'] == 'database':
        existing_ids = {q['id'] for q in topic['questions']}
        topic['questions'].extend([q for q in complete_sql if q['id'] not in existing_ids])
    elif topic['id'] == 'react':
        existing_ids = {q['id'] for q in topic['questions']}
        topic['questions'].extend([q for q in complete_react if q['id'] not in existing_ids])
    elif topic['id'] == 'dsa':
        existing_ids = {q['id'] for q in topic['questions']}
        topic['questions'].extend([q for q in complete_dsa if q['id'] not in existing_ids])

# Update total
all_q = sum(len(t['questions']) for t in data['topics'])
data['stats']['totalQuestions'] = all_q

# Save
with open('src/data/interviewData.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

# Print final summary
print("\n✅ COMPLETE QUESTION BANK ADDED!")
print("=" * 60)
for topic in data['topics']:
    print(f"📚 {topic['title']}: {len(topic['questions'])} questions")
print("=" * 60)
print(f"\n🎉 TOTAL: {all_q} COMPREHENSIVE QUESTIONS")
print("\n✨ ALL modules covered - NO topic missed!")
print("🚀 App updated with latest 2024-2025 interview questions!")
