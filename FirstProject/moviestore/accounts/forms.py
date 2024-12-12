from django.contrib.auth.forms import UserCreationForm
from django.forms.utils import ErrorList
from django.utils.safestring import mark_safe


class CustomErrorList(ErrorList):
  def __str__(self):
    if not self:
      return ''
    return mark_safe(''.join([f'<div class = "bg-red-500 text-white font-bold rounded-lg px-4 py-2 mb-4 mt-3" role = "alert">{e}</div>' for e in self]))

class CustomUserCreationForm(UserCreationForm):
  def __init__(self, *args, **kwargs):
    super(CustomUserCreationForm, self).__init__(*args, **kwargs)
    for fieldname in ['username', 'password1', 'password2']:
      self.fields[fieldname].help_text = None
      self.fields[fieldname].widget.attrs.update({ 'class' : 'mt-2 border border-gray-300 rounded-lg p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'})