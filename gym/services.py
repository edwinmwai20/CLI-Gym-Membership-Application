# gym/services.py

from .storage import load_members, save_members


def add_member():
    members = load_members()

    name = input("Member name: ")
    plan = input("Plan: ")

    new_id = len(members) + 1

    new_member = {
        "id": new_id,
        "name": name,
        "plan": plan,
        "status": "Active"
    }

    members.append(new_member)
    save_members(members)

    print("Member added.")


def view_members():
    members = load_members()

    for m in members:
        print(m)


def deactivate_member():
    members = load_members()
    member_id = int(input("Member ID: "))

    for m in members:
        if m["id"] == member_id:
            m["status"] = "Inactive"

    save_members(members)
    print("Member deactivated.")



def update_member():
    members = load_members()
    member_name = input("Enter member name: ")
    for m in members:
        if m['name'] == member_name:
            print(f"\nCurrent details: {m}")
            new_name = input("New name (press Enter to keep current): ")
            new_plan = input("New plan (press Enter to keep current): ")

            if new_name:
                m['name'] = new_name
            if new_plan:
                m['plan'] = new_plan

            save_members(members)

            print("Member updated successfully.")
            return



def delete_member():
    members = load_members()
    member_name = input("Enter member name: ")
    for m in members:
        if m["name"] == member_name:
            members.remove(m)
            save_members(members)
            print(f"{member_name} has been deleted")

            return