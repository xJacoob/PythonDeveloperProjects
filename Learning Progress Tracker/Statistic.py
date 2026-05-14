from Students import Students

class Statistic:

    """
    Statistics for courses
    """

    statistics = {
        "Most popular": "n/a",
        "Least popular": "n/a",
        "Highest activity": "n/a",
        "Lowest activity": "n/a",
        "Easiest course": "n/a",
        "Hardest course": "n/a"
    }

    points_to_complete = {
        "Python": 600,
        "DSA": 400,
        "Databases": 480,
        "Flask": 550
    }

    @classmethod
    def most_and_least_popular(cls, student_information: dict[str, Students]):
        enrollments = {"Python": 0, "DSA": 0, "Databases": 0, "Flask": 0}
        for key, value in student_information.items():
            for course, score in value.points.items():
                if score > 0:
                    enrollments[course] += 1

        max_values = max(enrollments.values())
        min_values = min(enrollments.values())
        most_popular_courses = []

        if max_values == 0:
            cls.statistics["Most popular"] = "n/a"
        else:
            most_popular_courses = [course for course, score in enrollments.items() if score == max_values]
            cls.statistics["Most popular"] = ", ".join(most_popular_courses)

        if min_values == 0:
            cls.statistics["Least popular"] = "n/a"
        else:
            least_popular_courses = [course for course, score in enrollments.items() if score == min_values and course not in most_popular_courses]
            if not least_popular_courses:
                cls.statistics["Least popular"] = "n/a"
            else:
                cls.statistics["Least popular"] = ", ".join(least_popular_courses)

    @classmethod
    def highest_and_lowest_activity(cls):
        activity = Students.course_activity
        min_value = min(activity.values())
        max_value = max(activity.values())
        highest_activity = []

        if max_value == 0:
            cls.statistics["Highest activity"] = "n/a"
        else:
            highest_activity = [course for course, score in activity.items() if score == max_value]
            cls.statistics["Highest activity"] = ", ".join(highest_activity)

        if min_value == 0:
            cls.statistics["Lowest activity"] = "n/a"
        else:
            lowest_activity = [course for course, score in activity.items() if score == min_value and course not in highest_activity]
            if not lowest_activity:
                cls.statistics["Lowest activity"] = "n/a"
            else:
                cls.statistics["Lowest activity"] = ", ".join(lowest_activity)

    @classmethod
    def hardest_and_easiest_courses(cls, student_information: dict[str, Students]):
        average_points = {"Python": 0, "DSA": 0, "Databases": 0, "Flask": 0}
        for key, value in student_information.items():
            for course, score in value.points.items():
                submissions = Students.course_activity[course]
                try:
                    average = score / submissions
                    average_points[course] = average
                except ZeroDivisionError:
                    print("Can't divide by zero")

        min_value = min(average_points.values())
        max_value = max(average_points.values())
        hardest_courses = []

        if min_value == 0:
            cls.statistics["Hardest course"] = "n/a"
        else:
            hardest_courses = [course for course, score in average_points.items() if score == min_value]
            cls.statistics["Hardest course"] = ", ".join(hardest_courses)

        if max_value == 0:
            cls.statistics["Easiest course"] = "n/a"
        else:
            easiest_courses = [course for course, score in average_points.items() if score == max_value and course not in hardest_courses]
            if not easiest_courses:
                cls.statistics["Easiest course"] = "n/a"
            else:
                cls.statistics["Easiest course"] = ", ".join(easiest_courses)


    @classmethod
    def details(cls, student_information: dict[str, Students], which_course: str):
        details_value = []
        for key, value in student_information.items():
            for course, points in value.points.items():
                if points > 0 and which_course == course:
                    percentage = points / cls.points_to_complete[course] * 100
                    details_value.append((key, points, round(percentage, 1)))

        sorted_details = sorted(details_value, key=lambda x: (-x[1], int(x[0])))

        return sorted_details


