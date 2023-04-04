from tareaschetto import *
def print_menu():
    print("\nMenu:")
    print("1. Create homework")
    print("2. Assign homework")
    print("3. Show homeworks")
    print("4. Exit")

if __name__ == '__main__':
    repository = InMemoryHomeworkRepository()
    service = HomeworkService(repository)

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter the name of the homework: ")
            deadline_days = int(input("Enter the number of days until the deadline: "))
            service.create_homework(name, deadline_days)
            print("Homework created successfully!")
        elif choice == "2":
            homeworks = service.get_homeworks()
            if not homeworks:
                print("There are no homeworks to assign.")
            else:
                print("Select a homework to assign:")
                for i, homework in enumerate(homeworks):
                    print(f"{i + 1}. {homework.get_name()} (due {homework.get_deadline().strftime('%Y-%m-%d')})")
                index = int(input("Enter the number of the homework: ")) - 1
                homework = homeworks[index]
                homework.set_is_complete(False)
                print(f"{homework.get_name()} has been assigned.")
        elif choice == "3":
            homeworks = service.get_homeworks()
            if not homeworks:
                print("There are no homeworks assigned.")
            else:
                print("Homeworks assigned:")
                for i, homework in enumerate(homeworks):
                    status = "complete" if homework.get_is_complete() else "incomplete"
                    print(f"{i + 1}. {homework.get_name()} (due {homework.get_deadline().strftime('%Y-%m-%d')}, {status})")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
