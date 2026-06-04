print("Hello and welcome to North Sussex Judo")

# Training plan prices (weekly fees)
TRAINING_FEES = {
    "B": ("Beginner", 25.00),
    "I": ("Intermediate", 30.00),
    "E": ("Elite", 35.00)
}

# Private tuition and competition fees
PRIVATE_TUITION_FEE = 9.50  # per hour
COMPETITION_FEE = 22.00  # per competition

# Weight categories
WEIGHT_CATEGORIES = {
    "H": "Heavyweight",
    "LH": "Light-Heavyweight",
    "M": "Middleweight",
    "LM": "Light-Middleweight",
    "L": "Lightweight",
    "F": "Flyweight"
}

# Maximum limits
MAX_PRIVATE_COACHING_HOURS = 5  # per week
WEEKS_IN_MONTH = 4

# Storage for records
records = []

def get_valid_input(prompt, valid_options=None, cast_func=str):
    """Get valid user input with error handling."""
    while True:
        try:
            user_input = cast_func(input(prompt).strip().upper())
            if valid_options and user_input not in valid_options:
                print("Invalid choice. Please select from:", ", ".join(valid_options))
                continue
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid value.")

def calculate_monthly_cost(training_plan, private_hours, num_competitions):
    """Calculate the total cost for the month."""
    training_cost = TRAINING_FEES[training_plan][1] * WEEKS_IN_MONTH
    private_tuition_cost = private_hours * PRIVATE_TUITION_FEE * WEEKS_IN_MONTH
    competition_cost = num_competitions * COMPETITION_FEE
    total_cost = training_cost + private_tuition_cost + competition_cost
    return training_cost, private_tuition_cost, competition_cost, total_cost

def add_record():
    """Add a new athlete's record."""
    print("\nAdding a new record:")
    athlete_name = input("Enter athlete's name: ")
    
    # Select training plan
    print("\nTraining Plans:")
    for key, (plan, price) in TRAINING_FEES.items():
        print(f"{key}: {plan} (£{price:.2f} per week)")
    training_plan = get_valid_input("Select a training plan (B/I/E): ", TRAINING_FEES.keys())
    
    # Enter current weight
    current_weight = get_valid_input("Enter athlete's current weight (kg): ", cast_func=float)
    
    # Show available weight categories
    print("\nAvailable competition weight categories:")
    for key, category in WEIGHT_CATEGORIES.items():
        print(f"{key}: {category}")
    competition_category = get_valid_input("Enter competition weight category (H/LH/M/LM/L/F): ", WEIGHT_CATEGORIES.keys())
    
    # Check if eligible for competitions
    num_competitions = 0
    if training_plan in ["I", "E"]:
        num_competitions = get_valid_input("Enter number of competitions this month: ", cast_func=int)
    else:
        print("Beginner athletes cannot enter competitions.")
    
    # Enter private coaching hours
    private_hours = get_valid_input(f"Enter private coaching hours per week (Max {MAX_PRIVATE_COACHING_HOURS}): ", cast_func=int)
    private_hours = min(private_hours, MAX_PRIVATE_COACHING_HOURS)  # Cap at max allowed
    
    # Calculate costs
    training_cost, private_tuition_cost, competition_cost, total_cost = calculate_monthly_cost(training_plan, private_hours, num_competitions)
    
    # Store record
    record = (athlete_name, TRAINING_FEES[training_plan][0], training_cost, private_hours, private_tuition_cost, num_competitions, competition_cost, total_cost, WEIGHT_CATEGORIES[competition_category])
    records.append(record)
    
    # Display summary
    print("\n---- Record Summary ----")
    print(f"Athlete: {athlete_name}")
    print(f"Training Plan: {TRAINING_FEES[training_plan][0]} (£{training_cost:.2f})")
    print(f"Private Coaching: {private_hours} hours/week (£{private_tuition_cost:.2f})")
    print(f"Competitions Entered: {num_competitions} (£{competition_cost:.2f})")
    print(f"Total Cost: £{total_cost:.2f}")
    print(f"Competition Weight Category: {WEIGHT_CATEGORIES[competition_category]}")
    print("--------------------------")
    print("Record added successfully!\n")

def main_menu():
    """Main menu for user interaction."""
    while True:
        print("\nMain Menu:")
        print("1. Add new record")
        print("2. View previous records")
        print("3. Exit")
        choice = get_valid_input("Select an option: ", ["1", "2", "3"])
        if choice == "1":
            add_record()
        elif choice == "2":
            if not records:
                print("\nNo records found.")
            else:
                print("\n---- Athlete Records ----")
                for record in records:
                    print(f"Athlete: {record[0]}, Training Plan: {record[1]}, Total Cost: £{record[7]:.2f}, Competition Weight Category: {record[8]}")
                print("--------------------------")
        elif choice == "3":
            print("Exiting program.")
            break

if __name__ == "__main__":
    main_menu()
