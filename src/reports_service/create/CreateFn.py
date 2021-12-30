from common.handlebase import Handler

class CreateFn(Handler):
  def handler(self):


def handler(event, context):
  return CreateFn(event, context).run()