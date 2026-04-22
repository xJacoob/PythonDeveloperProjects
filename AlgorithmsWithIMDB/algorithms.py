from Reader import Reader
from SortMovies import SortMovies

def main():
    reader = Reader("movies.csv")
    data = reader.read_csv()
    management_data = SortMovies(data)
    merge_sort = management_data.merge_sort(management_data.movie_list)
    binary_search = management_data.binary_search(6.0, merge_sort)

    for movie in binary_search:
        print(movie)

if __name__ == "__main__":
    main()