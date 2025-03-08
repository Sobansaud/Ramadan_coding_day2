from fastapi import FastAPI
import random 

my_app = FastAPI()

# we will built two get endpoints
# side-hustles
# skills

side_hustles= [
    "Web Development",
    "Graphic Design",
    "Content Writing",
    "Digital Marketing",
    "Photography",
    "Video Production",
    "Voice Over Work",
    "Tutoring",
    "Freelance Writing",
    "Social Media Management",
]

skills= [
    "Python",
    "JavaScript",
    "Html/Css",
    "C++",
    "Java",
    "C#",
    "Ruby",
    "Swift",
    "PHP",
    "Go",

]

@my_app.get("/side_hustles")
def get_side_hustles(my_key: str):
    '''Return a random side hustle'''
    if my_key != "soban":
        return {"error" : "Invalid Api Key"}
    return{'side-hustle': random.choice(side_hustles)}

@my_app.get("/skills")
def get_skills(my_key: str):
    '''Return a random skill'''
    if my_key != "soban":
        return {"error" : "Invalid Api Key"}
    return {"skill": random.choice(skills)}

# THEN RUN COMMAND ON TERMINAL (fastapi dev main.py)


