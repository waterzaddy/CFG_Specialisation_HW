def website_navigation(home, home_nav):
    current_url = home
    options = home_nav

    while True:
        print(f"You are currently on the URL {current_url}")
        print(f"Where are you clicking?\nOptions: {', '.join(options)}")
        user_choice = input().lower()

        if user_choice == "courses":
            current_url = courses
            options = courses_nav
        elif user_choice == "opportunities":
            current_url = opportunities
            options = opportunities_nav
        elif user_choice == "cfgdegree":
            current_url = cfg_degree
            options = subcategory_nav
        elif user_choice == "ambassadors":
            current_url = ambassadors
            options = subcategory_nav
        elif user_choice == "back":
            if current_url == courses:
                current_url = home
                options = home_nav
            elif current_url == opportunities:
                current_url = home
                options = home_nav
            elif current_url == cfg_degree:
                current_url = courses
                options = courses_nav
            elif current_url == ambassadors:
                current_url = opportunities
                options = opportunities_nav
        elif user_choice == "exit":
            print("Exiting the simulation.")
            break
        else:
            print("Invalid choice. Please choose an available option.")


# URLs
home = "https://codefirstgirls.com/"
courses = "https://codefirstgirls.com/courses"
opportunities = "https://codefirstgirls.com/opportunities"
cfg_degree = "https://codefirstgirls.com/courses/cfgdegree/"
ambassadors = "https://codefirstgirls.com/opportunities/ambassadors/"

# Navigation options
home_nav = ["Courses", "Opportunities", "Exit"]
courses_nav = ["CFGDegree", "Back", "Exit"]
opportunities_nav = ["Ambassadors", "Back", "Exit"]
subcategory_nav = ["Back", "Exit"]

# Run user navigation
website_navigation(home, home_nav)
