class Command:
    def execute(self):
        pass


class TextEditor:
    def copy(self):
        print("Skopiowano tekst")

    def paste(self):
        print("Wklejono tekst")

    def undo(self):
        print("Cofnięto ostatnią operację")


class CopyCommand(Command):
    def __init__(self, editor):
        self.editor = editor

    def execute(self):
        self.editor.copy()


class PasteCommand(Command):
    def __init__(self, editor):
        self.editor = editor

    def execute(self):
        self.editor.paste()


class UndoCommand(Command):
    def __init__(self, editor):
        self.editor = editor

    def execute(self):
        self.editor.undo()


class Button:
    def __init__(self, command):
        self.command = command

    def click(self):
        self.command.execute()


editor = TextEditor()

copy_command = CopyCommand(editor)
paste_command = PasteCommand(editor)
undo_command = UndoCommand(editor)

copy_button = Button(copy_command)
paste_button = Button(paste_command)
undo_button = Button(undo_command)



copy_button.click()
paste_button.click()
undo_button.click()