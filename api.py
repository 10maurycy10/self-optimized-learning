import requests
import tqdm
import sys
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

    def get_project_dict(self):
        db = {}
        for proj in self.d["projects"]:
            db[proj["id"]] = proj
        return db

class API:
    def __init__(self, token):
        self.auth = token

    def get_project_json(self, projectid):
        r = requests.get(f"https://www.summitlearning.org/my/projects/{projectid}/overview.json", headers={"cookie": self.auth.rstrip()})
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

if len(sys.argv) == 1:
    print("Please pass the year for which information sould be fetched as an argument")
    exit(1)

year = sys.argv[1]

api = API(open("cookie").read())

data = {}
year = api.get_year(year)
projects = year.get_project_dict()
for course in year.get_courses():
    c_name = course["name"]
    data[c_name] = {}
    for projectid in course["projectIds"]:
        data[c_name][projectid] = {}
        data[c_name][projectid]["name"] = projects[projectid]["name"]
        data[c_name][projectid]["skills"] = projects[projectid]["rubricDimensionIds"]

open("data.json",'w').write(json.dumps(data))

