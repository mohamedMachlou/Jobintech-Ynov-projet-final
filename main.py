from utils import input, radio, checkbox, select


def main():
    
    # 1️⃣ Normal text input
    name = input("Enter your name:")
    print(f"Hello, {name}!\n")

    # 2️⃣ Single choice (radio)
    favorite_lang = radio(
        "Choose your favorite programming language:",
        ["Python", "JavaScript", "Go", "Rust"],
    )
    print(f"Your favorite language is: {favorite_lang}\n")

    # 3️⃣ Multiple choice (checkbox)
    skills = checkbox(
        "Select your programming skills:", ["Python", "JavaScript", "Go", "Rust"]
    )
    print(f"You selected these skills: {skills}\n")

    # 4️⃣ Select menu
    project = select(
        "Choose a project to work on:", ["Project A", "Project B", "Project C"]
    )
    print(f"You selected project: {project}\n")


if __name__ == "__main__":
    main()
