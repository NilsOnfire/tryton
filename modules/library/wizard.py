from trytond.model import ModelView
from trytond.wizard import Wizard, StateView, StateTransition, StateAction
from trytond.wizard import Button

__all__ = [
    'CreateExemplaries',
    'CreateExemplariesParameters',
    ]


class CreateExemplaries(Wizard):
    'Create Exemplaries'
    __name__ = 'library.book.create_exemplaries'


class CreateExemplariesParameters(ModelView):
    'Create Exemplaries Parameters'
    __name__ = 'library.book.create_exemplaries.parameters'