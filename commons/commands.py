class Command:
  def handle(self):
    raise NotImplementedError

class CommandBus:
  def execute(self,command:Command):
    command.handle()