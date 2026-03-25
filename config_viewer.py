import csv

CONFIG_FILE = "robot_config.csv"


def display_config() -> None:
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            rows = list(reader)

            if len(rows) <= 1:
                print("No robot configuration data found.")
                return

            print("\nROBOT CONFIGURATION DATA")
            print("-" * 40)

            for row in rows:
                print(" | ".join(row))

    except FileNotFoundError:
        print("Robot configuration file not found.")
    except OSError as error:
        print(f"Error reading robot configuration data: {error}")


if __name__ == "__main__":
    display_config()
