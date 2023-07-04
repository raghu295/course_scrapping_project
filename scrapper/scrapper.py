import requests
from bs4 import BeautifulSoup
from db_model import DbModel

class Scrapper(object):
    BASE_URL = "https://broadwayinfosys.com/courses"

    def get_page_content(self):
        """+
        Get the page content
        :return:
        """
        response = requests.get(self.BASE_URL, headers={'User-Agent': 'Mozilla/5.0'})
        return response.content

    def parse_content(self):
        """
        Parse the content and return the list of courses
        :return:
        """
        content = self.get_page_content()
        html_content = BeautifulSoup(content, "html.parser")
        # print (html_content.prettify())

        courses = html_content.find_all("div", {"class": "col course-list-col col-md-4 col-lg-3"})
        result = []
        for course in courses:
            result.append({
                "course_name": str(course.find("strong").text).replace("\n", ""),
                "course_duration": str(course.find("p").find("strong").text).replace("\n", "") if course.find("p")
                else None,
                "course_link": course.find("a")["href"],
                "course_image": course.find("img")["data-src"],

                })
        print(result)

        return result

    def insert_to_db(self):
        db_model = DbModel()   # create an instance /object of Dbmodel
        db_data = db_model.get_all_course_name()
        if len(db_data) > 0:
            db_data = [d[0] for d in db_data if len(d) > 0]
            print("DB Data: ", db_data)
        courses = self.parse_content()
        for course in courses:
            print(course.get("course_name"), course.get("course_name") not in db_data)
            if course.get("course_name") not in []:
                print("Inserting data: ", tuple(course.values()))
            db_model.insert_data(tuple(course.values()))





if __name__ == "__main__":
    scrapper = Scrapper()
    print(scrapper.insert_to_db())