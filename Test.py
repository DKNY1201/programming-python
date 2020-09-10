# def like(n):
#     while n >= 0:
#         s = str(n)
#         isSastify = True
#
#         for i in range(len(s) - 1):
#             if s[i] >= s[i + 1]:
#                 isSastify = False
#                 break
#
#         if isSastify:
#             return n
#
#         n -= 1
#
#     return 0
#
#
# print(like(500))


def get_team_lead_name(names):
    team_lead_names = []
    max_len = float("-Inf")

    for name in names:
        unique_letters = set()

        for letter in name:
            if letter != " ":
                unique_letters.add(letter.lower())

        if len(unique_letters) > max_len:
            max_len = len(unique_letters)
            team_lead_names = [name]
        elif len(unique_letters) == max_len:
            team_lead_names.append(name)

    team_lead_names.sort()

    return team_lead_names[0]

names = ["kylan charles", "raymond strickland", "julissa shepard", "andrea meza", "destiney alvarado"]
names = ["kylan charles", "raymond strickland1", "julissa shepard", "andrea meza", "destiney alvarado", "raymond strickland2"]
print(get_team_lead_name(names))