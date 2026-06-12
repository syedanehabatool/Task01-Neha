def main():
    database_table = []
    task_counter = 1

    print("=============================================")
    print("      DECODELABS TO-DO LIST ENGINE v1.0      ")
    print("=============================================")

    while True:
        print("\n--- MENU ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit Engine")
        
        choice = input("Select an option (1-3): ").strip()

        if choice == '1':
            task_name = input("Enter the task description: ").strip()
            
            if not task_name:
                print("❌ Error: Task description cannot be empty.")
                continue

            task_row = {
                'id': task_counter,
                'task_name': task_name
            }

            database_table.append(task_row)
            print(f"✔️ Task successfully added! (Assigned ID: {task_counter})")
            task_counter += 1

        elif choice == '2':
            print("\n=============================================")
            print("               CURRENT TASKS                 ")
            print("=============================================")
            
            if not database_table:
                print("   [ No tasks found in volatile memory ]     ")
            else:
                print(f"{'ID':<6} | {'TASK DESCRIPTION':<30}")
                print("-" * 45)
                for row in database_table:
                    print(f"{row['id']:<6} | {row['task_name']:<30}")
            
            print("=============================================")

        elif choice == '3':
            print("\nShutting down backend engine...")
            print("⚠️ Warning: Memory is volatile. Data will be cleared upon exit.")
            print("Goodbye!")
            break

        else:
            print("❌ Invalid selection. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
