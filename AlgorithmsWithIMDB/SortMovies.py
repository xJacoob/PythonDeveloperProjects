class SortMovies:
    def __init__(self, movie_list):
        self.movie_list = movie_list

    def linear_search(self, target):
        sorted_list = []
        for movie in self.movie_list:
            if movie.rate == target:
                sorted_list.append(movie)

        return sorted_list

    def bubble_sort(self):
        length = len(self.movie_list)
        for i in range(length):
            for j in range(0, length - i - 1):
                if self.movie_list[j].rate > self.movie_list[j + 1].rate:
                    self.movie_list[j], self.movie_list[j + 1] = self.movie_list[j + 1], self.movie_list[j]

        return self.movie_list

    def binary_search(self, target, sorted_list):
        length = len(sorted_list)
        left = 0
        right = length - 1

        while left <= right:
            middle = (left + right) // 2
            if sorted_list[middle].rate == target:
                found_movies = []
                found_movies.append(sorted_list[middle])

                left_index = middle - 1
                while left_index >= 0 and sorted_list[left_index].rate == target:
                    found_movies.append(sorted_list[left_index])
                    left_index -= 1

                right_index = middle + 1
                while right_index < length and sorted_list[right_index].rate == target:
                    found_movies.append(sorted_list[right_index])
                    right_index += 1

                return found_movies

            elif sorted_list[middle].rate > target:
                right = middle - 1
            else:
                left = middle + 1

        return None

    def merge(self, left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i].rate <= right[j].rate:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        if i == len(left):
            result.extend(right[j:])
        else:
            result.extend(left[i:])

        return result

    def merge_sort(self, current_list):
        if len(current_list) <= 1:
            return current_list

        mid = len(current_list) // 2
        left = current_list[:mid]
        right = current_list[mid:]

        sorted_left = self.merge_sort(left)
        sorted_right = self.merge_sort(right)

        return self.merge(sorted_left, sorted_right)