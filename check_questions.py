import json

print("🔍 Checking current questions and identifying gaps...")
print("=" * 70)

# Load current data
with open('src/data/interviewData.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Print current state
print("\n📊 CURRENT QUESTION COUNT:")
print("-" * 70)
for topic in data['topics']:
    print(f"{topic['title']}: {len(topic['questions'])} questions")
    # Show question titles
    for i, q in enumerate(topic['questions'][:5], 1):
        print(f"  {i}. {q['question'][:60]}...")
    if len(topic['questions']) > 5:
        print(f"  ... and {len(topic['questions']) - 5} more")
    print()

total = sum(len(t['questions']) for t in data['topics'])
print(f"\n📚 TOTAL: {total} questions")
print("=" * 70)

# Based on your comprehensive list, here are the gaps:
print("\n🎯 MISSING IMPORTANT QUESTIONS TO ADD:")
print("=" * 70)

missing = {
    "Core Java": [
        "What is the difference between Comparable and Comparator?",
        "Explain access modifiers (public, private, protected, default)",
        "What is autoboxing and unboxing?",
        "How to create a Singleton class?",
        "What is the difference between throw and throws?",
        "Explain BufferedReader vs FileReader",
        "What is NIO? Difference from IO?",
        "Steps to connect Java with MySQL using JDBC",
        "What is Statement vs PreparedStatement vs CallableStatement?"
    ],
    "Spring Boot": [
        "What is @Component vs @Service vs @Repository?",
        "Explain @RequestMapping vs @GetMapping/@PostMapping",
        "What is CrudRepository vs JpaRepository?",
        "Explain cascade types in JPA",
        "What is OneToMany and ManyToOne mapping?",
        "How to implement JWT authentication?",
        "What is Feign Client in microservices?",
        "Explain circuit breaker pattern"
    ],
    "Database/SQL": [
        "What is DDL, DML, DQL, TCL?",
        "Explain all isolation levels",
        "What is optimistic vs pessimistic locking?",
        "Window functions (ROW_NUMBER, RANK, LEAD/LAG)",
        "What are CTEs (Common Table Expressions)?",
        "How to prevent SQL injection?"
    ],
    "React": [
        "What is JSX and why use Babel?",
        "Explain component lifecycle methods",
        "What is code-splitting and lazy loading?",
        "How to implement React.memo?",
        "What is the difference between useMemo and useCallback?"
    ],
    "DSA": [
        "How to find missing number in array?",
        "Implement binary search",
        "Find majority element in array",
        "Detect and remove cycle in linked list",
        "Implement queue using stacks",
        "Tree traversal (inorder, preorder, postorder)",
        "Lowest common ancestor in tree",
        "Dijkstra's shortest path algorithm"
    ]
}

for module, questions in missing.items():
    print(f"\n{module} ({len(questions)} missing):")
    for i, q in enumerate(questions, 1):
        print(f"  {i}. {q}")

print("\n" + "=" * 70)
print(f"📈 RECOMMENDATION: Add ~{sum(len(q) for q in missing.values())} more questions")
print("=" * 70)
