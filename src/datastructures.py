
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        self._members.append(member)
        print("ARRIVED!",member)
        pass

    def delete_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
            
        # pass

    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member
            else: print("ERROR, CANNOT RETRIEVE MEMBER")
        # fill this method and update the return
        # members_list = self._members
        # print(type(member_id, "memberID type!!!!"))
        # for member_object in members_list:
        #     member_id = member_object["id"]
        #     print(type(member_id, "memberID type!!!!"))
        #     if urlID == member_id:
        #         return member_object
        #     pass
    

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members

# find additional projects to build i.e youtube projects
# 4geeks projects section with project ideas to practice with 