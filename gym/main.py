from gym.auth import login
from gym.services import add_member, view_members, deactivate_member, delete_member


def admin_menu():
    while True:
        print("\n1. Add Member")
        print("2. View Members")
        print("3. Deactivate Member")
        print("4. Delete Member")
        print("5. Logout")

        choice = input("Choose: ")

        if choice == "1":
            add_member()
        elif choice == "2":
            view_members()
        elif choice == "3":
            deactivate_member()
        elif choice == "4":
            delete_member()
        elif choice == "5":
            break


def staff_menu():
    while True:
        print("\n1. View Members")
        print("2. Logout")

        choice = input("Choose: ")

        if choice == "1":
            view_members()
        elif choice == "2":
            break


def main():
    user = login()

    if user is None:
        return

    if user.role == "admin":
        admin_menu()
    else:
        staff_menu()


if __name__ == "__main__":
    main()