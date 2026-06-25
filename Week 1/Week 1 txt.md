# Week 1 — Python Basics + Introduction to Machine Learning (Theory)

## 🎯 Week Objectives

- Set up Python environment (VS Code + pip)
- Get comfortable with Python syntax
- Understand variables, data types, lists, dictionaries
- Write basic control flow (loops, conditions)
- Define and use functions
- Complete a mini-project to apply everything
- Read introductory ML theory (no code yet)

---

## 📚 Topics Covered

| Topic | File |
|-------|------|
| Variables and data types | `variables_datatypes.py` |
| Lists and dictionaries | `lists_dictionaries.py` |
| Loops and conditional logic | `loops_conditions.py` |
| Functions and scope | `functions.py` |
| Mini project | `mini_project_student_marks.py` |
| ML theory reading notes | `ml_theory_notes.md` |

---

## 📝 Summary of Learning

This was my first proper week with Python (I had done a little bit before but nothing structured). The biggest things that clicked:

- Python doesn't need semicolons or type declarations — it's a lot more readable.
- Lists and dictionaries are incredibly useful. I kept wanting to use them for everything.
- Functions took a little while to understand (especially `return` vs `print`), but once it clicked it made sense.
- The ML theory reading was eye-opening. I didn't realize how many everyday things (spam filters, recommendation systems) are ML.

I made some mistakes along the way — for example I forgot that `range(n)` goes from 0 to n-1, not 1 to n. That caused a bug in my loop which I've left in the file as a comment to remind myself.

---

## 📂 Files in This Folder

```
Week1_Python_Basics/
├── README.md                       # This file
├── variables_datatypes.py          # Basic Python variables and type operations
├── lists_dictionaries.py           # Working with lists and dicts
├── loops_conditions.py             # for/while loops, if/elif/else
├── functions.py                    # Defining and calling functions
├── mini_project_student_marks.py   # Mini project: grade calculator
└── ml_theory_notes.md              # Notes from ML introductory reading
```

---

## 💡 Key Takeaways

1. Python is beginner-friendly but there's a lot of depth below the surface.
2. `len()`, `append()`, `pop()`, `keys()`, `values()` — these four/five methods cover 90% of what I needed.
3. Functions make code reusable — I could have used them in Week 0 if I'd known!
4. ML is all about finding patterns in data. The computer doesn't "understand" — it optimizes.
5. Supervised vs unsupervised learning: the key difference is whether labels exist.

---

## 🔧 Future Improvements

- Practice more string manipulation (I haven't done much with `.split()`, `.join()` etc.)
- Try list comprehensions — I've seen them but haven't used them confidently
- Explore `lambda` functions
- Do more practice problems before moving to Week 2
