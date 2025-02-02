import argparse
#from dotenv import load_dotenv
import os
from src.infra.instance_loader import load_instance
from src.application.flowshop_solver import solve_flowshop

def main():
    # load env
    #load_dotenv()

    parser = argparse.ArgumentParser(
        description="Flowshop scheduling problem solver"
    )
    parser.add_argument("instance", help="instance file path")
    args = parser.parse_args()

    try:
        jobs = load_instance(args.instance)
    except Exception as e:
        print("Error:", e)
        return

    result = solve_flowshop(jobs)
    if result["sequence"] is not None:
        sequence_names = [jobs[i].name for i in result["sequence"]]
        print("best sequence:", sequence_names)
        print("minimum makespan:", result["makespan"])
    else:
        print("no solution found")

if __name__ == "__main__":
    main()
