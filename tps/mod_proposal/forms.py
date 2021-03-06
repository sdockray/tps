from wtforms import TextField, TextAreaField, BooleanField, SubmitField, HiddenField, SelectMultipleField
from wtforms.validators import Required
from flask.ext.login import current_user

from tps.utils.form import model_form, BaseForm, TagListField
from tps.mod_school import user_schools
from .models import Proposal


class ProposalBase(BaseForm):
	""" Full event form """
	tags = TagListField('Tags')
	field_order = ('*', 'tags', 'submit')

	def __init__(self, *args, **kwargs):
		super(ProposalBase, self).__init__(*args, **kwargs)
		if hasattr(self, 'schools'):
			self.schools.queryset = user_schools()


AddProposalForm = model_form( Proposal, 
	base_class=ProposalBase, 
	exclude=(
		'edited_description',
		'proposer',
		'schools',
		'published',
		'stage',
		'source',
		'updated',
		'created',
		'interested',
		'num_interested',
		'copy_of',
		'events',
		'discussions',
		'tags'))
submit_add = SubmitField('Propose!')
AddProposalForm.submit = submit_add


ProposalForm = model_form( Proposal, 
	base_class=ProposalBase, 
	exclude=(
		'edited_description',
		'proposer',
		'published',
		'stage',
		'source',
		'updated',
		'created',
		'interested',
		'num_interested',
		'events',
		'discussions',
		'copy_of',
		'tags'))
submit_save = SubmitField('Save')
ProposalForm.submit = submit_save


