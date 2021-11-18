class Team(object):
    def __init__(self, name, count, grade):
        self.name = name
        self.count = count
        self.grade = grade

    def __str__(self):
        return ("name: {}; count: {}; grade: {}".format(self.name, self.count, self.grade))

    def __lt__(self, other):
        if self.count == other.count:
            return self.grade > other.grade
        else:
            return self.count > other.count

testNum = int(input())
for i in range(testNum):
    teamNum, teamName = input().split(" ")
    teamNum = int(teamNum)

    teams = []
    for j in range(teamNum):
        name, count, grade = input().split(" ")
        aTeam = Team(name, int(count), int(grade))
        teams.append(aTeam)

    teams = sorted(teams)
    for j in range(len(teams)):
        if teams[j].name == teamName:
            if j + 1 <= round(len(teams) * 0.6):
                print('YES')
            else:
                print('NO')
            break    