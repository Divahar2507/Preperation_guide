import json

print("Adding personalized 'Tell me about yourself' answer...")

# Load data
with open('src/data/interviewData.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Find HR topic
for topic in data['topics']:
    if topic['id'] == 'hr':
        # Check if question already exists
        existing_ids = {q['id'] for q in topic['questions']}
        
        # Add personalized answer
        new_question = {
            "id": 509,
            "question": "Tell me about yourself (Sample Answer for Java Full-Stack Developer)",
            "answer": """This is THE MOST IMPORTANT question. Here's a structured approach with a sample answer:

### **Structure (60-90 seconds):**
1. **Present** (Current role/education)
2. **Past** (Relevant experience)
3. **Future** (Why this company/role)

---

### **Sample Answer for Java Full-Stack Developer:**

*"Good morning/afternoon. I'm Divahar P, currently in my final year of B.Tech in Information Technology at Anna University with a CGPA of 7.8.*

*I'm working as a Java Full-Stack Developer Intern at KodNest Technologies in Bengaluru, where I've been developing RESTful APIs using Spring Boot and building responsive frontends with React.js. One of my key achievements was optimizing backend processing by 35% through implementing a microservices architecture, and I also developed customer-facing dashboards that increased user engagement by 40%.*

*I'm particularly passionate about full-stack development and microservices. I've built an e-commerce platform using Spring Boot, MongoDB, and React that handles over 1,000 requests per minute. I also set up CI/CD pipelines with GitHub Actions, which accelerated our deployment process by 20%.*

*What excites me about [Company Name] is [specific reason - their tech stack, products, culture, or projects]. I'm looking to leverage my experience in Java, Spring Boot, and React to contribute to building scalable, user-centric applications while continuing to grow as a developer.*

*I'm a quick learner, a team player, and I'm genuinely excited about this opportunity."*

---

### **Key Elements to Include:**

1. **Education**: Mention your degree, university, CGPA (if good)
2. **Current Role**: Internship/job with key responsibilities
3. **Technical Skills**: Java, Spring Boot, React, databases
4. **Achievements**: Use numbers (35% improvement, 40% increase, etc.)
5. **Projects**: Mention 1-2 impressive projects with metrics
6. **Why This Company**: Show you've researched them
7. **Personality**: Quick learner, team player, passionate

---

### **Customization Template:**

*"I'm [Your Name], [Current Status - final year student/working professional] at [Institution/Company].*

*Currently, I'm [Current Role] where I [Key Responsibility 1] and [Key Responsibility 2]. I achieved [Specific Achievement with Numbers].*

*I'm skilled in [Tech Stack: Java, Spring Boot, React, SQL, etc.]. I built [Project Name] using [Technologies] that [Impact/Metric].*

*What attracts me to [Company] is [Specific Reason]. I'm excited to contribute my [Skills] to [Company's Work/Product]."*

---

### **Common Mistakes to Avoid:**

❌ Starting with "My name is..." (they know from resume)  
❌ Talking about childhood or personal life  
❌ Being too long (>2 minutes)  
❌ Just repeating resume  
❌ Not mentioning why you want THIS job  
❌ Being too generic  

---

### **Tips:**

✅ **Practice out loud** 10+ times  
✅ **Time yourself** (aim for 60-90 seconds)  
✅ **Use STAR** for achievements  
✅ **Smile and maintain eye contact**  
✅ **Show enthusiasm**  
✅ **End with why you want THIS role**  

---

### **For Freshers (No Experience):**

*"I'm [Name], final year B.Tech student in [Branch] at [University] with [CGPA].*

*During my academics, I've focused on full-stack development. I built [Project 1] using Java and Spring Boot that [Achievement]. I also developed [Project 2] with React that [Impact].*

*I've completed certifications in [Courses] and practiced [Number] DSA problems on LeetCode. I'm particularly strong in [Skills].*

*I'm drawn to [Company] because [Reason]. I'm eager to apply my knowledge and learn from experienced developers while contributing to [Company's Work]."*

---

### **Practice Questions:**

After answering, be ready for:
- "Walk me through your resume"
- "Tell me about your project in detail"
- "What's your biggest achievement?"
- "Why should we hire you?"

**Remember:** This is your FIRST IMPRESSION. Make it count! 🎯""",
            "difficulty": "Easy",
            "tags": ["Introduction", "Most Important"]
        }
        
        if 509 not in existing_ids:
            topic['questions'].append(new_question)
            print("✅ Added personalized 'Tell me about yourself' answer!")
        else:
            print("ℹ️ Question already exists, updating...")
            for q in topic['questions']:
                if q['id'] == 509:
                    q['answer'] = new_question['answer']
        
        break

# Update total
total = sum(len(t['questions']) for t in data['topics'])
data['stats']['totalQuestions'] = total

# Save
with open('src/data/interviewData.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print(f"\n✅ Updated! Total questions: {total}")
print("\n📝 Added comprehensive 'Tell me about yourself' with:")
print("  - Sample answer for Java Full-Stack Developer")
print("  - Personalized template")
print("  - Structure guide (60-90 seconds)")
print("  - Common mistakes to avoid")
print("  - Tips for delivery")
print("  - Fresher version")
print("\n🎯 This is now ready for practice!")
