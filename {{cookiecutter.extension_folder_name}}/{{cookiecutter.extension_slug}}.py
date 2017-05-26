###Make your imports


###Declare your global outputs
__all__ = []


#Main Extension Class
##Replace the FlaskExtension with your desired extension class name
class {{ cookiecutter.extension_class_name|title}}:
    """
    Doc string.
    Explain your extension in detail here.
    """

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        '''Initalizes the application with the extension.
        :param app: The Flask application object.
        '''
        pass
