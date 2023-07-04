from db_model import DbModel



def find_course_detail(course_name):
    db_model = DbModel()
    course_detail = db_model.get_course_detail(course_name)
    if course_detail:
        course_format = f"""
                        course_id: {course_detail[0]}
                        course_name:{course_detail[1]}
                        course_duration:{course_detail[2]}
                        course_link:{course_detail[3]}
                        course_image:{course_detail[4]}
                        created_at: {course_detail[5]}"""
        return course_format
    return "Course not found"


if __name__ == "__main__":
    course_name = input("Enter course name: ")
    res = find_course_detail(course_name)
    print(res)