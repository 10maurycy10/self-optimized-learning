import requests
import json

class Project:
    def __init__(self, d):
        self.d = d
    
    def get_tasks(self):
        return self.d["projectTasks"]

    def get_skills(self):
        """
        An iterator over the names of cog skills "task dimentions" 
        """
        for task in self.d["projectTasks"]:
            for skill in task["dimensions"]:
                yield skill["name"]

class Year:
    def __init__(self, d):
        self.d = d

    def get_courses(self):
        return self.d["courses"]

class API:
    def __init__(self, token):
        self.auth = token

    def get_project_json(self, projectid):
        r = requests.get(f"https://www.summitlearning.org/my/projects/{projectid}/overview.json", headers={"cookie": self.auth})
        r.raise_for_status()
        return json.loads(r.content)

    def get_year_json(self, year):
        r = requests.get(f"https://www.summitlearning.org/my/year/{year}.json", headers={"cookie": self.auth})
        r.raise_for_status()
        return json.loads(r.content)
    
    def get_year(self, year):
        d = self.get_year_json(year)
        return Year(d)

    def get_project(self, projectid):
        d = self.get_project_json(projectid)
        return Project(d)

api = API(open("cookie").read())

data = {}
import tqdm
for course in api.get_year(2023).get_courses():
    c_name = course["name"]
    data[c_name] = {}
    for projectid in tqdm.tqdm(course["projectIds"]):
        data[c_name][projectid] = []
        for skill in api.get_project(projectid).get_skills():
            data[c_name][projectid].append(skill)

open("data.json",'w').write(json.dumps(data))

