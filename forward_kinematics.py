import math
from typing import Tuple


def degrees_to_radians(angle_degrees: float) -> float:
    return math.radians(angle_degrees)


def forward_kinematics(link1: float, link2: float, theta1_deg: float, theta2_deg: float) -> Tuple[float, float]:
    theta1 = degrees_to_radians(theta1_deg)
    theta2 = degrees_to_radians(theta2_deg)

    x = link1 * math.cos(theta1) + link2 * math.cos(theta1 + theta2)
    y = link1 * math.sin(theta1) + link2 * math.sin(theta1 + theta2)

    return x, y


def display_result(link1: float, link2: float, theta1: float, theta2: float, x: float, y: float) -> None:
    print("\nFORWARD KINEMATICS")
    print("-" * 40)
    print(f"Link 1 length: {link1:.2f}")
    print(f"Link 2 length: {link2:.2f}")
    print(f"Theta 1: {theta1:.2f} degrees")
    print(f"Theta 2: {theta2:.2f} degrees")
    print(f"End-effector position: ({x:.2f}, {y:.2f})")


def main() -> None:
    link1 = 5.0
    link2 = 3.0
    theta1 = 30.0
    theta2 = 45.0

    x, y = forward_kinematics(link1, link2, theta1, theta2)
    display_result(link1, link2, theta1, theta2, x, y)


if __name__ == "__main__":
    main()
