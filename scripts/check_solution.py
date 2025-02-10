"""
check a single solution for a problem
"""
import sys
import json
import re
from argparse import ArgumentParser
import subprocess


def run_on_single_game(program: str, game_path: str) -> str:
    result = subprocess.run([sys.executable, program, game_path],
                            capture_output=True, check=True)
    return result.stdout.decode("utf-8").strip()


def main():
    parser = ArgumentParser(description="check a single solution for a problem")
    parser.add_argument("question", help="question path")
    parser.add_argument("program", help="program to check")
    args = parser.parse_args()
    gt_file = f"{args.question}_gt.json"
    with open(gt_file) as f:
        gt_dict = json.load(f)

    answer_regex = gt_dict["output_regex"]
    for answer in gt_dict["answers"]:
        game_path = answer["game"]
        expected = answer["result"]
        result = run_on_single_game(args.program, game_path)
        # todo: record keeping and statistics
        if result == expected:
            print(f"Success: {game_path}")
            continue
        if not re.match(answer_regex, result):
            print(f"Error: {game_path}")
            print(f"Expected: {expected}")
            print(f"Got: {result} which does not match the regex {answer_regex}")
            print()
            continue
        print(f"Failed: {game_path}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print()


if __name__ == "__main__":
    main()
