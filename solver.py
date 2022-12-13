import json

def solve_course(course):
    """
    A simple herustic solver, ranks projects by cogskills that were not already covered.
    This does not garanty perfect solutions, but is fast and simple

    The grade is a number from 0 (0%) to 1 (100%).

    returns [(progect, max_grade)]
    """
    covered = set([])
    solution = []
    grade = 0
    # Count the total amount of skills
    all_skills = []

    for project in course.values():
        all_skills.extend(project["skills"])

    all_skills = set(all_skills)
    skill_count = len(all_skills)
    # Ranks projcts by how many skills they have that are not covered by the current solution
    def get_rank(project):
        rank = 0
        for skill in project:
            if skill in covered:
                pass
            else:
                rank = rank + 1
        return rank
    # Repetedly select the higest ranked project, updating the covered set.
    while len(solution) < len(course) and len(covered) < skill_count:
        ranks = [get_rank(course[project]["skills"]) for project in course.keys()]
        bestproject = list(course.keys())[ranks.index(max(ranks))]

        for skill in course[bestproject]["skills"]:
            covered.add(skill)

        grade = len(covered) / skill_count
        solution.append((bestproject, grade))
    # Pass out the solution
    return solution


data = json.loads(open("data.json").read())
for course in data.keys():
    print(f"# {course} #")
    solution = solve_course(data[course])
    for (projectid, grade) in solution:
        gradetotal = int((grade * 0.7 + 0.3)*100)
        grade = int(grade*100)
        name = data[course][projectid]["name"]
        print(f"\t{grade}%\t{gradetotal}%\thttps://www.summitlearning.org/my/projects/{projectid}/\t{name}")
