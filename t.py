def minimumTime(n, relations, time):
    """
    Args:
        n:          int          the number of the courses
        relations:  list[list]   the relationships between courses, for example relations[j] = [prevCourse_j, nextCourse_j]
        time:       list[int]    number of month required to complete j_th course
    Returns:
        the minimum number of month required to complete all courses
    """
    
    # adjacency list for prevCourses
    prev_graph = [[] for _ in range(n)]
    for (prev, next) in relations:
        print(prev)
        print(next)
        prev_graph[next-1].append(prev-1)
    print(prev_graph)
    

    # 动态规划
    time_4_complete_course = [-1 for _ in range(n)]
    def dp(course_idx):
        if time_4_complete_course[course_idx] > 0:
            return time_4_complete_course[course_idx]
        # if prev_graph[course_idx] == []:
        #     return time[course_idx]
        else:
            return time[course_idx] + max(dp(prev_idx) for prev_idx in prev_graph[course_idx])

    for course_idx in range(n):
        time_4_complete_course[course_idx] = dp(course_idx)
    
    return max(time_4_complete_course)


if __name__ == '__main__':
    #  n = 3
    #  relations = [[1,3], [2,3]]
    #  time = [3,2,5]

    n = 5
    #  relations = [[1,5], [2,5], [3,5], [3,4], [4,5]]
    relations = []
    time = [1,2,3,4,5]

    answer = minimumTime(n, relations, time)
    print(answer)

    # for i in []:
    #     print(i)