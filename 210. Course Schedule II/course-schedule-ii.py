'''
1. Every course is a Node, with points to all prerequisites of this course (at most n course).
2. We loop through all course, and try to take the course, if we can't take the course, 
   we loop through the prerequisites and take those course.
3. When a loop is detected in step 2 (a requires b and b requires a), it's impossible to finish all course.
'''
class Course:
    def __init__(self, _id):
        self.id = _id
        self.prerequisite_ids = set()
        
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def take_course(course_id, course_order: List, taken: set, visited=set()):
            nonlocal courses
            course = courses[course_id]
            
            if course.id in taken:
                return True
            elif course.id in visited: 
                # visited but not taken! loop found!
                return False
            
            visited.add(course.id)
            
            # take prerequisites first
            for pre_course_id in course.prerequisite_ids:
                if pre_course_id not in taken:
                    success = take_course(pre_course_id, course_order, taken, visited)
                    if not success:
                        return False
            
            # take the course
            taken.add(course.id)
            course_order.append(course.id)
            return True
            
        courses = [Course(_id) for _id in range(numCourses)]
        for prereq in prerequisites:
            cur_course = prereq[0]
            pre_course = prereq[1]
            courses[cur_course].prerequisite_ids.add(pre_course)
        
        taken = set() # id of taken courses
        course_order = []
        for course_id in range(numCourses):
            success = take_course(course_id, course_order, taken)
            if not success:
                return []
        
        return course_order
            
        
    