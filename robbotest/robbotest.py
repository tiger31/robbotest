"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources
from web_fragments.fragment import Fragment
from xblock.core import XBlock
from xblock.fields import Integer, String, Scope
from xblockutils.resources import ResourceLoader

loader = ResourceLoader(__name__)


class RobboTestXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    # TO-DO: delete count, and define your own fields.
    count = Integer(
        default=0, scope=Scope.user_state,
        help="A simple counter, to show something happening",
    )

    question = String(
        default="What is 0 + 0?", scope=Scope.content,
        help="Question"
    )

    answer = String(
        scope=Scope.content,
        default="0", help="Question answer",
    )



    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the RobboTestXBlock, shown to students
        when viewing courses.
        """
        frag = Fragment()
        frag.add_content(
            loader.render_django_template(
                '/static/html/test.html',
                context=context,
                i18n_service=self.runtime.service(self, 'i18n')
            )
        )
        frag.add_css(self.resource_string("static/css/test.css"))
        frag.add_javascript(self.resource_string("static/js/src/vue.js"))
        frag.add_javascript(self.resource_string("static/js/src/vue-foo.min.js"))
        frag.add_javascript(self.resource_string("static/js/src/test.js"))
        frag.initialize_js('TestXBlock')

        #frag.initialize_js('RobboTestXBlock')
        return frag

    def studio_view(self, context=None):
        """
        The primary view of the TestXBlock, shown to students
        when viewing courses.
        """
        frag = Fragment()
        frag.add_content(
            loader.render_django_template(
                '/static/html/test_editor.html',
                context=context,
                i18n_service=self.runtime.service(self, 'i18n')
            )
        )
        frag.add_css(self.resource_string("static/css/test.css"))
        frag.add_javascript(self.resource_string("static/js/src/vue.js"))
        frag.add_javascript(self.resource_string("static/js/src/vue-foo.min.js"))
        frag.add_javascript(self.resource_string("static/js/src/test_editor.js"))
        frag.initialize_js('TestXBlockEditor')
        return frag

    # TO-DO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.
    @XBlock.json_handler
    def increment_count(self, data, suffix=''):
        """
        An example handler, which increments the data.
        """
        # Just to show data coming in...
        assert data['answer'] == self.answer

        self.count += 1
        return {"count": self.count}

    @XBlock.json_handler
    def studio_submit(self, data, suffix=''):
        self.question = data['question'];
        self.answer = data['answer'];
        return data;

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("RobboTestXBlock",
             """<robbotest/>
             """),
            ("Multiple RobboTestXBlock",
             """<vertical_demo>
                <robbotest/>
                <robbotest/>
                <robbotest/>
                </vertical_demo>
             """),
        ]
