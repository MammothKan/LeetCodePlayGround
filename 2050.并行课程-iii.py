#
# @lc app=leetcode.cn id=2050 lang=python3
#
# [2050] 并行课程 III
#

# @lc code=start
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
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
            prev_graph[next-1].append(prev-1)

        # 动态规划
        time_4_complete_course = [-1 for _ in range(n)]
        def dp(course_idx: int):
            if time_4_complete_course[course_idx] > 0:
                return time_4_complete_course[course_idx]
            else:
                if prev_graph[course_idx] == []:
                    return time[course_idx]
                else:
                    return time[course_idx] + max(dp(prev_idx) for prev_idx in prev_graph[course_idx])

        for course_idx in range(n):
            print(time_4_complete_course)
            time_4_complete_course[course_idx] = dp(course_idx)
        
        return max(time_4_complete_course)

# @lc code=end

