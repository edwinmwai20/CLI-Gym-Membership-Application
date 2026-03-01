from gym.storage import load_members, save_members


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