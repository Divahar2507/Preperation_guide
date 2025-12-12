import json

# Load existing data
with open('src/data/interviewData.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# COMPREHENSIVE Core Java Questions (add to reach 15 total)
java_new = [
    {
        "id": 9,
        "question": "What is Method Overloading vs Method Overriding?",
        "answer": "### Method Overloading (Compile-time Polymorphism)\n- **Same method name**, different parameters (number, type, order)\n- **Same class**\n- Return type can be different\n- Example:\n```java\nint add(int a, int b)\ndouble add(double a, double b)\nint add(int a, int b, int c)\n```\n\n### Method Overriding (Runtime Polymorphism)\n- **Same method signature** (name + parameters)\n- **Subclass** overrides parent method\n- Must have same return type\n- Example:\n```java\nclass Animal { void sound() { } }\nclass Dog extends Animal { void sound() { sysout('Bark'); } }\n```",
        "difficulty": "Medium",
        "tags": ["OOPs", "Polymorphism"]
    },
    {
        "id": 10,
        "question": "Explain static keyword in Java.",
        "answer": "**static** belongs to CLASS, not instance.\n\n### Static Variable\n- Shared among all objects\n- Memory allocated once\n```java\nstatic int count = 0;\n```\n\n### Static Method\n- Can be called without object\n- Can only access static members\n```java\nMath.sqrt(25); // static method\n```\n\n### Static Block\n- Executes when class is loaded\n```java\nstatic { System.out.println(\"Class loaded\"); }\n```\n\n**Why main is static?** JVM can call it without creating object.",
        "difficulty": "Easy",
        "tags": ["Keywords"]
    },
    {
        "id": 11,
        "question": "What is Exception Handling? Checked vs Unchecked.",
        "answer": "Exception = Abnormal condition disrupting program flow.\n\n### Checked Exceptions\n- Checked at **compile-time**\n- Must handle with try-catch or throws\n- Examples: IOException, SQLException\n\n### Unchecked Exceptions\n- Checked at **runtime**\n- Not mandatory to handle\n- Examples: NullPointerException, ArrayIndexOutOfBoundsException\n\n### Hierarchy\n```\nThrowable\n├── Error (OutOfMemoryError)\n└── Exception\n    ├── RuntimeException (Unchecked)\n    └── IOException (Checked)\n```",
        "difficulty": "Medium",
        "tags": ["Exception Handling"]
    },
    {
        "id": 12,
        "question": "What is multithreading? Thread vs Runnable.",
        "answer": "Multithreading = Multiple threads executing concurrently.\n\n### Thread Class\n```java\nclass MyThread extends Thread {\n    public void run() { /* code */ }\n}\nMyThread t = new MyThread();\nt.start();\n```\n\n### Runnable Interface (Preferred)\n```java\nclass MyRunnable implements Runnable {\n    public void run() { /* code */ }\n}\nThread t = new Thread(new MyRunnable());\nt.start();\n```\n\n**Why Runnable better?**\n- Java doesn't support multiple inheritance\n- More flexible design",
        "difficulty": "Hard",
        "tags": ["Multithreading"]
    },
    {
        "id": 13,
        "question": "Explain synchronized keyword.",
        "answer": "**synchronized** prevents thread interference.\n\n### Synchronized Method\n```java\npublic synchronized void increment() {\n    count++;\n}\n```\n\n### Synchronized Block\n```java\nsynchronized(this) {\n    count++;\n}\n```\n\n**How it works:**\n- Only ONE thread can execute at a time\n- Other threads wait (blocked)\n\n**Use when:** Accessing shared resources (bank account balance, etc.)",
        "difficulty": "Hard",
        "tags": ["Multithreading", "Concurrency"]
    },
    {
        "id": 14,
        "question": "String vs StringBuilder vs StringBuffer.",
        "answer": "### String (Immutable)\n- Cannot be modified\n- Create new object for each change\n- Thread-safe (immutable)\n\n### StringBuilder (Mutable, Not Thread-safe)\n- Can be modified\n- **Fastest** (no synchronization)\n- Use in single-threaded\n\n### StringBuffer (Mutable, Thread-safe)\n- Can be modified  \n- Synchronized methods\n- Use in multi-threaded\n\n**Performance:** StringBuilder > StringBuffer > String",
        "difficulty": "Medium",
        "tags": ["Strings"]
    },
    {
        "id": 15,
        "question": "What is Garbage Collection in Java?",
        "answer": "**Garbage Collection** = Automatic memory management.\n\n### How it works:\n1. JVM identifies unreferenced objects\n2. Frees memory occupied by them\n3. Prevents memory leaks\n\n### GC Methods:\n- `System.gc()` - suggests JVM to run GC (not guaranteed)\n- `finalize()` - called before object destruction (deprecated)\n\n### Types:\n- **Minor GC** - Young Generation\n- **Major GC** - Old Generation\n- **Full GC** - Entire Heap\n\n**Advantage:** Developer doesn't manually free memory (unlike C/C++)",
        "difficulty": "Medium",
        "tags": ["Memory Management"]
    }
]

# COMPREHENSIVE Spring Boot Questions (add to reach 12 total)
spring_new = [
    {
        "id": 107,
        "question": "What are different bean scopes in Spring?",
        "answer": "### Singleton (Default)\n- ONE instance per Spring container\n- Same object returned every time\n\n### Prototype  \n- NEW instance each time bean is requested\n\n### Request (Web)\n- New instance per HTTP request\n\n### Session (Web)\n- New instance per HTTP session\n\n### Application\n- One instance per ServletContext\n\n```java\n@Scope(\"prototype\")\n@Component\npublic class MyBean { }\n```",
        "difficulty": "Medium",
        "tags": ["Spring Core", "Beans"]
    },
    {
        "id": 108,
        "question": "Explain @Autowired, @Qualifier, @Primary.",
        "answer": "### @Autowired\nAuto dependency injection by type\n```java\n@Autowired\nprivate UserRepository repo;\n```\n\n### @Qualifier\nResolves ambiguity when multiple beans of same type exist\n```java\n@Autowired\n@Qualifier(\"mysqlRepo\")\nprivate UserRepository repo;\n```\n\n### @Primary\nMarks default bean when multiple candidates exist\n```java\n@Primary\n@Component\npublic class MySQLRepo implements UserRepository { }\n```",
        "difficulty": "Medium",
        "tags": ["DI", "Annotations"]
    },
    {
        "id": 109,
        "question": "JPA vs Hibernate difference?",
        "answer": "### JPA (Java Persistence API)\n- **Specification** / Interface\n- Standard for ORM\n- Vendor independent\n\n### Hibernate\n- **Implementation** of JPA\n- Most popular ORM framework\n- Has additional features beyond JPA\n\n**Analogy:** JPA = Interface, Hibernate = Implementation\n\nOther JPA implementations: EclipseLink, OpenJPA",
        "difficulty": "Easy",
        "tags": ["Database", "ORM"]
    },
    {
        "id": 110,
        "question": "What is Spring Boot Actuator?",
        "answer": "Actuator provides **production-ready** features for monitoring and managing.\n\n### Key Endpoints:\n- `/actuator/health` - Application health\n- `/actuator/metrics` - Application metrics\n- `/actuator/info` - Application info\n- `/actuator/env` - Environment properties\n- `/actuator/beans` - All Spring beans\n\n### Enable:\n```xml\n<dependency>\n    <groupId>org.springframework.boot</groupId>\n    <artifactId>spring-boot-starter-actuator</artifactId>\n</dependency>\n```\n\n**Use:** Monitoring in production, health checks for load balancers",
        "difficulty": "Medium",
        "tags": ["Monitoring", "DevOps"]
    },
    {
        "id": 111,
        "question": "How to handle exceptions in Spring Boot?",
        "answer": "### @ControllerAdvice\nGlobal exception handler\n```java\n@ControllerAdvice\npublic class GlobalExceptionHandler {\n    @ExceptionHandler(ResourceNotFoundException.class)\n    public ResponseEntity<?> handleNotFound(Exception ex) {\n        return new ResponseEntity<>(ex.getMessage(), HttpStatus.NOT_FOUND);\n    }\n}\n```\n\n### @ResponseStatus\n```java\n@ResponseStatus(HttpStatus.NOT_FOUND)\npublic class ResourceNotFoundException extends Exception { }\n```\n\n**Best Practice:** Centralized error handling with meaningful HTTP status codes",
        "difficulty": "Hard",
        "tags": ["Exception Handling", "REST"]
    },
    {
        "id": 112,
        "question": "What is application.properties vs application.yml?",
        "answer": "Both used for externalized configuration.\n\n### application.properties\n```properties\nserver.port=8080\nspring.datasource.url=jdbc:mysql://localhost/db\n```\n\n### application.yml (Preferred)\n```yaml\nserver:\n  port: 8080\nspring:\n  datasource:\n    url: jdbc:mysql://localhost/db\n```\n\n**Advantages of YAML:**\n- More readable (hierarchical)\n- Less repetitive\n- Supports lists\n\nBoth work the same, just syntax difference.",
        "difficulty": "Easy",
        "tags": ["Configuration"]
    }
]

# COMPREHENSIVE SQL/Database Questions  
sql_new = [
    {
        "id": 206,
        "question": "Primary Key vs Unique Key vs Foreign Key.",
        "answer": "### Primary Key\n- **Uniquely identifies** each row\n- **NOT NULL** automatically\n- Only **ONE** per table\n- Creates **clustered index**\n\n### Unique Key\n- Ensures uniqueness\n- Can have **NULL** values (one NULL allowed)\n- **Multiple** allowed per table\n\n### Foreign Key\n- References Primary Key of another table\n- Maintains **referential integrity**\n- Can have duplicate values\n\n**Example:**\n```sql\nCREATE TABLE Students (\n    id INT PRIMARY KEY,\n    email VARCHAR(100) UNIQUE,\n    class_id INT FOREIGN KEY REFERENCES Classes(id)\n);\n```",
        "difficulty": "Medium",
        "tags": ["Keys", "Constraints"]
    },
    {
        "id": 207,
        "question": "What is a View in SQL?",
        "answer": "**View** = Virtual table based on a query.\n\n### Create View\n```sql\nCREATE VIEW active_users AS\nSELECT id, name, email\nFROM users\nWHERE status = 'active';\n```\n\n### Use View\n```sql\nSELECT * FROM active_users;\n```\n\n### Advantages:\n- **Security** - hide sensitive columns\n- **Simplicity** - complex joins as simple table\n- **Consistency** - reusable logic\n\n**Materialized View:** Stores result physically (faster but needs refresh)",
        "difficulty": "Medium",
        "tags": ["Views"]
    },
    {
        "id": 208,
        "question": "Explain Stored Procedure vs Function.",
        "answer": "### Stored Procedure\n- Can **modify** data (INSERT, UPDATE, DELETE)\n- Returns via OUT parameters\n- Can't be used in SELECT\n```sql\nCALL update_salary(emp_id, new_salary);\n```\n\n### Function\n- **Read-only** (only SELECT)\n- Returns single value\n- Can be used in SELECT\n```sql\nSELECT calculate_age(birth_date) FROM users;\n```\n\n**Use Procedure:** Complex business logic, data modifications\n**Use Function:** Calculations, transformations in queries",
        "difficulty": "Hard",
        "tags": ["Stored Procedures"]
    },
    {
        "id": 209,
        "question": "What is a Transaction? COMMIT vs ROLLBACK.",
        "answer": "**Transaction** = Group of operations (all or nothing).\n\n### Commands:\n- `BEGIN TRANSACTION` - Start\n- `COMMIT` - Save changes permanently\n- `ROLLBACK` - Undo changes\n- `SAVEPOINT` - Set intermediate point\n\n### Example:\n```sql\nBEGIN TRANSACTION;\n    UPDATE accounts SET balance = balance - 100 WHERE id = 1;\n    UPDATE accounts SET balance = balance + 100 WHERE id = 2;\nCOMMIT; -- Both succeed\n-- If error: ROLLBACK; -- Both cancelled\n```\n\n**ACID Properties ensure transaction reliability.**",
        "difficulty": "Medium",
        "tags": ["Transactions"]
    },
    {
        "id": 210,
        "question": "NoSQL vs SQL databases.",
        "answer": "### SQL (Relational)\n- **Structured** data (tables, rows, columns)\n- **Fixed schema**\n- **ACID** compliant\n- Examples: MySQL, PostgreSQL\n- Use: Banking, E-commerce\n\n### NoSQL (Non-Relational)\n- **Unstructured** data (documents, key-value)\n- **Flexible schema**\n- **BASE** (Basically Available, Soft state, Eventually consistent)\n- Examples: MongoDB, Redis, Cassandra\n- Use: Social media, Big Data, Real-time apps\n\n**When to use NoSQL:**\n- Massive scale\n- Rapid development\n- Unstructured data",
        "difficulty": "Medium",
        "tags": ["Database Types"]
    }
]

# COMPREHENSIVE React Questions
react_new = [
    {
        "id": 305,
        "question": "Class Components vs Functional Components.",
        "answer": "### Class Components\n```jsx\nclass MyComponent extends React.Component {\n    constructor(props) {\n        super(props);\n        this.state = { count: 0 };\n    }\n    render() { return <div>{this.state.count}</div>; }\n}\n```\n\n### Functional Components (Modern)\n```jsx\nfunction MyComponent() {\n    const [count, setCount] = useState(0);\n    return <div>{count}</div>;\n}\n```\n\n**Advantages of Functional:**\n- Simpler syntax\n- Better performance\n- Hooks support\n- Less boilerplate\n\n**Modern React:** Use functional components with Hooks",
        "difficulty": "Easy",
        "tags": ["Components"]
    },
    {
        "id": 306,
        "question": "What is Context API and when to use it?",
        "answer": "Context API provides **global state** without prop drilling.\n\n### Create Context\n```jsx\nconst ThemeContext = React.createContext('light');\n```\n\n### Provider\n```jsx\n<ThemeContext.Provider value='dark'>\n    <App />\n</ThemeContext.Provider>\n```\n\n### Consumer (with useContext)\n```jsx\nconst theme = useContext(ThemeContext);\n```\n\n**Use when:**\n- Authentication state\n- Theme/Language settings\n- Avoid prop drilling 5+ levels\n\n**Don't use for:** Frequent updates (use Redux/Zustand instead)",
        "difficulty": "Medium",
        "tags": ["State Management"]
    },
    {
        "id": 307,
        "question": "Why are Keys important in React Lists?",
        "answer": "Keys help React identify which items changed, added, or removed.\n\n### Bad (using index)\n```jsx\n{items.map((item, index) => <div key={index}>{item}</div>)}\n```\n\n### Good (using unique ID)\n```jsx\n{items.map(item => <div key={item.id}>{item.name}</div>)}\n```\n\n**Why not index?**\n- Reordering breaks\n- Performance issues\n- State bugs\n\n**Best practice:** Use stable, unique IDs from data",
        "difficulty": "Easy",
        "tags": ["Lists", "Performance"]
    },
    {
        "id": 308,
        "question": "Controlled vs Uncontrolled Components.",
        "answer": "### Controlled Component\n- React **controls** form data via state\n- Value from state, onChange updates state\n```jsx\nconst [name, setName] = useState('');\n<input value={name} onChange={e => setName(e.target.value)} />\n```\n\n### Uncontrolled Component\n- DOM **controls** form data\n- Use `ref` to access value\n```jsx\nconst inputRef = useRef();\n<input ref={inputRef} />\nconst value = inputRef.current.value;\n```\n\n**Prefer Controlled** for validation, dynamic behavior",
        "difficulty": "Medium",
        "tags": ["Forms"]
    }
]

# COMPREHENSIVE DSA Questions
dsa_new = [
    {
        "id": 405,
        "question": "How to reverse a Linked List?",
        "answer": "### Iterative Approach (Best)\n```java\nNode reverse(Node head) {\n    Node prev = null;\n    Node current = head;\n    while (current != null) {\n        Node next = current.next;\n        current.next = prev;\n        prev = current;\n        current = next;\n    }\n    return prev;\n}\n```\n\n**Time:** O(n), **Space:** O(1)\n\n### Recursive Approach\n```java\nNode reverse(Node head) {\n    if (head == null || head.next == null) return head;\n    Node rest = reverse(head.next);\n    head.next.next = head;\n    head.next = null;\n    return rest;\n}\n```\n\n**Time:** O(n), **Space:** O(n) due to recursion stack",
        "difficulty": "Medium",
        "tags": ["Linked List"]
    },
    {
        "id": 406,
        "question": "Binary Search Tree (BST) operations.",
        "answer": "### Search in BST\n```java\nboolean search(Node root, int key) {\n    if (root == null) return false;\n    if (root.data == key) return true;\n    if (key < root.data) return search(root.left, key);\n    return search(root.right, key);\n}\n```\n\n### Insert in BST\n```java\nNode insert(Node root, int key) {\n    if (root == null) return new Node(key);\n    if (key < root.data) root.left = insert(root.left, key);\n    else root.right = insert(root.right, key);\n    return root;\n}\n```\n\n**Time Complexity:**\n- Average: O(log n)\n- Worst (skewed tree): O(n)",
        "difficulty": "Hard",
        "tags": ["Trees", "BST"]
    },
    {
        "id": 407,
        "question": "Stack vs Queue differences and uses.",
        "answer": "### Stack (LIFO - Last In First Out)\n- Operations: push(), pop(), peek()\n- **Uses:** \n  - Function calls (call stack)\n  - Undo/Redo\n  - Parenthesis matching\n  - Backtracking\n\n### Queue (FIFO - First In First Out)\n- Operations: enqueue(), dequeue(), front()\n- **Uses:**\n  - BFS traversal\n  - Printer queue\n  - Task scheduling\n  - Message queues\n\n**Implementation:**\n- Stack: Array or Linked List\n- Queue: Circular array or Linked List",
        "difficulty": "Easy",
        "tags": ["Data Structures"]
    },
    {
        "id": 408,
        "question": "Explain Sliding Window technique.",
        "answer": "Sliding Window optimizes problems involving subarrays/substrings.\n\n### Example: Max sum of k consecutive elements\n```java\nint maxSum(int[] arr, int k) {\n    int windowSum = 0, maxSum = 0;\n    // First window\n    for (int i = 0; i < k; i++) windowSum += arr[i];\n    maxSum = windowSum;\n    \n    // Slide window\n    for (int i = k; i < arr.length; i++) {\n        windowSum = windowSum - arr[i-k] + arr[i];\n        maxSum = Math.max(maxSum, windowSum);\n    }\n    return maxSum;\n}\n```\n\n**Time:** O(n) instead of O(n*k) with nested loops\n\n**Use cases:** Longest substring, maximum sum subarray",
        "difficulty": "Medium",
        "tags": ["Techniques", "Optimization"]
    }
]

# COMPREHENSIVE HR Questions
hr_new = [
    {
        "id": 503,
        "question": "What are your strengths and weaknesses?",
        "answer": "### Strengths (Pick 2-3 genuine ones)\n**Template:** Strength + Example\n\n*\"My key strength is **problem-solving**. In my recent project, I optimized a slow API by implementing caching, reducing response time by 40%. I also have strong **collaboration skills** - I mentored 3 junior developers in my internship.\"*\n\n### Weaknesses (Pick 1, show improvement)\n**Template:** Weakness + What you're doing to improve\n\n*\"I sometimes focus too much on perfection which can slow me down. To improve this, I've started using time-boxing - allocating specific time for tasks and then moving forward, which has improved my efficiency.\"*\n\n**Don't say:** \"I'm a perfectionist\" or \"I work too hard\"",
        "difficulty": "Medium",
        "tags": ["Self-awareness"]
    },
    {
        "id": 504,
        "question": "Why do you want to work for our company?",
        "answer": "**Research the company first!**\n\n### Template:\n1. **Specific interest** in company's product/tech\n2. **Alignment** with your career goals\n3. **Values** match\n\n**Example:**\n*\"I'm particularly excited about [Company]'s work in [specific technology/product]. Your use of microservices architecture aligns perfectly with my experience in Spring Boot. I've been following your tech blog and impressed by your focus on innovation. The collaborative culture you promote matches my working style, and I believe I can contribute significantly to your [specific team/project].\"*\n\n**Don't say:** \"For money\" or \"It's close to my house\"",
        "difficulty": "Easy",
        "tags": ["Motivation"]
    },
    {
        "id": 505,
        "question": "Where do you see yourself in 5 years?",
        "answer": "**Show growth mindset + alignment with company**\n\n### Template:\n\"In 5 years, I see myself as [realistic progression]...\"\n\n**Example:**\n*\"In 5 years, I see myself as a Senior Full-Stack Developer, having mastered both frontend and backend technologies. I'd like to lead a small team, mentor junior developers, and contribute to architectural decisions. I'm also interested in cloud technologies, so I hope to gain AWS certifications. Most importantly, I want to be someone the organization relies on for solving complex technical challenges.\"*\n\n**Avoid:**\n- \"Your job\" (threatening)\n- \"Don't know\" (no ambition)\n- Completely unrelated field",
        "difficulty": "Medium",
        "tags": ["Career Goals"]
    },
    {
        "id": 506,
        "question": "Describe a time you faced conflict at work/team.",
        "answer": "**Use STAR method**\n\n**Example:**\n\n**Situation:** \"In my college project, our team disagreed on technology stack - React vs Angular.\"\n\n**Task:** \"I needed to resolve this to move forward without affecting team morale.\"\n\n**Action:** \"I organized a meeting where each person presented pros/cons with research. I created a comparison matrix based on project requirements, team skills, and deadlines. We voted democratically.\"\n\n**Result:** \"We chose React. The decision-making process improved team bonding. We completed the project successfully and everyone learned React together.\"\n\n**Key:** Show maturity, communication, and problem-solving",
        "difficulty": "Hard",
        "tags": ["Behavioral", "Conflict Resolution"]
    },
    {
        "id": 507,
        "question": "Biggest achievement in your career/academics?",
        "answer": "**Pick something impressive + relevant**\n\n### Template:\nChallenge + Your Action + Result\n\n**Example:**\n*\"My biggest achievement was optimizing a microservices project during my internship at [Company]. The order service was timing under high load.*\n\n*I analyzed the bottleneck, found N+1 query issues in database calls, and implemented batch processing and Redis caching. This improved response time by 60% and handled 1000+ concurrent requests.*\n\n*The solution was presented to senior architects and adopted across other services. This taught me the importance of performance optimization and gave me confidence in handling production issues.\"*\n\n**Quantify results** whenever possible!",
        "difficulty": "Medium",
        "tags": ["Achievements"]
    },
    {
        "id": 508,
        "question": "How do you handle failure or criticism?",
        "answer": "**Show growth mindset**\n\n### Template:\nAcknowledge + Learn + Improve\n\n**Example:**\n*\"I view failure as a learning opportunity. In my first internship, I pushed code that broke the staging environment - I forgot to test edge cases.*\n\n*Instead of being defensive, I:*\n*1. Immediately owned the mistake and fixed it*\n*2. Conducted a root cause analysis*\n*3. Implemented a personal checklist for code review*\n*4. Now I use test-driven development (TDD)*\n\n*This failure made me a more thorough developer. I always ask for feedback from seniors and use criticism to identify blind spots.\"*\n\n**Show:** Accountability + Action + Growth",
        "difficulty": "Medium",
        "tags": ["Self-improvement"]
    }
]

# Add ALL questions to respective topics
for topic in data['topics']:
    if topic['id'] == 'java-core':
        # Filter out duplicates by ID
        existing_ids = {q['id'] for q in topic['questions']}
        topic['questions'].extend([q for q in java_new if q['id'] not in existing_ids])
    elif topic['id'] == 'spring-boot':
        existing_ids = {q['id'] for q in topic['questions']}
        topic['questions'].extend([q for q in spring_new if q['id'] not in existing_ids])
    elif topic['id'] == 'database':
        existing_ids = {q['id'] for q in topic['questions']}
        topic['questions'].extend([q for q in sql_new if q['id'] not in existing_ids])
    elif topic['id'] == 'react':
        existing_ids = {q['id'] for q in topic['questions']}
        topic['questions'].extend([q for q in react_new if q['id'] not in existing_ids])
    elif topic['id'] == 'dsa':
        existing_ids = {q['id'] for q in topic['questions']}
        topic['questions'].extend([q for q in dsa_new if q['id'] not in existing_ids])
    elif topic['id'] == 'hr':
        existing_ids = {q['id'] for q in topic['questions']}
        topic['questions'].extend([q for q in hr_new if q['id'] not in existing_ids])

# Update total count
all_q = sum(len(t['questions']) for t in data['topics'])
data['stats']['totalQuestions'] = all_q

# Save
with open('src/data/interviewData.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

# Print summary
print(f"\n✅ ALL TOPICS UPDATED!")
print(f"=" * 50)
for topic in data['topics']:
    print(f"{topic['title']}: {len(topic['questions'])} questions")
print(f"=" * 50)
print(f"📚 TOTAL: {all_q} questions")
print(f"\n🎉 No topic missed - ALL covered comprehensively!")
