from Candidate import Candidate
from Recruitment import Recruitment


def main():
    n_capacity = int(input())
    candidate_list = []

    with open("applicants.txt", "r") as file:
        for line in file:
            data = line.split()
            new_candidate = Candidate(data[0], data[1], data[7:], float(data[2]), float(data[3]), float(data[4]), float(data[5]), float(data[6]))
            candidate_list.append(new_candidate)

    recruitment_process = Recruitment(n_capacity, candidate_list)
    recruitment_process.allocation()
    recruitment_process.print_result()
    recruitment_process.write_to_file()

if __name__ == "__main__":
    main()