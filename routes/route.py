from controller.generate import summarize
def initialize_routes(api):
    api.add_resource(summarize,'/summarize')