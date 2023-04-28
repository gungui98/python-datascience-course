import glob
import subprocess
import argparse

def get_args():
    args = argparse.ArgumentParser()
    args.add_argument("--week", type=int, default=1)
    return args.parse_args()

if __name__ == "__main__":
    args = get_args()
    test_folder = f"week_ ({args.week})"
    notebook_files = glob.glob(f"{test_folder}/*exercise*.ipynb") + glob.glob(f"{test_folder}/*Exercise*.ipynb")
    notebook_files = list(set(notebook_files))
    all_notebooks_passed = True
    print(f"Testing {len(notebook_files)} notebooks.")
    for notebook_file in notebook_files:
        print(f"Testing {notebook_file}")
        # Check if the notebook passes the tests
        output = subprocess.run(["jupyter", "nbconvert", "--to", "html", "--execute", notebook_file], capture_output=True)
        if output.returncode != 0:
            all_notebooks_passed = False
            print(f"The notebook {notebook_file} failed the tests.")
            print(output.stderr.decode("utf-8"))
            exit(1)
