from commitizen import BaseCommitizen

class SHCz(BaseCommitizen):
    def questions(self):
        questions = [
                {
                    'type': 'input',
                    'name': 'title',
                    'message': 'Commit title'
                    },
                {
                    'type': 'input',
                    'name': 'issue',
                    'message': 'Issue Number'
                    },
                ]
        return questions
    def message(self, answers):
        return '{0} (#{1})'.format(answers['title'], answers['issue'])
    def example(self):
        return 'Problem with user (#321)'

