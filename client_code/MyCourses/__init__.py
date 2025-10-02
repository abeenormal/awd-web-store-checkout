from ._anvil_designer import MyCoursesTemplate
from anvil import *
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.facebook.auth
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
from ..CourseItem import CourseItem


class MyCourses(MyCoursesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.load_courses()

    # Any code you write here will run before the form opens.
  def render_course(self, course_name):
    self.content_panel.clear

  def load_courses(self):
    courses= anvil.server.call("get_my_courses")

    if len(courses)> 0:
      self.no_courses_label.visible = False

      course_panel = GridPanel()

      for i, course in enumerate(courses):
        c = CourseItem(name=course["name"], button_text="ViewContent", description= course["description"], image= course["image"], button_callback= self.render_course)
        course_panel.add_component(c, row=str(i//2), width_xs=6)

      self.content_panel.add_component(course_panel)